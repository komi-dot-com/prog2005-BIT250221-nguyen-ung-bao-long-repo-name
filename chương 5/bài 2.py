import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = x**3

plt.plot(x, y1, color='blue', label='y = x^2')
plt.plot(x, y2, color='red', label='y = x^3')
plt.title('Đồ thị hàm số')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.legend()
plt.grid(True)
plt.show()
