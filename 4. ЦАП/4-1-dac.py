import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    fl = -1
    while fl != 'a':
        fl = input()
        if fl.isdigit():
            if int(fl) != float(fl):
                print('Нужно ввести целое число от 0 до 255')
            elif int(fl) > 255 or int(fl) < 0
                print('Нужно ввести число от 0 до 255')
            else:
                bits = decimal2binary(int(fl))
                GPIO.output(dac, bits)
        else:
            print('Нужно ввести число от 0 до 255, а не текст')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
