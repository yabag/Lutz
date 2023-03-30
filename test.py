import sys
import time

import timer

try:
    timer = time.perf_counter()
except AttributeError:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

