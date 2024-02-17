import RPi.GPIO as GPIO
import time

# Replace 'channel' with the GPIO pin number you connected the DO pin to
# VCC to 3.3 v Power
# GND to GND
# DO to physical pin 3 / BCM 2

channel = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel):
        print("No water detected")
    else:
        print("Water detected")
    time.sleep(1)

