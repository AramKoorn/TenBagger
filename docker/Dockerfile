FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential python3 python3-pip python3-dev \
    gosu libsasl2-dev libsasl2-2 libsasl2-modules-gssapi-mit git \
	openssh-client postgresql curl openjdk-11-jdk libfreetype* pkg-config

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

SHELL ["/bin/bash", "-c"]

COPY . /opt/TenBagger
WORKDIR  /opt/TenBagger

RUN ls 
