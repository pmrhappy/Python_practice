import logging
from logging import config
from logging.handlers import TimedRotatingFileHandler
import logging.handlers
import time
import os, sys
from _datetime import date


def createLogger(logger_name):
    #logging.basicConfig()
    #today = date.today().__str__()
    path = os.path.dirname(__name__)
    path = os.path.join(path, "config.ini")
    logging.config.fileConfig(path)
    logger = logging.getLogger(logger_name)
    '''while 1:
        logger.info("hello\n")
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(1)'''
        
    return logger

#createLogger("test1")



    
    
    
    
