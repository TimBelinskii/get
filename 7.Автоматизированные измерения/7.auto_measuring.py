import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    signal = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        signal[i] = 1
        GPIO.output(dac, signal)
        time.sleep(0.0007)
        comp_v = GPIO.input(comp)
        signal[i] = comp_v
    v = 0
    for i in range(7):
        v += signal[i] * 2 ** (7 - i)
    return v, signal


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
leds = leds[::-1]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

v = []

try:
    t0 = time.time()
    GPIO.output(troyka, GPIO.HIGH)
    while voltage <= 0.97 * 3.3:
        value, signal = adc()
        GPIO.output(leds, signal)
        voltage = round(value / 256 * 3.3, 2)
        v.append(voltage)
        # print(f"Цифровое значение: {signal} -> {value}, значение напряжения: {voltage}")
    GPIO.output(troyka, GPIO.LOW)
    while voltage >= 0.02 * 3.3:
        value, signal = adc()
        GPIO.output(leds, signal)
        voltage = round(value / 256 * 3.3, 2)
        v.append(voltage)
        # print(f"Цифровое значение: {signal} -> {value}, значение напряжения: {voltage}")
    t1 = time.time()
    dt = t1 - t0
    with open('data.txt', 'w') as f:
        for value in v:
            f.write(value)
finally:
    GPIO.output(dac + [troyka] + leds, GPIO.LOW)
    GPIO.cleanup()
