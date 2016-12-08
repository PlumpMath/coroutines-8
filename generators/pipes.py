# One of the most pwerful applications of generators is
# setting up processing pipelines.

# input sequence -> generator -> generator -> for x in a

import tail


def grep(pattern, lines):
    for line in lines:
        if pattern in lines:
            yield line

logfile = open("access-log")
loglines = tail.follow(logfile)
pylines = grep("python", loglines)

for line in pylines:
    print(line)
