from co_routine_decorator import coroutine
import grep
import printer


@coroutine
def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


if __name__ == "__main__":
    f = open("access-log")
    follow(f, broadcast([grep("python", printer()),
                        grep("ply", printer())]))

    # Or you can have all grep statements printout to the same printer
    p = printer()
    follow(f, broadcast([grep("python", p),
                        grep("ply", p)]))
