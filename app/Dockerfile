# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add ffmpeg
# install dependencies

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib



RUN pip install --upgrade pip



COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
run pip install --upgrade youtube-dl
run pip install --upgrade ipython
run pip install --upgrade awscli
run pip install pytest
run pip install Pillow
run pip install djangorestframework
COPY ./runtests.py /usr/src/app/runtests.py
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
