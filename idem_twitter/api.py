#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

__appname__ = "super twitter 2.0"
__author__ = "Alan Smithee"
__build__ = "2022112201"
__version__ = "1.0-beta"

from typing import List
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi_offline import FastAPIOffline
import idem_twitter.models as models
import idem_twitter.crud as crud
from idem_twitter.misc import hcss_class
import idem_twitter.database as database

logger = logging.getLogger()

#### Create app
#app = FastAPI()        # standard FastAPI initialization
app = FastAPIOffline()  # Offline FastAPI initialization, allows /docs to not use online CDN
database.init_db()
models.ActiveRecordBase.set_session(database.get_session())


@app.get("/")
async def root():
    return {"tweets": len(crud.tweet_get())}


@app.get("/tweets", response_model=List[models.Tweet])
@app.get("/tweet/{id}", response_model=models.Tweet)
async def get_tweets(id: int = None):
    try:
        return crud.tweet_get(id)
    except Exception as exc:
            logger.debug("Cannot list tweets: {}".format(exc), exc_info=True)
            raise HTTPException(
                status_code=400,
                detail="Cannot list tweets: {}".format(exc),
            )

@app.post("/tweet", response_model=models.Tweet, status_code=201)
async def create_tweet(tweet: models.TweetCreate):
    try:
        return crud.tweet_create(tweet)
    except Exception as exc:
            logger.debug("Cannot create tweets: {}".format(exc), exc_info=True)
            raise HTTPException(
                status_code=400,
                detail="Cannot create tweets: {}".format(exc),
            )

@app.delete("/tweet/{id}")
async def delete_tweet(id: int):
    try:
        return crud.tweet_delete(id)
    except Exception as exc:
            logger.debug("Cannot delete tweet: {}".format(exc), exc_info=True)
            raise HTTPException(
                status_code=400,
                detail="Cannot delete tweet: {}".format(exc),
            )


@app.get("/front", response_class=HTMLResponse)
async def front():
    number_of_tweets = len(crud.tweet_get())
    css_class = 'bg-primary' if number_of_tweets else 'bg-warning'
    tweets = ""
    for index, tweet in enumerate(crud.tweet_get()):
        card_class = "bg-info" if index % 2 else "bg-secondary"
        tweets += '<div class="card {}"><div class="card-body"><div class="card-title">Tweet</div><div class="card-text">{}</div></div></div>'.format(card_class, tweet.text)
    return """
    {}
    <html>
        <head>
            <title>My Super twitter App v2</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
        <div class="container p-2">
        <img src="https://pixy.org/src/443/4434039.png" width="15%">
        <h1 class="bg-success p-4">Welcome to our mighty twitter v2.</h1>
        <h2 class="{} p-4">We have {} tweets currently.</h2>
        {}
        </div>
        </body>
    </html>
    """.format(hcss_class, css_class, number_of_tweets, tweets)