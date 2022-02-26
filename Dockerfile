FROM python:3.7-alpine
MAINTAINER Aishwarya Prabhat

#prevent buffering and allow logs to show up immediately on stream
ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt 

RUN mkdir /app
WORKDIR /app 
COPY ./app /app

#security best practice
RUN adduser -D user
USER user

