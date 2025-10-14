import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

try:
    dc = mcp.MCP4725(5, 0x61, True)

    while True:
        try:

            fx=sg.get_triangle_wave_amplitude(signal_frequency, time.time())
            dc.set_voltage(fx*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
        except ValueError:
            print("Это не число!\n")
        
finally:
    dc.deinit()