# door 
code.py --> CircuitPython version, explicitly designed for rapid testing, prototyping, and readability. 

The Cal1 125kHZ cards use a unique method of encoding that took a lot of time to reverse engineer. I spent many hours trying to figure it out, on and off over several months. Eventually I decided to give up. In the interest of knowledge transfer, I began typing up a document detailing everything I learned. This is not that document. This is an attempt to explain in a considerably more precise and readable way.

Here is the 'decoding' scheme I discovered.
When the HID ProxPro 5352A reads a Cal1 card (using HID's proprietary formatting and other goodies), it will transmit an ASCII-encoded, hexadecimal string over serial [1].

This is what it looks like for my card: 000C654EEA25CE

The above string gives little information, however. To pull out the 6-digit, unique 'code' on the back of every ID card: you need to convert it to binary. My 6-digit 'code' is 488722. If you order a replacement Cal1 card, this will change. The other UID on your card will not. 

And so, the above string now becomes: 00000000000011000110010101001110111010100010010111001110. The might not seem like much. Converting '488722' to binary becomes 1110111010100010010, which can in fact be found as a subset of the string at positions [28:47]. This relationship has held up between several Cal1 cards that have been tested, and so it's unlikely to be a fluke. 


pseudocode
----------------
- sleep until input is received (poll every 0.1s or so)
- convert hex string to binary
- slice binary from positions 28 to 47
- convert binary substring to decimal
- check if decimal sequence is valid/OK




[1] You can use either RS232, RS422, or RS485, depending on your model. Wire D+ and D- to the respective RX/TX pins on your MCU.


# Maintenance Notes
---------------------------
General
-- This program was written using CircuitPython, Adafruit's version of MicroPython. 

-- The HID ProxPro5352A reader can take in between 12-28VDC (max). I highly recommend using a 24VDC *linear* power supply. 


Storage
--> Please, please do not use a microSD card to store any critical data. 
