from datetime import datetime
import inspect
from functools import wraps


def profile_for_method(func, classname=None):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if classname:
            print('`%s` started' % (classname+'.'+func.__name__))
        else:
            print('`%s` started' % (func.__name__))
        start_time = datetime.now()
        res = func(*args, **kwargs)
        if classname:
            print('`%s` finished in %fs' % (classname+'.'+func.__name__, (datetime.now() - start_time).total_seconds()))
        else:
            print('`%s` finished in %fs' % (func.__name__, (datetime.now() - start_time).total_seconds()))
        return res

    return wrapped

def profile(elem, *args, **kwargs):
    if inspect.isfunction(elem):
        return profile_for_method(elem)
    else:
        classname = elem.__name__
        for key in elem.__dict__:
            if inspect.isfunction(elem.__dict__[key]):
                setattr(elem, key, profile_for_method(elem.__dict__[key], classname))
        return elem


class New:
    @profile
    def func(self):
        return True
    @profile
    def funcy(self):
        return True
    
@profile
class Old:
    def funny(self):
        return True
    def funni(self):
        return True

N = New()
N.func()
N.funcy()
Oo = Old()
Oo.funny()
Oo.funni()

