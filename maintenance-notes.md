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
