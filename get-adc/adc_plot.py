import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10,6))
    plt.plot(time, voltage)
    plt.xlabel("Время")
    plt.ylabel("Напряжение")
    plt.grid(True, which = "major", linestyle = "-")
    plt.grid(True, which = "minor", linestyle = "--", linewidth = 0.5)
    plt.ylim(0, max_voltage)
    plt.minorticks_on()
    plt.show()
