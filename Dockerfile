FROM python:3.7-alpine
MAINTAINER Muma Justice

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers

RUN mkdir /app
WORKDIR /app
COPY ./app /app


