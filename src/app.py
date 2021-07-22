import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from text import textprocess
from scrape.ScrapeTwint import ScrapeHashtagTwint
from datetime import datetime, timedelta

from transformers import pipeline
from google_trans_new import google_translator


class WriteApp:
    def __init__(self, path):
        self._df = pd.read_csv(path + 'tweets.csv', sep='\t')
        self.tweets = None

    @staticmethod
    def data(self):
        return self._df

    @staticmethod
    def tokenized_text(self):
        return self.tweets_tokenized

    def remove_columns(self, columns_remove):
        self._df = self._df.drop(columns_remove, axis=1)
        return self

    def select_tweets(self):
        self.tweets = self._df['tweet']
        self.puretweets = self._df['tweet']
        return self

    def remove_url(self):
        self.tweets = textprocess.remove_url(list(self.tweets))
        return self

    def tokenize(self):
        self.tweets_tokenized = textprocess.tokenize_text(self.tweets)
        return self

    def remove_punctuation(self):
        self.tweets = textprocess.remove_punctuation(self.tweets)
        return self

    def remove_stopwords(self):
        import os; os.listdir()
        stopwords = np.loadtxt('stopwords.txt', dtype=str)
        self.tweets_tokenized = textprocess.remove_stopwords(
                                text.tweets_tokenized, stopwords)
        return self

    def generate_wordcloud(self, max_font_size: int,
                           width: int, height: int, figsize: tuple):
        WC = textprocess.get_text_cloud(self.tweets_tokenized)
        word_cloud = WordCloud(max_font_size=max_font_size,
                               width=width, height=height)
        word_cloud.generate(WC)
        imagem = plt.figure(figsize=figsize)
        plt.imshow(word_cloud)
        plt.axis('off')
        return imagem

    def showrandomtweet(self):
        example = np.random.choice(self.puretweets)
        st.write(example)
        return self

    def translate_and_analize(self):
        translator = google_translator()

        classifier = pipeline('sentiment-analysis')

        translations = translator.translate(self.tweets, lang_tgt='en')

        analysis_tot = [classifier(tweet)[0] for tweet in translations]

        print(analysis_tot)

        labels = [analysis['label'] for analysis in analysis_tot]

        analysis_statistic = [ labels.count('POSITIVE')/len(self.tweets) , labels.count('NEGATIVE')/len(self.tweets) ]

        mean_score = np.mean([analysis['score'] for analysis in analysis_tot])

        return analysis_statistic, mean_score



lingua = st.sidebar.selectbox('', ['pt', 'en'])

if lingua == 'en':

    st.title('Tweetcraft')

    st.write("")

    st.header("An App by @sa_nahum and @RioJanu")

    st.write("")
    st.write("")

    st.write("Welcome to Tweetcraft!")

    st.write("Enjoy a brief journey into the wonders of \
              Twitter scraping and processing")

    st.write("")

    st.write("First off, choose a word of your musing... \
    an ingredient to the magik spell")

    hash = st.text_input('Scrape Twitter for your target word! ;)')

    st.write("")

    st.write("Now, choose a time frame! Tweetcraft \
            dwells on fresh data, \
            so it will scrape twitter for the last \
            N minutes where N is yours \
            to input! remember a very large N \
            will make the process slower")

    timelapse = st.number_input('Twitter in the last N minutes!',
                                value=5, max_value=30, min_value=1)

    d = datetime.today() - timedelta(hours=0, minutes=timelapse)
    horadia = d.strftime("%Y-%m-%d %H:%M:%S")

    ScrapeHashtagTwint(hash, horadia)

    if hash:
        text = WriteApp(hash)
        columns_to_temove = ['id', 'conversation_id', 'created_at',
                             'time', 'timezone', 'user_id', 'username',
                             'name', 'place',  'language', 'mentions',
                             'urls', 'photos', 'replies_count',
                             'retweets_count', 'likes_count', 'date',
                             'hashtags', 'cashtags', 'link', 'retweet',
                             'quote_url', 'video', 'thumbnail', 'near',
                             'geo', 'source', 'user_rt_id', 'user_rt',
                             'retweet_id', 'reply_to', 'retweet_date',
                             'translate', 'trans_src', 'trans_dest']
        text = text.remove_columns(columns_to_temove)
        text = text.select_tweets().remove_url().remove_punctuation()
        text = text.tokenize().remove_stopwords()

        st.write(text.generate_wordcloud(500, 500, 535, (16, 9)))

        st.write("")

        st.write("Checkout one random tweet from the collection \
                  you've just downloaded")

        st.write("")

        text.showrandomtweet()

        st.write("")

        st.write("Now let's do a quick dive into the Sentiment within our tweet set!")

        stat, mean_score = text.translate_and_analize()

        st.write("How much Positivity we found around this word?")

        streamlit.progress(stat[0])

        st.write("What is the confidence score of this analysis")

        streamlit.progress(stat[0])

elif lingua == 'pt':

    st.title('Tweetcraft')

    st.write("")

    st.header("Um App de @sa_nahum e @RioJanu")

    st.write("")
    st.write("")

    st.write("Benvindo ao Tweetcraft!")

    st.write("Curta uma breve jornada pelas maravilhas \
            da extração e processamento de dados do Twitter")

    st.write("")

    st.write("Primeiramente, escolha uma palavra do seu interesse... \
    um ingrediente para o feitiço")

    hash = st.text_input('Busque o Twitter pela sua palavra alvo! ;)')

    st.write("")

    st.write("Agora escolha uma janela temporal! Tweetcraft \
            trabalha com dados frescos quentinhos do forno, \
            então ele buscará o Twitter \
            nos N últimos minutos onde N é sua \
            escolha! lembre-se que um N muito grande \
            deixa o processo mais lento")

    timelapse = st.number_input('Twitter nos últimos N minutos!',
                                value=5, max_value=30, min_value=1)

    d = datetime.today() - timedelta(hours=0, minutes=timelapse)
    horadia = d.strftime("%Y-%m-%d %H:%M:%S")

    ScrapeHashtagTwint(hash, horadia)

    if hash:
        text = WriteApp(hash)
        columns_to_temove = ['id', 'conversation_id', 'created_at',
                             'time', 'timezone', 'user_id', 'username',
                             'name', 'place',  'language', 'mentions',
                             'urls', 'photos', 'replies_count',
                             'retweets_count', 'likes_count', 'date',
                             'hashtags', 'cashtags', 'link', 'retweet',
                             'quote_url', 'video', 'thumbnail', 'near',
                             'geo', 'source', 'user_rt_id', 'user_rt',
                             'retweet_id', 'reply_to', 'retweet_date',
                             'translate', 'trans_src', 'trans_dest']
        text = text.remove_columns(columns_to_temove)
        text = text.select_tweets().remove_url().remove_punctuation()
        text = text.tokenize().remove_stopwords()

        st.write(text.generate_wordcloud(500, 500, 535, (16, 9)))

        st.write("")

        st.write("Dá uma olhada em um tweet aleatório do conjunto baixado")

        st.write("")

        text.showrandomtweet()

        st.write("")

        #st.write("Now let's do a quick dive into the Sentiment within our tweet set!")

        st.write("Agora vamos dar um rápido mergulho no Sentimento presente nesse conjunto de tweets!")

        stat, mean_score = text.translate_and_analize()

        st.write("Quanta Positividade encontramos ao redor dessa palavra?")

        st.progress(stat[0])

        st.write("Qual é a nota de confiança dessa análise?")

        st.progress(mean_score)


st.button("Re-run")
