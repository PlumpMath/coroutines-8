# You send data to coroutines
# You send data to threads (via queues)
# You send data to processes (via messages)
# Coroutines naturally tie into problems involving threads
# and distributed systems.


@coroutines
def threaded(target):
    messages = Queue()
    def run_target():
        while True:
            item = messages.get()
            if item is GeneratorExit:
                target.close()
                return
            else:
                target.send(item)
Thread(target=run_target).start()
try:
    while True:
        item = yield
        messages.put(item)
except GeneratorExit:
    messages.put(GeneratorExit)
