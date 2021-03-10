import logging
from time import time  # To time our operations
from functools import wraps

logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt='%H:%M:%S', level=logging.INFO)


def timing(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        logging.info("%r(%r, %r) took %2.2f secs" % (function.__name__, args, kwargs, end - start))
        return result

    return wrap
