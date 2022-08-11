FROM python:3.10.2-slim-buster

WORKDIR /dnsr

COPY . .
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install nano
RUN apt-get install -y iputils-ping
RUN apt-get install -y iputils-ping
RUN apt-get install -y net-tools
ENV TZ=America/Toronto

CMD ["python3", "./main.py"]