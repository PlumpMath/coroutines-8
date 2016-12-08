from co_routine_decorator import coroutine


@coroutine
def grep(pattern):
    print("Looking for ", pattern)
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away.  Goodbye")

# coroutines will sort of hang around until you close them and when you do,
# an exception will be rised inside the co-routine.

g = grep("python")
g.send("I love me some python")
g.close()
