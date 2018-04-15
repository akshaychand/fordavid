FROM postgres:alpine AS build

LABEL maintainer="Akshay Chand <chand.akshay@gmail.com>"

# Run the rest of the commands as the ``postgres``
# user created by the ``postgres` package
USER postgres

ENV APP_USER=www-data
ENV APP_PASSWORD=mysecretpassword

COPY ./postgres/initsql/*.sh /docker-entrypoint-initdb.d/

