# In concurrent programming, one typically dubdivides problems into "tasks"

# Tasks have a few essential features:
# - Independent control flow
# - Internal state
# - Can be scheduled (suspended/resumend)
# - Can communicate with other tasks

# Claim: Coroutines are tasks
# Is it possible to do multi-tasking using nothing but coroutines
# (no threads, no subprocesses)?


# On a CPU, a program is a series of instructions.
# When running, there is no notion of doing more than one thing at a time
# (or any kind of task switching).

# The thing that knows about of multi-tasking is the operating system.
# It does this by rapidly switching between tasks

# When a CPU is running your program, it is not runningthe operating system
# Question: How does the operating system (which is not running) make
#  an application
# (which is running) switch to antoher task?
# The "context-switching" problem ...
# There are usually only two mechanisms that an OS uses to gain control:
# - Interrupts - Some kind of hardware related signal
# - Traps - A software generated signal
# In both cases, the CPU briefly suspends what it is doing, and runs code
# that's part of the OS.
# It is at this time the OS might switch tasks.

# Traps are what make an OS work
# The OS drops your program on the CPU
# It runs until it hits a trap (system call)
# The program suspends and the OS runs
# Reapeat (run-trap-run-trap)


# To run many taks, add a bunch of queues

# Ready queues
#  -----------------------------
# | task     task       task   |  --------------------- task        task
# ------------------------------                        cpu         cpu
#               |
#               |                                              |
#               |                                              |
#               |------ Wait Queues                            |
#                        ----------------                      |
#                       |task      task |<---------------------|
#                       ----------------                       |
#                                                              |
#                        ----------------                      |
#                       |task      task |<---------------------|
#                       ----------------


# The yield statement is kind of "trap

class Task(object):
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.sendval = None

    def run(self):
        return self.target.send(self.sendval)


class SystemCall(object):
    def handle(self):
        pass


class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self, task):
        self.ready.put(task)

    def exit(self, task):
        del self.taskmap[task.tid]

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

# Example run
if __name__ == "__main__":
    def foo():
        mytid = yield GetTid()
        for i in range(5):
            print("foo ", mytid)
            yield

    def bar():
        mytid = yield GetTid()
        for i in range(10):
            print("bar ", mytid)
            yield

    s = Scheduler()
    s.new(foo())
    s.new(foo())
    s.mainloop()
