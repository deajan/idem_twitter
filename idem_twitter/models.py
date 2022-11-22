#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


from typing import Optional
from sqlalchemy_mixins import ActiveRecordMixin
from sqlmodel import Field, SQLModel
from pydantic import constr


# In order for Mixins to work with sqlmodel, we need to patch SQLModel main.py at line 322 by adding a default None value for __config__
# config = getattr(base, "__config__", None)
# see https://github.com/tiangolo/sqlmodel/pull/256


class ActiveRecordBase(SQLModel, ActiveRecordMixin):
    __abstract__ = True
    pass


class User(ActiveRecordBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class TweetBase(ActiveRecordBase):
    text: constr(max_length=160)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Tweet(TweetBase, table=True):
    id: int = Field(default=None, primary_key=True)

class TweetCreate(TweetBase):
    pass


