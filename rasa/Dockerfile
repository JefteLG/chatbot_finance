FROM rasa/rasa:3.4.0-full

USER root
WORKDIR /app
COPY . .

ENTRYPOINT ["rasa", "run", "--enable-api", "--cors", "'*'", "--debug"]