import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from text import textprocess
from scrape.ScrapeTwint import ScrapeHashtagTwint
from datetime import datetime, timedelta


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
        stopwords = list(pd.read_fwf('stopwords.txt', header = None)[0])
        self.tweets_tokenized = textprocess.remove_stopwords(text.tweets_tokenized, stopwords)
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


st.title('Tweetcraft')

st.write("")

st.write("Welcome to Tweetcraft! Enjoy a brief journey into the wonders of Twitter scraping and processing")

st.write("")

st.write("First off, choose a word of your musing... an ingredient to the magik spell")

hash = st.text_input('Scrape Twitter for your target word! ;)')

st.write("")

st.write("Now, choose a time frame! Tweetcraft dwells on fresh data, so it will scrape twitter for the last N minutes Where N is yours to input! remember a very large N will make the process slower")

timelapse = st.number_input('Twitter in the last N minutes!', value = 5, max_value = 30, min_value = 1)

d = datetime.today() - timedelta(hours=0, minutes=timelapse)
horadia = d.strftime("%Y-%m-%d %H:%M:%S")

ScrapeHashtagTwint(hash, horadia)

if hash:
    text = WriteApp(hash)
    columns_to_temove = ['id', 'conversation_id', 'created_at', 'date',
                         'time', 'timezone', 'user_id', 'username', 'name',
                         'place',  'language', 'mentions', 'urls', 'photos',
                         'replies_count', 'retweets_count', 'likes_count',
                         'hashtags', 'cashtags', 'link', 'retweet',
                         'quote_url', 'video', 'thumbnail', 'near',
                         'geo', 'source', 'user_rt_id', 'user_rt',
                         'retweet_id', 'reply_to', 'retweet_date',
                         'translate', 'trans_src', 'trans_dest']
    text = text.remove_columns(columns_to_temove)
    text = text.select_tweets().remove_url().remove_punctuation().tokenize().remove_stopwords()
    
    st.write(text.generate_wordcloud(500, 500, 535, (16, 9)))

    st.write("")

    st.write("Checkout one random tweet from the collection you've just downloaded")

    st.write("")

    text.showrandomtweet()

    #st.text()

st.button("Re-run")




