import logging
import tmodule

# create logger with 'spam_application'
logger = logging.getLogger("spam_application")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info("creating an instance of tmodule.Auxiliary")
a = tmodule.Auxiliary()
logger.info("created an instance of tmodule.Auxiliary")
logger.info("calling tmodule.Auxiliary.do_something")
a.do_something()
logger.info("finished tmodule.Auxiliary.do_something")
logger.info("calling tmodule.some_function()")
tmodule.some_function()
logger.info("done with tmodule.some_function()")
