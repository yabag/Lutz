"""Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
Любительские инструменты для измерения времени выполнения вызово функции.
Определяет суммарное времяб лучшее время и лучшее суммарное время
"""

import time, sys

timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    Суммарное время выполнения функции func() reps раз
    Возвращает (суммарное время, последний результат)
    """

    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    Самая быстрая функция func() среди запусков.
    Возвращает (лучшее время, последний результат)
    """

    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of total:
    (best of reps1 runs of (total of reps2 runs of func))
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func))
    """

    return bestof(reps1, total, reps2, func, *pargs, **kargs)
