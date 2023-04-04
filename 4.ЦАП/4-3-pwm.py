import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def predictVoltage(value):
    return f'Предпологаемое напряжение на выходе ЦАП - {round(3.3 / 100 * value, 2)}'


def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


T = 10
freq = 1000
pin = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup([pin, 8], GPIO.OUT)
p = GPIO.PWM(pin, freq)
p_led = GPIO.PWM(8, freq)

try:
    print('Введите значение коэффициента заполнения в пределах от 0 до 100')
    dc = 0
    p.start(dc)
    p_led.start(dc)
    while True:
        dc = input()
        if isNumber(dc):
            if 0 <= float(dc) <= 100:
                p.ChangeDutyCycle(float(dc))
                p_led.ChangeDutyCycle(float(dc))
                print(predictVoltage(float(dc)))
            else:
                print('Необходимо ввести число от 0 до 100')
        else:
            print('Необходимо ввести число, а не текст')

finally:
    p.stop()
    p_led.stop()
    GPIO.cleanup()
