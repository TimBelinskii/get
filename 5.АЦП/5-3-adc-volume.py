import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def signal2leds(value):
    signal = [0] * 8
    n = int(8 * value / 256)
    signal[:n+1] = [1]*n
    GPIO.output(leds, signal)



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
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        value, signal = adc()
        signal2leds(value)
        voltage = round(value / 256 * 3.3, 2)
        print(f"Цифровое значение: {value} -> {signal}, значение напряжения: {voltage}")

finally:
    GPIO.output(dac + [troyka] + leds, GPIO.LOW)
    GPIO.cleanup()
