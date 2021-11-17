from flask import Flask, request, send_file, abort
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import tempfile
import os
import json
import subprocess

app = Flask(__name__)

def get_full_class_name(obj):
    module = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + '.' + obj.__class__.__name__

@app.route("/convert", methods=['POST'])
@cross_origin(origin="*")
def convert():
    type = request.form["type"]
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file_type = filename.split(".")
    ext = file_type[1]
    outdata = ""
    with tempfile.TemporaryDirectory() as dname:
        input_filepath = os.path.join(dname, "target." + ext)
        file.save(input_filepath)
        cmd = f"soffice --headless --convert-to {type} --outdir {dname} {input_filepath}"
        try:
            result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            if result.returncode != 0:
                raise IOError(f"{input_filepath} failed to convert")
            outfilepath = os.path.join(dname, "target." + type)
            return send_file(outfilepath)
        except Exception as e:
            ename = get_full_class_name(e)
            return ename, 400

if __name__ == "__main__":
    app.run(port=8000, host = "0.0.0.0")
