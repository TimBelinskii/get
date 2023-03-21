import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def predictVoltage(value):
    return f'Предпологаемое напряжение на выходе ЦАП - {round(3.3 / 256 * value, 2)}'


T = 10
freq = 1000
pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, freq)

try:
    dc = 0
    while True:
        dc = input()
        if dc.isnumeric():
            if 0 < float(dc) < 100
                p.start(dc)
            else:
                print('Необходимо ввести число от 0 до 100')
        else:
            print('Необходимо ввести число, а не текст')

finally:
    GPIO.cleanup()
