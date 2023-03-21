import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def predictVoltage(value):
    return f'Предпологаемое напряжение на выходе ЦАП - {round(3.3/256 * value, 2)}'


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        for i in range(256):
            bits = decimal2binary(i)
            GPIO.output(dac, bits)
            time.sleep(0.2)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
