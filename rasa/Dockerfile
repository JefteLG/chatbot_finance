FROM rasa/rasa:3.4.0-full

USER root
WORKDIR /app
COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN python -m spacy download pt_core_news_lg

ENTRYPOINT ["rasa", "run", "--enable-api", "--cors", "'*'", "--debug"]