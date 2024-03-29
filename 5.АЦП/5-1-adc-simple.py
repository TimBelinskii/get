import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    for v in range(256):
        GPIO.output(dac, decimal2binary(v))
        time.sleep(0.0007)
        comp_v = GPIO.input(comp)
        if comp_v == 0:
            return v


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        value = adc()
        voltage = round(value / 256 * 3.3, 2)
        print(f"Цифровое значение: {value}, значение напряжения: {voltage}")

finally:
    GPIO.output(dac + [troyka], 0)
    GPIO.cleanup()
