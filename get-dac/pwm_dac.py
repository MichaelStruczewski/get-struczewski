import RPi.GPIO as GPIO
import time
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_freq = pwm_freq
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)
        self.pwm.start(0)


    def deinit(self):
        if self.pwm:
            self.pwm.stop()
        GPIO.cleanup()

    def decimal2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
            print("Устанавливаем 0.0 В")
            voltage = 0
        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.3, True) 

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()
