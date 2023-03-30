#!/bin/bash

import sys

def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)

    if kargs: raise TypeError('extra keywards: %s' % kargs)

    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    file.write(output + end)
