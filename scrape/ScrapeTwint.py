


import twint
import os

def ScrapeHashtagTwint(hashtag, datetime):
    os.system('twint -s '+ hashtag +' --since "' + datetime +'"  -o '+ hashtag +'tweets.csv --csv ')
    pass


