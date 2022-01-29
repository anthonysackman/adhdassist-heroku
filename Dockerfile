# syntax=docker/dockerfile:1

FROM python:3.10.2-alpine

COPY ./requirements.txt /docker-app/requirements.txt

WORKDIR /docker-app

EXPOSE 5000

RUN pip install -r requirements.txt

COPY . /docker-app

CMD ["flask", "run", "--host=0.0.0.0"]