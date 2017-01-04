FROM python:3.5.2
MAINTAINER Sanket Saurav <sanketsaurav@gmail.com>

# setup source dir
RUN mkdir /poe
WORKDIR /poe
ADD . /poe/

# install the requirements
RUN pip install -r requirements.txt

# start python development server
CMD ['python', 'poe/app.py']
