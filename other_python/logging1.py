import logging

logger = logging.getLogger(__name__)    # __name__ is by convention, log will be module's name, if not set, root logger
logger.setLevel(logging.DEBUG)

formatter1 = logging.Formatter("%(levelname)s %(asctime)s - %(message)s")
formatter2 = logging.Formatter("%(message)s")   # can have different formats for different handler

file_handler1 = logging.FileHandler("c://temp/python/logging.txt")
file_handler1.setLevel(logging.ERROR)   # only ERROR will be written when message by
file_handler1.setFormatter(formatter1)  # logger.error('here is an error')
                                        # if you want trace logger.exception('here is the trace')

stream_handler1 = logging.StreamHandler()   # this puts debug msg to console only, not log file
stream_handler1.setFormatter(formatter1)

logger.addHandler(file_handler1)        # can have more than one handler
logger.addHandler(stream_handler1)

# these are replaced by the lines above
# LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
# logging.basicConfig(filename="c:\\temp\python\logging.txt",
#                     level=logging.DEBUG,
#                     format=LOG_FORMAT,
#                     filemode='w')  # overwrite existing file, default is append

#logger.debug("message {a}, {b}, {c}").format(a, b, c)

# a=0
# b=1
# c=2
# logger.error('here is an error')
# logger.debug("message {}, {}, {}".format(a, b, c))





