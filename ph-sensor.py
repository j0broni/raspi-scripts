import time
import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

# Define sensor channels
# (channels 3 to 7 unused)
ph_channel = 0

# Define delay between readings (s)
delay = 1

while True:
    # Read the ph sensor data
    ph_level = readadc(ph_channel)
    print("PH Level: {}".format(ph_level))

    # Wait before repeating loop
    time.sleep(delay)
