import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from text import textprocess
from scrape.ScrapeTwint import ScrapeHashtagTwint
from datetime import datetime, timedelta
import nltk as nltk
from nltk.probability import FreqDist

from transformers import pipeline

# from google_trans_new import google_translator

# needs to use this to generate synthatic classes
nltk.download("averaged_perceptron_tagger")


class WriteApp:
    def __init__(self, path):

        self._df = pd.read_csv(path + "tweets.csv")
        self.tweets = None

    def data(self):
        return self._df

    def tokenized_text(self):
        return self.tweets_tokenized

    def remove_columns(self, columns_remove):
        self._df = self._df.drop(columns_remove, axis=1)
        return self

    def select_tweets(self):
        self.tweets = self._df["tweet"]
        self.puretweets = self._df["tweet"]
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
        stopwords = list(pd.read_fwf("stopwords.txt", header=None)[0])
        self.tweets_tokenized = textprocess.remove_stopwords(
            text.tweets_tokenized, stopwords
        )
        return self

    def generate_wordcloud(
        self, max_font_size: int, width: int, height: int, figsize: tuple
    ):
        WC = textprocess.get_text_cloud(self.tweets_tokenized)
        word_cloud = WordCloud(max_font_size=max_font_size, width=width, height=height)
        word_cloud.generate(WC)
        imagem = plt.figure(figsize=figsize)
        plt.imshow(word_cloud)
        plt.axis("off")
        return imagem

    def showrandomtweet(self):
        example = np.random.choice(self.puretweets)
        st.write(example)
        return self

    def generate_wordcloud_lean(self):
        self.WC = textprocess.get_text_cloud(self.tweets_tokenized)
        self.wordlist = self.WC.split(" ")
        return self

    def get_synthatic_classes(self):

        self.classified = nltk.pos_tag([i for i in self.wordlist if i])
        words = np.transpose(self.classified)[0]
        classes = np.transpose(self.classified)[1]

        return self

    def filter_class(self, classified_lean_WordCloud, class_):
        filtered_wc = []
        for word_class in classified_lean_WordCloud:
            if word_class[1] == class_:
                filtered_wc += [word_class[0]]
        return filtered_wc

    def describe_classes(self, classified_lean_WordCloud):
        description_dictionary = {
            "CC": "coordinating conjunction",
            "CD": "cardinal digit",
            "DT": "determiner",
            "EX": "existential there",
            "FW": "foreign word",
            "IN": "preposition/subordinating conjunction",
            "JJ": "This NLTK POS Tag is an adjective (large)",
            "JJR": "adjective, comparative (larger)",
            "JJS": "adjective, superlative",
            "LS": "list market",
            "MD": "modal (could, will)",
            "NN": "noun, singular (cat, tree)",
            "NNS": "noun plural (desks)",
            "NNP": "proper noun, singular (sarah)",
            "NNPS": "proper noun, plural (indians or americans)",
            "PDT": "predeterminer (all, both, half)",
            "POS": "possessive ending (parent\ ‘s)",
            "PRP": "personal pronoun (hers, herself, him,himself)",
            "PRP$": "possessive pronoun (her, his, mine, my, our )",
            "RB": "adverb (occasionally, swiftly)",
            "RBR": "adverb, comparative (greater)",
            "RBS": "adverb, superlative (biggest)",
            "RP": "particle (about)",
            "TO": "infinite marker (to)",
            "UH": "interjection (goodbye)",
            "VB": "verb (ask)",
            "VBG": "verb gerund (judging)",
            "VBD": "verb past tense (pleaded)",
            "VBN": "verb past participle (reunified)",
            "VBP": "verb, present tense not 3rd person singular(wrap)",
            "VBZ": "verb, present tense with 3rd person singular (bases)",
            "WDT": "wh-determiner (that, what)",
            "WP": "wh- pronoun (who)",
            "WRB": "wh- adverb (how)",
        }

        from_word_to_description = {}
        for word_class in classified_lean_WordCloud:
            from_word_to_description[word_class[0]] = description_dictionary[
                word_class[1]
            ]
        return from_word_to_description

    def write_target_syntathic_structure(
        self, target_syntathic_structure=("NNP", "RB", "VB", "NN"), n_most_common=3
    ):
        """
        Example:

        target_syntathic_structure = ("NNP","RB","VB","NN")

        """
        final_sentence = ""

        classified_word_list = self.classified

        for syntathic_class in target_syntathic_structure:
            print(syntathic_class)
            target_sub_list = self.filter_class(classified_word_list, syntathic_class)
            freq_target = FreqDist(target_sub_list)
            print(freq_target)
            possible_words = np.transpose(freq_target.most_common(n_most_common))[0]
            word_choice = np.random.choice(possible_words)
            final_sentence += " " + word_choice

        return final_sentence

    def showrandomtweet(self):
        example = np.random.choice(self.puretweets)
        st.write(example)
        return self

    def translate_tweets(self):
        translator = google_translator()
        self.translations = translator.translate(self.tweets, lang_tgt="en")
        return self

    def analyze_tweets(self):
        classifier = pipeline("sentiment-analysis")
        # analysis_tot = [classifier(tweet)[0] for tweet in self.translations] # BYPASSING TRANSLATION GOOGLE_TRANS_NEW ISSUE
        analysis_tot = [classifier(tweet)[0] for tweet in self.tweets]
        labels = [analysis["label"] for analysis in analysis_tot]
        analysis_statistic = [
            labels.count("POSITIVE") / len(self.tweets),
            labels.count("NEGATIVE") / len(self.tweets),
        ]
        mean_score = np.mean([analysis["score"] for analysis in analysis_tot])
        return analysis_statistic, mean_score


