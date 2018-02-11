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

with open("bread.txt", "r") as f:
    data = f.read()

pat = re.compile(r"[A-Z][^\.!?]?*[\.!?]", data)
sentences = pat.findall(data)

while True:
    indx = np.random.randint(0, len(sentences))
    api.update_status(sentences[indx])
    time.sleep(37)
