############
### run ###
############

# base image
FROM python:3.8

LABEL maintainer = "jadikesavan1@sheffield.ac.uk"

# Intall packages from requirements.txt
COPY  requirements.txt requirements.txt
COPY docker/wait-for-it.sh /wait-for-it.sh

RUN pip3 install -r requirements.txt --no-cache-dir

WORKDIR app

RUN chmod +x /wait-for-it.sh
