# Copper: a highly maintainable RFID access control system.

You know those nifty Cal1 cards? Well, I spent awhile reverse engineering them. Here's the 'decoding' scheme I discovered. When the HID ProxPro 5352A reads a Cal1 card (using HID's proprietary formatting and other goodies), it will transmit an ASCII-encoded, hexadecimal string over serial [1]. This is what it looks like for my card: `000C654EEA25CE`. ![img1](/photos/hex-output.jpg)


The above string gives little information, however. To pull out the 6-digit, unique 'code' on the back of every ID card: you need to convert it to binary. My 6-digit 'code' is 488722. If you order a replacement Cal1 card, this will change. The other UID on your card will not. 


And so, the above string now becomes: *00000000000011000110010101001110111010100010010111001110*. The might not seem like much. Converting '488722' to binary becomes *1110111010100010010*, which can in fact be found as a subset of the string at positions *[28:47]*. This relationship has held up between several Cal1 cards that have been tested, although I'd be interested to see if it still holds up for the new cards introduced this year.

[![Watch the video](https://img.youtube.com/vi/ZLiSRAXvVas/maxresdefault.jpg)](https://youtu.be/dttw-bmGwjo)


## Cool Pics below
### Inside the door opener
![img2](/photos/inside-door-opener.jpg)

### Inside the card reader
![img3](/photos/inside-reader.jpg)
