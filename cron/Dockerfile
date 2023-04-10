FROM alpine:3.15

# Update the package index
RUN apk update

# Set the timezone to America/Sao_Paulo
RUN apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" > /etc/timezone

# Install required packages
RUN apk add --update --no-cache bash dos2unix

# Install python/pip
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip --upgrade
ENV PYTHONUNBUFFERED=1

# # install any Python requirements used by the jobs
# RUN pip3 install colorama

WORKDIR /usr/scheduler

# Copy files
COPY api.py .
COPY update_actives.py .
COPY crontab.* ./
COPY start.sh .
COPY .env .
COPY config.py .
COPY utils.py .
COPY requirements.txt ./requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Convert files to Unix format
RUN dos2unix crontab.*

# # Make shell script files executable
# RUN find . -type f -iname "*.sh" -exec chmod +x {} \;

# Make Python script files executable
RUN find . -type f -iname "*.py" -exec chmod +x {} \;

# create cron.log file
RUN touch /var/log/cron.log

# Run cron on container startup
RUN chmod +x ./start.sh
CMD ["./start.sh"]