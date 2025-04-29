import matplotlib.pyplot as plt
import numpy as np

n_g = 5
t = 10
x_center = np.array([1,3,5,7,9])
y_center = np.array([2,4,1,6,3])

x_dev = 0.5
y_dev = 0.5

x_data=[]
y_data=[]
for i in range(n_g):
  x_g = x_center[i] + np.random.uniform(-x_dev, x_dev, t)
  y_g = y_center[i] + np.random.uniform(-y_dev, y_dev,t)
  x_data.append(x_g)
  y_data.append(y_g)

x_means = [np.mean(x) for x in x_data]
y_means = [np.mean(y) for y in y_data]
x_error = [np.max(np.abs(x - mean)) for x, mean in zip (x_data, x_means)]
y_error = [np.max(np.abs(y - mean)) for y, mean in zip (y_data, y_means)]

plt.figure(figsize=(10,6))
for i in range(n_g):
  plt.errorbar(x_means[i], y_means[i], xerr = x_error[i], yerr = y_error[i], fmt = '0', markersize = 8, capsize = 5, label=f'Group {i+1}')
for i in range(n_g):
  plt.scatter(x_data[i], y_data[i], s=20, alpha = 0.5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title()
plt.grid(True)
plt.legend()
plt.show()
