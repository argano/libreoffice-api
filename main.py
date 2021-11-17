from flask import Flask, request
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import tempfile
import os
import json
import subprocess

app = Flask(__name__)


@app.route("/convert", methods=['POST'])
@cross_origin(origin="*")
def convert():
    # type = request.form["type"]
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file_type = filename.split(".")
    ext = file_type[1]
    outdata = ""
    with tempfile.TemporaryDirectory() as dname:
        input_filepath = os.path.join(dname, "target." + ext)
        file.save(input_filepath)
        cmd = f"soffice --headless --convert-to html --outdir {dname} {input_filepath}"
        print(cmd)
        try:
            result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            if result.returncode != 0:
                raise IOError(f"{input_filepath} failed to switch")
            print(os.path.join(dname, "target." + ext))
            outfile = open(os.path.join(dname, "target." + "html"), "r")
            outdata = outfile.read()
        except Exception as e:
            print(e)
            json.dumps({
                "result": "error"
            })
        msg = {
            "result": outdata
        }
    return json.dumps(msg)

if __name__ == "__main__":
    app.run(port=8000, host = "0.0.0.0")
