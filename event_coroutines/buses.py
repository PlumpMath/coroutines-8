from coroutine import *


@coroutine
def buses_to_dicts(target):
    while True:
        event, value = yield
        # Look for the start of a <bus> element
        if event == 'start' and value[0] == 'bus':
            busdict = {}
            fragments = []

            # Capture text of inner elements in a dict
            while True:
                event, value = yield
                if event == 'start':
                    fragments = []
                elif event == 'text':
                    fragments.append(value)
                elif event == 'end':
                    if value != 'bus':
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break


@coroutine
def filter_on_field(fieldname, value, target):
    while True:
        d = yield
        if d.get(fieldname) == value:
            target.send(d)
