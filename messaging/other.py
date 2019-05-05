from functools import wraps


def introduce(func):
    """
    A decorator that prints a line and the name of the object before it's method called
    Helps to analyse logs easily
    """
    @wraps(func)
    def introduce_before_call(*args, **kwargs):
        print('\n=====================================')
        self_str = str(args[0])
        print(f'{self_str}:')
        return func(*args, **kwargs)
    return introduce_before_call
