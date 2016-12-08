# Remembering to call .next() is easy to forget
# Solved by wrapping coroutines with a decorator


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


# @coroutine
# def grep(pattern)
