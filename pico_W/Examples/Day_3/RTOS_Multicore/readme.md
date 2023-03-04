~~~~
The GIL is not enabled so both core0 and core1 can run Python code concurrently, with care to use locks for shared data.

pg. 15: Multicore Support : Rasppberry Pi Pico Python SDK
~~~~

After trying a couple of times to install `micropython-rtos` and failing....
The above statement made sense.

For shared data, as seen in file `multi_core3.py`, a lock was initiated for the shared variable `counter`