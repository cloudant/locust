import os
import time

def reltime():
    if os.name == 'nt':
        return int(time.time())
    else:
        return int(os.times()[4])

