import time

import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    for v in range(256):
        signal = decimal2binary(v)
        GPIO.output(dac, signal)
        voltage = v / 256 * 3.3
        time.sleep(0.0007)
        comp_v = GPIO.input(comp)
        if comp_v == 0:
            print(f'Значение АЦП: {v} -> {signal}, поданное напряжение: {round(voltage, 2)}')


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        adc()

finally:
    GPIO.output(dac + [comp], 0)
    GPIO.cleanup()
