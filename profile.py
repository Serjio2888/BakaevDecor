from datetime import datetime
import inspect
from functools import wraps


def profile(elem, *args, **kwargs):
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
                a = elem.__dict__[fun]
                print('`%s` started' % (a.__qualname__))
                start_time = datetime.now()
                res = elem(*args, **kwargs)
                print('`%s` finished in %fs' % (a.__qualname__, (datetime.now() - start_time).total_seconds()))
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
