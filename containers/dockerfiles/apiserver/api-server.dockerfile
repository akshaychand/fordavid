FROM ubuntu:16.04

LABEL maintainer="Akshay Chand <chand.akshay@gmail.com>"

ENV APP_ENV development

ENV INSTALL_PATH /loanviz

RUN mkdir -p $INSTALL_PATH/logs

# Create an app user so our program doesn't run as root.
RUN useradd -c 'LoanViz User' -m -d /home/loanviz-user -s /bin/bash loanviz-user

# apt-get and system utilities
RUN apt-get update
    && apt-get install -y libssl-dev libldap2-dev libffi-dev libpq-dev \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5 \
    && rm -rf /var/lib/apt/lists/*
    && apt-get -y install unixodbc unixodbc-dev

# python libraries
RUN python3-pip python3-dev python3-setuptools --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# install necessary locales
RUN apt-get update
    && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

RUN pip3 install --upgrade pip

# install SQL Server Python SQL Server connector module - pyodbc
RUN pip3 install pyodbc

RUN curl -LO https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh && \
    bash Anaconda3-4.2.0-Linux-x86_64.sh -p /Anaconda3 -b && \
    rm Anaconda3-4.2.0-Linux-x86_64.sh

ENV PATH $PATH:/Anaconda3/bin
RUN conda update -y conda

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR $INSTALL_PATH

COPY . .

RUN chown -R loanviz-user $INSTALL_PATH

USER loanviz-user

EXPOSE 5000 5555 8080 8000 80

CMD /usr/local/bin/gunicorn -b 0.0.0.0:5000 --access-logfile - "server:app"