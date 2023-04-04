try:
    while True:
        adc()

finally:
    GPIO.output(dac + [comp], 0)
    GPIO.cleanup()
