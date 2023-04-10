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
    (1, '\\usr\\bin\\python3'),
    (0, '\\usr\\bin\\python3'),
    (0, '\\usr\\bin\\python3')
]