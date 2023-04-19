"""
pybench_cases.py: запускает pybench на наборе версий Python и операторов.
Выбирайте режимы путем редактирования этого сценария либо использования
аргументов командной строки (в sys.argv): например, запускайте
C:\python27\python pybench_cases.py, чтобы протестировать только одну
версию Pyhton из перечисленных в stmts, pybench_cases.py -a
для тестирования всех версий Python и py -3 pybench_cases.py -a -t
для трассировки командных строк.
"""
import pybench, sys
pythons = [
    (1, '/usr/bin/python3'),
    (0, '/usr/bin/python2.7'),
    (0, '/usr/bin/pypy')
]
pythons += [
    (1, '/usr/bin/python3'),
    (0, '/usr/bin/pypy')
]

stmts = [
    (0, 0, "[x ** 2 for x in range(1000)]"),
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),
    (0, 0, "list(x ** 2 for x in range(1000))"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'")
]
stmts += [
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
    (1, 1, "len(str(2 ** 1000000))")
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)
