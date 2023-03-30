def sumtree(l):
    tot = 0
    for x in l:

        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)

    return tot


def sumtree_2(l):
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)

    return tot


def sumtree_3(l):
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front

    return tot


l = [1, [2, [3, [4, [5]]]]]
print(sumtree_3(l))
