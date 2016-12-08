from co_routine_decorator import coroutine


@coroutine
def printer():
    while True:
        line = yield
        print(line)
