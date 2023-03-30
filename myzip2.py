def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return (tuple(s[i] for s in seqs) for i in range(minlen))


def mymapPad(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in index]


s1, s2 = 'abc', 'xyz123'
print(list(myzip(s1, s2)))
print(mymapPad(s1, s2))
print(mymapPad(s1, s2, pad=99))
