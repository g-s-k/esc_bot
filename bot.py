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
        if err[0]["message"] == "Status is a duplicate.":
            pass
        else:
            raise
    time.sleep(37)
