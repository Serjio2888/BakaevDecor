from datetime import datetime
import inspect
from functools import wraps


def profile(elem):
    if inspect.isfunction(elem):
        @wraps(elem)
        def wrapped(*args, **kwargs):
            print('`%s` started' % (elem.__name__))
            start_time = datetime.now()
            res = elem(*args, **kwargs)
            print('`%s` finished in %fs' % (elem.__name__, (datetime.now() - start_time).total_seconds()))
            return res
        return wrapped
    else:
        for fun in elem.__dict__:
            if inspect.isfunction(elem.__dict__[fun]):
                setattr(elem, fun, profile(elem.__dict__[fun]))
        return elem
