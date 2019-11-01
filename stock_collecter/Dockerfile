FROM ubuntu:16.04

RUN apt-get update && apt-get -y install cron

# Copy hello-cron file to the cron.d directory
COPY hello-cron /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN crontab /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
# CMD cron && tail -f /var/log/cron.log
CMD ["cron", "-f"]

# COPY . /app
# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev
# RUN pip install -r /app/requirements.txt
# FROM stock_collecter
# CMD ["python /app/src/Stock.py init"]
# CMD ["python /app/src/Stock.py request -symbol MSFT"]
# CMD ["flask", "run"]

