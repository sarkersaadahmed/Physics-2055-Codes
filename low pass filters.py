import numpy as np
import matplotlib.pyplot as plt

frequency = np.array([0.102, 0.132, 0.217, 0.355, 0.437, 0.558, 0.983, 1.254, 1.519, 1.718, 1.997, 2.319, 2.725, 4.53, 6.56, 8.52, 13.06, 18.99, 20.0])
voltage_low_pass = np.array([4.36, 4.32, 4.32, 4.32, 4.32, 4.32, 4.28, 4.28, 4.3, 4.3, 4.3, 4.3, 4.3, 3.6, 3.25, 2.8, 2.12, 1.68, 1.44])

plt.figure(figsize=(10, 6))
plt.plot(frequency, voltage_low_pass, label='Low-pass Filter', marker='o')
plt.xlabel('Frequency [kHz]')
plt.ylabel('Voltage Output')
plt.title('Frequency vs. Voltage Output (Low-pass Filter)')
plt.grid(True)
plt.legend()
plt.show()

gradient_low_pass = np.gradient(voltage_low_pass, frequency)

print("Gradient values for Low-pass Filter:")
for i, grad in enumerate(gradient_low_pass):
    print(f"At frequency {frequency[i]} kHz, the gradient is {grad:.4f} V/kHz")
