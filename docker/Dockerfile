FROM python:3.9.5-slim-buster as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

SHELL ["/bin/bash", "-c"]

COPY . /opt/TenBagger
WORKDIR  /opt/TenBagger

RUN pip3 install --user . 

RUN ls /opt/TenBagger


