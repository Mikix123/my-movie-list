# start with a base image
FROM python:3.7
ENV PYTHONUNBUFFERED 1

MAINTAINER Michal Kurasz, Krzysztof Drozd

ARG environment

RUN mkdir /code
WORKDIR /code

COPY . /code/

# build app
RUN pip install -r requirements.txt

ENV	DJANGO_SETTINGS_MODULE movie_app.settings.${environment:-docker}

# expose port 8000 for us to use
EXPOSE 8000