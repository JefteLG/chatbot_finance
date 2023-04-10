FROM python:3.8-slim-buster

WORKDIR /app
RUN apt-get update
RUN apt-get install locales -y

RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt_br
ENV LC_ALL pt_BR.UTF-8
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

COPY requirements.txt ./requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . ./actions
#RUN rm -rf actions/tests

ENTRYPOINT python -m rasa_sdk --actions actions --debug
