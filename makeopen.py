import builtins


def makeopen(id):
    original = builtins.open

    def custom(*pargs, **kargs):
        print('Custom open call %r: ' % id, pargs, kargs)
        return original(*pargs, **kargs)

    builtins.open = custom


f = open('script2.py')
print(f.read())

makeopen('spam')
f = open('script2.py')
print(f.read())

makeopen('eggs')
f = open('script2.py')
print(f.read())
