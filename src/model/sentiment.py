import numpy as np
import json
from datetime import datetime
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

import re
from nltk.tokenize import WordPunctTokenizer

import google
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types\
    .Document(content=tweet,
              type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
    .analyze_sentiment(document=document)\
    .document_sentiment\
    .score
    return sentiment_score

def clean_tweet(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet)
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]',' ',link_removed)
    lower_case_tweet = number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()

    return clean_tweet

data_path = "../scrape/data/data_sentiment.npy"
dates_path = "../scrape/data/dates.json"
tweets_path = "../scrape/data/tweets.json"
np_path = "../scrape/data/data_sentiment.npy"


data = np.load(data_path)

with open(dates_path) as json_file:  
    dates = json.load(json_file)
    
with open(tweets_path) as json_file:  
    tweets = json.load(json_file)

tweets = tweets.split("], ")

'''
user_removed = re.sub(r'@[A-Za-z0-9]+','',tweets[359])
link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
number_removed = re.sub('[^a-zA-Z]',' ',link_removed)
lower_case_tweet = number_removed.lower()
tok = WordPunctTokenizer()
words = tok.tokenize(lower_case_tweet)
clean_tweet = (' '.join(words)).strip()
'''

#print(clean_tweet)

#print(get_sentiment_score(clean_tweet))


for i in range(2000):
    num = int(data[i, data.shape[1]-2])
    mean_score = 0

    if num == 0:
        data[i, data.shape[1]-2] = 1
    else:
        tweets_current = tweets[i].split("\", \"")
        nums = np.zeros(num)

        
        for j in range(num):
            tweet = tweets_current[j]
            try:
                nums[j] = get_sentiment_score(clean_tweet(tweet))
            except google.api_core.exceptions.InvalidArgument:
                print(clean_tweet(tweet))

        mean_score = np.mean(nums)
        score = 0

        if mean_score > -0.25:
            score = 1

        if mean_score > 0.25:
            score = 2

        data[i, data.shape[1]-2] = score

    if i % 100 == 0:
        np.save(np_path, data)
        print("iteration {}; score for this iteration is {}".format(i, mean_score))


np.save(np_path, data)
