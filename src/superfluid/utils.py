def ensure_list(thing):
    if thing is None:
        return []
    elif isinstance(thing, (list, tuple)):
        return list(thing)
    return [thing]
