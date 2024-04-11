import numpy as np
import matplotlib.pyplot as plt
random_numbers = np.random.normal(1146, 100, 365)


plt.figure(figsize=(10,6))
plt.plot(random_numbers)
plt.show()

actual_mean = np.mean(random_numbers)
print(random_numbers)
print("Фактическое среднее значение:", actual_mean)