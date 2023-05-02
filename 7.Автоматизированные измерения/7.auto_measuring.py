import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def makeGraph(values):
    n = range(len(values))
    plt.scatter(n, values)
    plt.savefig('graph.png')

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
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

v = []

try:
    t0 = time.time()
    voltage = 0
    GPIO.output(troyka, GPIO.LOW)
    # Зарядка конденсатора
    while voltage <= 0.97 * 3.3:
        value, signal = adc()
        GPIO.output(leds, signal)
        voltage = value / 256 * 3.3
        v.append(voltage)
        print(f"Цифровое значение: {signal} -> {value}, значение напряжения: {round(voltage, 2)}")

    GPIO.output(troyka, GPIO.HIGH)
    # Разрядка конденсатора
    while voltage >= 0.8:
        value, signal = adc()
        GPIO.output(leds, signal)
        voltage = round(value / 256 * 3.3, 2)
        v.append(voltage)
        print(f"Цифровое значение: {signal} -> {value}, значение напряжения: {voltage}")

    # Анализ полученных данных
    t1 = time.time()
    dt = round(t1 - t0, 2)
    f = round(len(v) / dt, 2)
    T = round(dt / len(v), 2)
    st = 0
    for i in range(1, len(v)):
        st += abs(v[i] - v[i - 1])

    st = round(st/(len(v) - 1), 2)

    # Вывод результатов
    with open('data.txt', 'w') as F:
        for value in v:
            F.write(str(value) + '\n')
    with open('settings.txt', 'w') as F:
        F.write(f'Средняя частота дискретизации: {f} Гц\n')
        F.write(f'Шаг квантования: {st} В')
    makeGraph(v)
    print(f'Общая продолжительность эксперимента: {dt} c')
    print(f'Период одного измерения: {T} c')
    print(f'Средняя частота дискретизации: {f} Гц')
    print(f'Шаг квантования: {st} В')
finally:
    GPIO.output(dac + [troyka] + leds, GPIO.LOW)
    GPIO.cleanup()
