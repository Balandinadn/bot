import matplotlib.pyplot as plt
import numpy as np
x = [_ for _ in range(11)]
y1 = x.copy()
y2 = [i*2 for i in x]
y3 = [i*3 for i in x]
y4 = [i**2 for i in x]
y5 = [(i**2)*2 for i in x]
plt.xlabel('Ось х')
plt.ylabel('Ось у')
plt.plot(x, y1, color='orange', marker='*', markersize=7)
plt.plot(x, y2, color='blue', marker='*', markersize=7)
plt.plot(x, y3, color='green', marker='*', markersize=7)
plt.plot(x, y4, color='red', marker='*', markersize=7)
plt.plot(x, y5, color='purple', marker='*', markersize=7)
plt.show()
