class WhenThen:
    
    def __init__(self, func):
        self._conditions = []
        self._func = func
        self.num = -1

    def __call__(self, *args, **kwargs):
        for condition in self._conditions:
            if condition['when'](*args, **kwargs):
                return condition['then'](*args, **kwargs)
        return self._func(*args, **kwargs)
    
    @property
    def get_conditions(self):
        return self._conditions
        
    def check_when_errors(self):
        if len(self._conditions) and self._conditions[self.num]['then'] is None:
            raise ValueError

    def check_then_errors(self):
        if not len(self._conditions) or self._conditions[self.num]['then'] is not None:
            raise ValueError

    def when(self, func):
        self.check_when_errors()
        self._conditions.append({'when': func, 'then': None})
        self.num += 1
        return self

    def then(self, func):
        self.check_then_errors()
        self._conditions[self.num]['then'] = func
        return self

#сама функция-декоратор
def whenthen(func):
    return WhenThen(func)
