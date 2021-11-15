# Cloyne-RFID-Controller

You know those nifty Cal1 cards? Well, I spent awhile reverse engineering them. Here's the 'decoding' scheme I discovered.

When the HID ProxPro 5352A reads a Cal1 card (using HID's proprietary formatting and other goodies), it will transmit an ASCII-encoded, hexadecimal string over serial [1].

This is what it looks like for my card: 000C654EEA25CE

The above string gives little information, however. To pull out the 6-digit, unique 'code' on the back of every ID card: you need to convert it to binary. My 6-digit 'code' is 488722. If you order a replacement Cal1 card, this will change. The other UID on your card will not. 

And so, the above string now becomes: 00000000000011000110010101001110111010100010010111001110. The might not seem like much. Converting '488722' to binary becomes 1110111010100010010, which can in fact be found as a subset of the string at positions [28:47]. This relationship has held up between several Cal1 cards that have been tested, although I'd be interested to see if it still holds up for the new cards introduced this year.

### TODO
1. Decide whether interpreted or compiled (i.e. CircuitPython vs Rust)
2. Add read/write to SPI flash (annoying w/ CircuitPython)
3. Add Bluetooth UART module
4. Implement LoRa to update (iv)
5. CRUD database for user management


pseudocode
----------------
- sleep until input is received (poll every 0.1s or so)
- convert hex string to binary
- slice binary from positions 28 to 47
- convert binary substring to decimal
- check if decimal sequence is valid/OK




[1] Wire D+ and D- to the respective RX/TX pins on your MCU. 


# Maintenance Notes
---------------------------
General
-- This program was written using CircuitPython, Adafruit's version of MicroPython. 

-- The HID ProxPro5352A reader can take in between 12-28VDC (max). I highly recommend using a 24VDC *linear* power supply. 


Storage
--> Please, please do not use a microSD card to store any critical data. 


# Links
-------
[1] HID 5352A Manual : https://www.hidglobal.com/system/files/doc_eol_expired_files/proxpro_serial_ins_en.pdf  

[2] Internet archive version of the link above : https://web.archive.org/web/20210725190958/https://www.hidglobal.com/system/files/doc_eol_expired_files/proxpro_serial_ins_en.pdf
