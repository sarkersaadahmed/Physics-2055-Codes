import numpy as np
import matplotlib.pyplot as plt

frequency = np.array([0.102, 0.132, 0.217, 0.355, 0.437, 0.558, 0.983, 1.254, 1.519, 1.718, 1.997, 2.319, 2.725, 4.53, 6.56, 8.52, 13.06, 18.99, 20.0])
voltage_high_pass = np.array([0.02837837838, 0.03181818182, 0.02636363636, 0.06100917431, 0.07546296296, 0.08611111111, 0.1375, 0.1796296296, 0.208372093, 0.2306976744, 0.2674418605, 0.3023255814, 0.3395348837, 0.4859813084, 0.6650943396, 0.7548076923, 0.8725490196, 0.93, 1.064935065])

plt.figure(figsize=(10, 6))
plt.plot(frequency, voltage_high_pass, label='High-pass Filter', marker='o')
plt.xlabel('Frequency [kHz]')
plt.ylabel('Voltage Output')
plt.title('Frequency vs. Voltage Output (High-pass Filter)')
plt.grid(True)
plt.legend()
plt.show()

gradient_high_pass = np.gradient(voltage_high_pass, frequency)

print("\nGradient values for High-pass Filter:")
for i, grad in enumerate(gradient_high_pass):
    print(f"At frequency {frequency[i]} kHz, the gradient is {grad:.4f} V/kHz")
