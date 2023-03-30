def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def mymap_2(func, *seqs):
    return (func(*args) for args in zip(*seqs))
