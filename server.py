#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


import sys
import logging
import uvicorn

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    try:
        uvicorn.run("idem_twitter.api:app", workers=1, log_level="debug", reload=True, host='0.0.0.0', port=8080)
    except KeyboardInterrupt as exc:
        logger.error("Program interrupted by keyoard: {}".format(exc))
        sys.exit(200)
    except Exception as exc:
        logger.error("Program interrupted by error: {}".format(exc))
        logger.critical('Trace:', exc_info=True)
        sys.exit(201)