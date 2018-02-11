#!/usr/bin/env python3

import sys
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

with open(sys.argv[1], "r") as f:
    data = f.read()

pat = re.compile(r"[A-Z][^\.!?]*?[\.!?]", re.M)
sentences = pat.findall(data)

while True:
    indx = np.random.randint(0, len(sentences) - 1)
    tweet = re.sub(r"<.*?>", "", sentences[indx])[:280]
    try:
        api.update_status(tweet)
    except tweepy.TweepError as err:
        print(err)
        if err.api_code == 187:
            print("Duplicate tweet attempted:")
            print(tweet)
        else:
            raise
    time.sleep(37)
