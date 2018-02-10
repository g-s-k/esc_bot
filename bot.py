#!/usr/bin/env python3

import json
import tweepy
import numpy
import matplotlib.pyplot as plt
import time

with open("keys.json") as f:
    api_keys = json.load(f)

auth = tweepy.OAuthHandler(api_keys["consumer_key"], api_keys["consumer_secret"])
auth.set_access_token(api_keys["access_token"], api_keys["access_token_secret"])

api = tweepy.API(auth)

while True:
    x, y = numpy.meshgrid(*([numpy.linspace(-1, 1, 25)] * 2))
    coeffs = numpy.random.rand(2, 2) - 0.5
    stuff = numpy.polynomial.polynomial.polyval2d(x, y, coeffs)
    plt.pcolormesh(stuff, cmap="plasma")
    # plt.show()
    plt.savefig("tmp.png")
    plt.cla()
    api.update_with_media("tmp.png")
    time.sleep(10)