lingua = st.sidebar.selectbox("", ["pt", "en"])

if lingua == "en":

    st.title("Tweetcraft")

    st.write("")

    st.header("An App by @sa_nahum and @RioJanu")

    st.write("")
    st.write("")

    st.write("Welcome to Tweetcraft!")

    st.write(
        "Enjoy a brief journey into the wonders of \
              Twitter scraping and processing"
    )

    st.write("")

    st.write(
        "First off, choose a word of your musing... \
    an ingredient to the magik spell"
    )

    hash = st.text_input("Scrape Twitter for your target word! ;)")

    st.write("")

    st.write(
        "Now, choose a time frame! Tweetcraft \
            dwells on fresh data, \
            so it will scrape twitter for the last \
            N minutes where N is yours \
            to input! remember a very large N \
            will make the process slower"
    )

    timelapse = st.number_input(
        "Twitter in the last N minutes!", value=5, max_value=30, min_value=1
    )

    d = datetime.now() - timedelta(minutes=timelapse)
    horadia = d.strftime("%Y-%m-%d %H:%M:%S")
    # horadia = d.strftime('%a %b %d %H:%M:%S %z %Y')

    if hash:
        ScrapeHashtagTwint(hash, horadia)
        text = WriteApp(hash)

        columns_to_remove = [
            "id",
            "conversation_id",
            "created_at",
            # "time",
            "timezone",
            "user_id",
            "username",
            "name",
            "place",
            "language",
            # "mentions",
            "urls",
            "photos",
            # "replies_count",
            # "retweets_count",
            # "likes_count",
            "date",
            "hashtags",
            "cashtags",
            "link",
            "retweet",
            "quote_url",
            "video",
            "thumbnail",
            "near",
            "geo",
            "source",
            "user_rt_id",
            "user_rt",
            "retweet_id",
            "reply_to",
            "retweet_date",
            "translate",
            "trans_src",
            "trans_dest",
        ]
        text = text.remove_columns(columns_to_remove)
        text = text.select_tweets().remove_url().remove_punctuation()
        text = text.tokenize().remove_stopwords()

        st.write(text.generate_wordcloud(500, 500, 535, (16, 9)))

        st.write("")

        with st.expander(
            "Checkout one random tweet from the collection \
                  you've just downloaded"
        ):
            st.write("")
            text.showrandomtweet()

        st.write("")

        # text.translate_tweets()

        stat, mean_score = text.analyze_tweets()

        with st.expander("a quick dive into the Sentiment within our tweet set!"):
            st.write("How much Positivity we found around this word?")
            st.progress(stat[0])
            st.write("What is the confidence score of this analysis")
            st.progress(stat[1])

        st.write("")
        st.write("")

        with st.expander("What does the HiveMind tell us?"):

            text = text.select_tweets().remove_url().remove_punctuation()

            text = text.tokenize().remove_stopwords()

            text = text.generate_wordcloud_lean()

            text = text.get_synthatic_classes()

            prophecy = text.write_target_syntathic_structure()

            st.write(prophecy)

        st.write("")
        st.write("")

