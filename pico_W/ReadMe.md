### State Machines
Real-time responsiveness: Embedded systems often need to respond to events and inputs in real-time. State machines can help to ensure that the system responds quickly and efficiently to these events, which is essential in many embedded systems applications.

### Modbus RTU protocol and RS485

> Step 1;
~~~~
import upip
upip.install('micropython-brainelectronics-helpers')
~~~~
> How can we use raspberry pi pico as a Modbus Mater/Slave Device.

https://forum.micropython.org/viewtopic.php?t=5453

After the Project, Read this Doc.
> https://software.open-dev.ru/docs/online/micropython/library/umodbus.html

### RTU Slave Setup - Set_RTU_Client.py
> Setup to act as Client:

> Provide Modbus data via RTU to a host device. 

`The Modbus can provide modbus data via RTU to a host device. `

> The Slave Register setups are used as a `starting point` for configuring modbus slaves in systems (industrial automation systems)
