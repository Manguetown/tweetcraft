import streamlit as st
import time
import numpy as np
import pandas as pd
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
        return self

    def remove_url(self):
        #if self.tweets == None:
        #    raise AttributeError("Tweets not defined")
        self.tweets = textprocess.remove_url(list(self.tweets))
        return self

    def tokenize(self):
        self.tweets_tokenized = textprocess.tokenize_text(self.tweets)
        return self
    
    def generate_wordcloud(self, max_font_size: int, width: int, height: int, figsize: tuple):
        WC = textprocess.get_text_cloud(self.tweets_tokenized)
        word_cloud = WordCloud(max_font_size = max_font_size, width = width, height = height)
        word_cloud.generate(WC)
        imagem = plt.figure(figsize = figsize)
        plt.imshow(word_cloud)
        plt.axis('off')
        return imagem


d = datetime.today() - timedelta(hours=0, minutes=5)
horadia = d.strftime("%Y-%m-%d %H:%M:%S")

st.title('Word Cloud')

hash = st.text_input('Scrape Twitter for your target Hashtag! ;)')

ScrapeHashtagTwint(hash, horadia)

if hash:
    text = WriteApp(hash)
    columns_to_temove = ['id', 'conversation_id', 'created_at', 'date', 'time', 'timezone',
                         'user_id', 'username', 'name', 'place',  'language', 'mentions',
                         'urls', 'photos', 'replies_count', 'retweets_count', 'likes_count',
                         'hashtags', 'cashtags', 'link', 'retweet', 'quote_url', 'video',
                         'thumbnail', 'near', 'geo', 'source', 'user_rt_id', 'user_rt',
                         'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src',
                         'trans_dest']
    text = text.remove_columns(columns_to_temove).select_tweets().remove_url().tokenize()

    st.write(text.generate_wordcloud(500, 500, 535, (16, 9)))

st.button("Re-run")
