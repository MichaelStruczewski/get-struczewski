import r2r_dac as r2r
import signal_generator as sg
import time
amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

try:
    dc = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)

    while True:
        try:

            fx=sg.get_triangle_wave_amplitude(signal_frequency, time.time())
            dc.set_voltage(fx*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
        except ValueError:
            print("Это не число!\n")

finally:
    dc.deinit()