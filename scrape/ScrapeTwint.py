


import twint
import os

class ScrapeTwint:

def __init__(self):
    pass

def InstallTwint(self):
    os.system('git clone --depth=1 https://github.com/twintproject/twint.git')
    os.system('cd twint')
    os.system('pip3 install . -r requirements.txt')
    pass

def ScrapeHashtagTwint(hashtag, datetime):
    os.system('twint -s '+ hashtag +' --since "' + datetime +'"  -o '+ hashtag +'tweets.csv --csv ')
    pass


