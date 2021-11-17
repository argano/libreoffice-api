# libreoffice-api

Web API to call libreoffice headless function.

## Usage

```
pip install -r requirements.txt
python main.py # or gunicorn -b 0.0.0.0:8000 main:app
```

## Docker Image

[argano/libreoffice-api](https://hub.docker.com/r/argano/libreoffice-api)

### Build

```
docker build -t argano/libreoffice-api:lastest --network host .
```

## API

### POST /convert

- body: multipart/form-data
    - fields:
      - file: binary file
      - type: argument of `--convert-to`

## Contribution

1. Fork it ( http://github.com/argano/libreoffice-api )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## License

MIT
