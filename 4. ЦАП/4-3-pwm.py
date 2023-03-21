import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def predictVoltage(value):
    return f'Предпологаемое напряжение на выходе ЦАП - {round(3.3 / 256 * value, 2)}'


def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


T = 10
freq = 1000
pin = 22
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, freq)

try:
    dc = 0
    p.start(dc)
    while True:
        dc = input()
        if isNumber(dc):
            if 0 < float(dc) < 100:
                p.ChangeDutyCycle(float(dc))
            else:
                print('Необходимо ввести число от 0 до 100')
        else:
            print('Необходимо ввести число, а не текст')

finally:
    p.stop()
    GPIO.cleanup()
