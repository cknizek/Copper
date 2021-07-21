import board
import digitalio
import busio

relay = digitalio.DigitalInOut(board.D0)
relay.direction = digitalio.Direction.OUTPUT
uart = busio.UART(board.TX, board.RX, baudrate=9600)

arr = [488722]
# hexMap is a dict/map, keys are hex values, values are binary equivalent
hexMap = {
  '0' : '0000',
  '1' : '0001',
  '2' : '0010',
  '3' : '0011',
  '4' : '0100',
  '5' : '0101',
  '6' : '0110',
  '7' : '0111',
  '8' : '1000',
  '9' : '1001',
  'A' : '1010',
  'B' : '1011',
  'C' : '1100',
  'D' : '1101',
  'E' : '1110',
  'F' : '1111'
}

def toBin(hex):
  # input arg. 'hex' is ASCII-encoded hexadecimal string 
  binStr = ""
  for elem in hex:
    tmp = hexMap[elem]
    binStr += tmp
  return binStr


def isValid(hex):
  hex = toBin(hex)
  if int(a[28:47], 2) in arr:
    print("success! access granted :)")
    relay.value = True # pull high
    time.sleep(0.1) # value is arbitrary
    relay.value = False

while True:
  data = uart.read(14) # transponder will read 14 bytes ONLY, read HID ProxPro5352A documentation as to why...
  if data is not None:
    data_string = ''.join([chr(b) for b in data])
    isValid(data_string)
    print(data_string, end="")