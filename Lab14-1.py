import numpy as np
import matplotlib.pyplot as plt

# Визначаємо діапазон x
x = np.linspace(-3, 3, 400)
# Обчислюємо значення функції y
y = 2**x * np.sin(10 * x)

# Створюємо графік
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r'$Y(x)=2^x \cdot \sin(10x)$')

# Додаємо назву графіка
plt.title('Графік функції $Y(x)=2^x \cdot \sin(10x)$')

# Позначаємо осі
plt.xlabel('x')
plt.ylabel('Y(x)')

# Додаємо легенду
plt.legend()

# Виводимо графік на екран
plt.show()