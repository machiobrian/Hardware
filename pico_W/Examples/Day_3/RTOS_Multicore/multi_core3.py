# implement one with a synchronized coordination between threads : 
# we make use of a thread safe DS : 

"""
lock and queue : used when there are shared resources.
                 access/thread is controlled by locks
"""

import time 
import _thread
from machine import Pin

# define a shared variable and a lock
counter = 0
lock = _thread.allocate_lock() # creates a new lock object

# define thread 1
def thread_1():
    global counter # shared resource
    while True:
        # we aquire the lock and increment the counter
        with lock:
            counter += 1

        time.sleep(0.5) # increment the counter every 0.5 seconds

def thread_2():
    global counter
    while True:
        # acquire the lock and increment the counter
        with lock:
            counter -= 1
        time.sleep(1) # decrement the counter every 1 second

        # the 'lock' variable acquires and releases the lock.

# instantiate the two threads and start them
_thread.start_new_thread(thread_1, ()) # () return its identifier
_thread.start_new_thread(thread_2, ())


# keep the main thread running with a while loop
while True:
    with lock:
        print(counter)

    time.sleep(2) # prints the var every 2 seconds