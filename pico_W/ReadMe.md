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

`"COILS", "HREGS", "ISTS", and "IREGS" are four types of registers commonly used in industrial control systems.`

    "COILS" (also known as "digital output coils") represent binary outputs that can be turned on or off.
    These can be used to control devices such as lights, motors, or solenoids.

    "HREGS" (also known as "holding registers") are used to store data values that can be read from and written to by a controller.
    These registers can be used to store parameters or settings for a device, or to track system performance.

    "ISTS" (also known as "digital input status") represent binary inputs that can be read by a controller to determine whether a particular device or sensor is on or off.
    Examples of digital inputs include limit switches, photoelectric sensors, or push buttons.

    "IREGS" (also known as "input registers") are used to store data values that can be read by a controller, but cannot be written to directly. 
    These registers can be used to store data from sensors or other external devices.
