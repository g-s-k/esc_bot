#!/usr/bin/env python3

import json
import tweepy
import re
import time
import numpy as np

with open("keys.json", "r") as f:
    api_keys = json.load(f)

auth = tweepy.OAuthHandler(api_keys["consumer_key"], api_keys["consumer_secret"])
auth.set_access_token(api_keys["access_token"], api_keys["access_token_secret"])

api = tweepy.API(auth)

with open("tweets.txt", "r") as f:
    data = f.read()

words = re.findall(r"\w+", data)

while True:
    indx = np.random.randint(0, len(words), 12)
    tweet = " ".join([words[i] for i in indx])
    api.update_status(tweet)
    time.sleep(37)
