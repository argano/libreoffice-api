FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && apt-get install -y libreoffice python3-pip curl

COPY . .

RUN python3 -m pip install -r ./requirements.txt

EXPOSE 8000

CMD [ "python3", "-m", "gunicorn", "--bind", "0.0.0.0:8000", "--log-level", "debug", "main:app" ]
