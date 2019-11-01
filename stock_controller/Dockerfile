FROM ubuntu:18.04

# Crontab fix
RUN apt-get update && apt-get -y install cron
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab


WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
# ENV STOCK_DB_PATH /app/src/resources/stocks.db
ENV STOCK_DB_PATH /db/test.db

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /app/src/controller

ENTRYPOINT ["flask", "run"]
# CMD ["flask", "run"]
