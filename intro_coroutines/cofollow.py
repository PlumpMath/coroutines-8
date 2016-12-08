from co_routine_decorator import coroutine
import time


# Source
def follow(the_file, target):
    the_file.seek(0, 2)
    while True:
        line = the_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)

    if __name__ = "__main__":
        f = open("access-log")
        follow(f, printer())
