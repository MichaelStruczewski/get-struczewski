import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

try:
    dc = pwm.PWM_DAC(12, 1000, 3.3, True)

    while True:
        try:

            fx=sg.get_sin_wave_amplitude(signal_frequency, time.time())
            dc.set_voltage(fx*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
        except ValueError:
            print("Это не число!\n")
        
finally:
    dc.deinit()
