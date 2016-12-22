import logging
import logging.handlers
import time


logging.basicConfig()

nor = logging.getLogger("nor")
nor.setLevel(logging.INFO)

filehandler = logging.handlers.TimedRotatingFileHandler(
        "logging_test2.log", 'S', 3, 0)

filehandler.suffix = "%Y%m%d-%H%M.log"
nor.addHandler(filehandler)

while 1:
    nor.info("hello\n")
    time.sleep(1)
    
    
    
    
