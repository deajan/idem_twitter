#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
import logging
from idem_twitter.config import database_url, _DATABASE_DEBUG, _DATABASE_AUTOCOMMIT


engine = create_engine(database_url, echo=_DATABASE_DEBUG, pool_pre_ping=True)

logger = logging.getLogger()

def get_session():
    session = Session(engine, autocommit=_DATABASE_AUTOCOMMIT)
    return session


@contextmanager
def get_session_ctx():
    """
    Used for contextual usage:
    with get_session_ctx as session:
        do_work(session)
    """
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception as exc:
        logger.error("SQL Error: %s" % exc.__str__())
        logger.debug("Trace:", exc_info=True)
        session.rollback()
        logger.error("SQL Error: Rollback complete.")
        raise
    finally:
        session.close()


def init_db():  # WIP we need to run this on app start
    SQLModel.metadata.create_all(engine)