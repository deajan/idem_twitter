#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


from typing import List
import logging
from fastapi import FastAPI, HTTPException
from fastapi_offline import FastAPIOffline
import idem_twitter.models as models
import idem_twitter.crud as crud
import idem_twitter.database as database

logger = logging.getLogger()

#### Create app
#app = FastAPI()
app = FastAPIOffline()  # Allows /docs to not use online CDN
database.init_db()
models.ActiveRecordBase.set_session(database.get_session())


@app.get("/")
async def root():
    return "Welcome to our mighty twitter v2. We have {} tweets currently.".format(len(crud.tweet_get()))


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

@app.post("/tweet", response_model=models.Tweet)
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