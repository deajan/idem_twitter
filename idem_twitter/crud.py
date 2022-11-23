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
    tw.session.commit()
    return tw

def tweet_get(id_tweet: int = None):
    if id_tweet:
        return Tweet().find(id_tweet)
    return Tweet().all()


def tweet_delete(id_tweet: int):
    tw = Tweet.find(id_tweet)
    tw.delete()
    tw.session.commit()