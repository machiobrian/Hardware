# the code does not use any synchronization mechanism : hence a difference in rate of execution 
# may be witnessed

import time
import _thread
from machine import Pin

# define two threads
def thread1():
    # blink the inbuilt LED
    led1 = Pin("LED", Pin.OUT)
    while True:
        led1.toggle()
        time.sleep(0.3)

def thread2():
    while True:
        print("Blinking inbuuilt LED")

# create the two threads and start them
_thread.start_new_thread(thread1, ()) # the syntax passes an empty tple as argument 
                                        # to each thread function.
# _thread.start_new_thread(thread2, ())

# keep the main thread running infinitely.
while True:
    pass
