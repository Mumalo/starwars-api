FROM python:3.9-alpine
MAINTAINER Muma Justice

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN mkdir /starwars
WORKDIR /starwars
COPY ./starwars /starwars


