import json
import logging
import os
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(json.dumps(event))
    sleeptime= int(os.environ.get("SLEEP","2")) 
    time.sleep(sleeptime)
    if (os.environ.get("BEHAVIOR") == "NG") :
        logger.error('failed function')
        raise Exception('failed!')
    else :
        return (event)