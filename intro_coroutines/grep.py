def grep(pattern):
    print("Looking for", pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)


g = grep("python")
next(g)
print(g.send("Hello there"))
print(g.send("Hello there python"))
