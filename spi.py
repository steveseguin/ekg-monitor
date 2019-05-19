import Adafruit_GPIO.FT232H as FT232H
import Adafruit_GPIO as GPIO
import time
import binascii

######################
WAKEUP = 0x02
STANDBY = 0x04
RESET = 0x06
START = 0x08
STOP = 0x0a

RDATAC = 0x10
SDATAC = 0x11
RDATA = 0x12

# register commands
RREG = 0x20
WREG = 0x40
ID =  0x00
#######################

# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()
# Find the first FT232H device.
ft232h = FT232H.FT232H()
spi = FT232H.SPI(ft232h, cs=8, max_speed_hz=300000, mode=1, bitorder=FT232H.MSBFIRST)
############################

## PIN SETUP
## PIN 8 = CS OUTPUT
ft232h.setup(8, GPIO.OUT)  # CS OUTPUT
ft232h.setup(9, GPIO.OUT)  # START OUTPUT
ft232h.setup(10, GPIO.IN)  # DRDY INPUT
ft232h.setup(11, GPIO.OUT)  # RESET
ft232h.setup(12, GPIO.OUT)  # CLKSEL OUTPUT
ft232h.setup(13, GPIO.OUT)  # SCLK OUTPUT

ft232h.output(8, GPIO.HIGH)
ft232h.output(9, GPIO.LOW)
ft232h.output(11, GPIO.LOW)
ft232h.output(12, GPIO.LOW) # ?
ft232h.output(13, GPIO.LOW) # ?

# Create a SPI interface from the FT232H using pin 8 (C0) as chip select.
# Use a clock speed of 3mhz, SPI mode 0, and most significant bit first.
time.sleep(1)


spi.write([SDATAC])
time.sleep(0.01)

gIDval = spi.transfer([ID])

print format(gIDval),gIDval
#print "start"
#time.sleep(0.01)
#spi.write([0x08])
#time.sleep(0.01)
#while True:
#	level = ft232h.input(10)
#	if level == GPIO.HIGH:
#	response = spi.read(8*24)
#		print response[0]
#	print 'Received {0}'.format(response)
#	else:
#		print "LOWWWWWWW"
	#spi.write([0x01, 0x02, 0x03])