""" modified from a chapter 9 exercise in the Python Cookbook by David Beazly """

from functools import wraps, partial
from inspect import isclass
import logging
import sys

logging.basicConfig(stream=sys.stderr)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def wrapper(obj, f=None):
    if f is None: return partial(wrapper, obj)
    setattr(obj, f.__name__, f)
    return f


def log(level=logging.DEBUG, msg=None):
    def _middle(f):
        @wrapper(f)
        def set_level(newlevel):
            nonlocal level
            level=newlevel

        @wrapper(f)
        def set_msg(newmsg):
            nonlocal msg
            msg=newmsg

        @wraps(f)
        def _inner(*args, **kwargs):
            nonlocal msg
            if msg is None:
                msg = '.'.join(f.__qualname__.split('.')[-2:])
            logger.log(level, msg)
            return f(*args, **kwargs)

        return _inner
    return _middle


def logclass(cls):
    if isclass(cls):
        for nm in dir(cls):
            attr=getattr(cls, nm)
            try:
                if callable(attr) and not nm.startswith('_'): setattr(cls, nm, log()(attr))
            except TypeError:
                pass

    return cls