elif lingua == "pt":

    st.title("Tweetcraft")

    st.write("")

    st.header("Um App de @sa_nahum e @RioJanu")

    st.write("")
    st.write("")

    st.write("Benvindo ao Tweetcraft!")

    st.write(
        "Curta uma breve jornada pelas maravilhas \
            da extração e processamento de dados do Twitter"
    )

    st.write("")

    st.write(
        "Primeiramente, escolha uma palavra do seu interesse... \
    um ingrediente para o feitiço"
    )

    hash = st.text_input("Busque o Twitter pela sua palavra alvo! ;)")

    st.write("")

    st.write(
        "Agora escolha uma janela temporal! Tweetcraft \
            trabalha com dados frescos quentinhos do forno, \
            então ele buscará o Twitter \
            nos N últimos minutos onde N é sua \
            escolha! lembre-se que um N muito grande \
            deixa o processo mais lento"
    )

    timelapse = st.number_input(
        "Twitter nos últimos N minutos!", value=5, max_value=30, min_value=1
    )

    d = datetime.today() - timedelta(minutes=timelapse)
    horadia = d.strftime("%Y-%m-%d %H:%M:%S")
    # horadia = d.strftime('%a %b %d %H:%M:%S %z %Y')

    if hash:
        ScrapeHashtagTwint(hash, horadia)
        text = WriteApp(hash)
        columns_to_remove = [
            "id",
            "conversation_id",
            "created_at",
            # "time",
            "timezone",
            "user_id",
            "username",
            "name",
            "place",
            "language",
            # "mentions",
            "urls",
            "photos",
            # "replies_count",
            # "retweets_count",
            # "likes_count",
            "date",
            "hashtags",
            "cashtags",
            "link",
            "retweet",
            "quote_url",
            "video",
            "thumbnail",
            "near",
            "geo",
            "source",
            "user_rt_id",
            "user_rt",
            "retweet_id",
            "reply_to",
            "retweet_date",
            "translate",
            "trans_src",
            "trans_dest",
        ]
        text = text.remove_columns(columns_to_remove)
        text = text.select_tweets().remove_url().remove_punctuation()
        text = text.tokenize().remove_stopwords()

        st.write(text.generate_wordcloud(500, 500, 535, (16, 9)))

        st.write("")

        with st.expander("Dá uma olhada em um tweet aleatório do conjunto baixado"):
            st.write("")
            text.showrandomtweet()

        st.write("")

        # text.translate_tweets()

        stat, mean_score = text.analyze_tweets()

        with st.expander(
            "Um breve mergulho no Sentimento presente no nosso conjunto de tweets!"
        ):
            st.write("Quanta Positividade encontramos ao redor do termo alvo?")
            st.progress(stat[0])
            st.write("Qual é a confiabilidade dessa análise?")
            st.progress(stat[1])

        st.write("")
        st.write("")

        with st.expander("O que nos diz a Mente Geral?"):

            text = text.select_tweets().remove_url().remove_punctuation()

            text = text.tokenize().remove_stopwords()

            text = text.generate_wordcloud_lean()

            text = text.get_synthatic_classes()

            prophecy = text.write_target_syntathic_structure()

            st.write(prophecy)

        st.write("")
        st.write("")


st.button("Re-run")
