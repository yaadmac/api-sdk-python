FROM python:2.7

MAINTAINER Adrian Meza

RUN apt-get update
RUN apt-get install -y vim wget curl git

#One Time Staging Steps

RUN git clone https://github.com/adrian-zumbler/api-sdk-python
WORKDIR /api-sdk-python

#additional python libs
RUN pip install -e .