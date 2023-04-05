from timer2 import total, bestof, bestoftotal

t = total(pow, 2, 1000)[0]
print(t)

t = total(pow, 2, 1000, _reps=1000)[0]
print(t)

t = total(pow, 2, 1000, _reps=1000000)[0]
print(t)

best = bestof(pow, 2, 100000)[0]
print(best)

best = bestof(pow, 2, 1000000, _reps=30)[0]
print(best)

bot = bestoftotal(str.upper, 'spam', _reps1=30, _reps=1000)
print(bot)

tib = bestof(total, str.upper, 'spam', _reps=30)
print(tib)


def spam(a, b, c, d): return a + b + c + d


t1 = total(spam, 1, 2, c=3, d=4, _reps=1000)
print(t1)

best = bestof(spam, 1, 2, c=3, d=4, _reps=1000)
print(best)

bot = bestoftotal(spam, 1, 2, c=3, d=4, _reps1=1000, _reps=1000)
print(bot)

bot2 = bestoftotal(spam, *(1, 2), _reps1=1000, _reps=1000, **dict(c=3, d=4))
print(bot2)