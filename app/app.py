import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from text.text import TextProcess
from scrape.ScrapeTwint import ScrapeTwint
from datetime import datetime, timedelta

d = datetime.today() - timedelta(hours=0, minutes=5)
horadia = d.strftime("%Y-%m-%d %H:%M:%S")

st.title('Word Cloud')

hash = st.text_input('Scrape Twitter for your target Hashtag! ;)')

ScrapeTwint.ScrapeHashtagTwint(hash, horadia)


if hash:
    df = pd.read_csv(hash + 'tweets.csv', sep='\t')

    tweet = df.drop(['id', 'conversation_id', 'created_at', 'date', 'time', 'timezone',
        'user_id', 'username', 'name', 'place',  'language', 'mentions',
        'urls', 'photos', 'replies_count', 'retweets_count', 'likes_count',
        'hashtags', 'cashtags', 'link', 'retweet', 'quote_url', 'video',
        'thumbnail', 'near', 'geo', 'source', 'user_rt_id', 'user_rt',
        'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src',
        'trans_dest'],axis=1)

    t = tweet['tweet']

    WC = TextProcess.remove_url(list(t))
    WC = TextProcess.tokenize_text(WC)
    WC = TextProcess.get_text_cloud(WC)

    word_cloud = WordCloud(max_font_size = 500, width = 500, height = 535)
    word_cloud.generate(WC)
    imagem = plt.figure(figsize = (16, 9))
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
    st.write(imagem)

st.button("Re-run")
#

