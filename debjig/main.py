from functools import wraps, partial
import logging


def wrapper(obj, f=None):
    if f is None: return partial(wrapper, obj)
    setattr(obj, f.__name__, f)
    return f


def log(level=logging.DEBUG, msg=None):
    def _middle(f):
        @wraps(f)
        def _inner(*args, **kwargs):
            logger.log(level, msg)
            f(*args, **kwargs)
        return _inner
        
        @wrapper
        def set_level(newlevel):
            nonlocal level
            level=newlevel

        @wrapper
        def set_msg(newmsg):
            nonlocal msg
            msg=newmsg
            
    return _middle
