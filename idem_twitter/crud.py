#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

from idem_twitter.models import Tweet, TweetCreate

def tweet_create(tweet: TweetCreate):
    # Modele de données avec validation
    print(tweet)
    # Conversion en modèle de base de données (sans validation)
    tw = Tweet.from_orm(tweet)
    print(tw)
    tw.save()
    return tw

def tweet_get(id: int = None):
    if id:
        return Tweet().find(id)
    return Tweet().all()


def tweet_delete(id: int):
    tweet = Tweet.find(id)
    tweet.delete()