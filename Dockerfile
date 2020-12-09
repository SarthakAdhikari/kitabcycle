FROM python:3.7-alpine
MAINTAINER Sarthak

ENV PYTHONUNBUFFERED 1

COPY ../requirements.txt ./requirements.txt
