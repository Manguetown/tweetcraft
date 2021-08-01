import twint


def ScrapeHashtagTwint(hashtag, datetime):

    c = twint.Config()
    c.Search = hashtag
    c.Since = datetime
    c.Pandas = True
    c.Hide_output = True

    twint.run.Search(c)
    df = twint.storage.panda.Tweets_df
    df.to_csv(f"{hashtag}tweets.csv")
