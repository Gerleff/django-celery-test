FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc vim curl wget zlib1g zsh

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/localtime

COPY . ./

# Remove psycopg2 requirements, install psycopg2-binary instead
RUN sed -i '/psycopg2/d' requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install flake8 psycopg2-binary==2.8.6

