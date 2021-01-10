FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip locales language-pack-ja-base language-pack-ja
RUN locale-gen ja_JP.UTF-8
ADD requirements.txt /home/requirements.txt
WORKDIR /home
RUN pip3 install -r requirements.txt