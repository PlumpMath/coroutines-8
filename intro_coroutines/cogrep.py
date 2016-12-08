from co_routine_decorator import coroutine
import time


# Coroutines can also be used for filtering (bcs a coroutine can both send and
# receive)
def follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thiefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


# A filter!
@coroutine
def grep(pattern):
    while True:
        line = yield
        if pattern in line:
            target.send(line)



if __name__ == "__main__":
    f = open("access-log")
    follow(f, grep("python", printer()))
