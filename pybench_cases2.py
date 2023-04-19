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
    (0, 0, "def f(x): return x\n[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x): return x\nres=[]\nfor x in 'spam' * 2500: res.append(f(x))"),
    (0, 0, "def f(x): return x\n$listif3(map(f, 'spam' * 2500))"),
    (0, 0, "def f(x): return x\nlist(f(x) for x in 'spam' * 2500)"),
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)
