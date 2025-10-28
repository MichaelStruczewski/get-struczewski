import time
import RPi.GPIO as GPIO
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.001, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def decimal2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def number_to_dac(self, number):
        signal = self.decimal2bin(number)
        GPIO.output(self.bits_gpio, signal)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def sequential_counting_adc(self):
        for value in range(256):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            compValue = GPIO.input(self.comp_gpio)
            if compValue > 0:
                return value
        return 255
            
    def get_sc_voltage(self):
        wth = self.sequential_counting_adc()
        voltage = wth / 255 * self.dynamic_range
        return voltage
    
if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.26)

        while True:
            strange = adc.get_sc_voltage()
            print(strange)

    finally:
        adc.deinit()