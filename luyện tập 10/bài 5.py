import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y1, color='blue')
axs[0].set_title('Đồ thị y = x^2')
axs[0].set_xlabel('Trục x')
axs[0].set_ylabel('Trục y')
axs[1].plot(x, y2, color='red')
axs[1].set_title('Đồ thị y = sqrt(x)')
axs[1].set_xlabel('Trục x')
axs[1].set_ylabel('Trục y')
plt.tight_layout()
plt.show()
