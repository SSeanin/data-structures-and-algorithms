from collections import defaultdict


def memoize(fn):
    cache = defaultdict(lambda: None)

    def go(*args):
        if cache[args] is not None:
            return cache[args]
        data = fn(*args)
        cache[args] = data
        return data

    return go
