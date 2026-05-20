import numpy as np

import matplotlib.pyplot as plt

# Example Data: r, theta, h
# Example: radius varies with height
xn = []
yn = []
zn = []
z1 = np.linspace(0, 1, 10)
theta = np.linspace(0, 2 * np.pi - 0.01, 10)
r1 = np.random.rand(10, 10) * 3
R = 8
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
# vertical
for jk in range(10):
    xd = np.cos(theta[jk])
    yd = np.sin(theta[jk])
    x = np.ones(10)
    y = np.ones(10)
    for ik in range(10):

        x[ik] = (R - r1[ik, jk]) * xd
        y[ik] = (R - r1[ik, jk]) * yd
    ax.plot3D(x, y, z1, "r")
# horizontal
for jk in range(10):
    z = z1[jk] * np.ones(10)
    x = np.ones(10)
    y = np.ones(10)
    for ik in range(10):
        xd = np.cos(theta[ik])
        yd = np.sin(theta[ik])
        x[ik] = (R - r1[jk, ik]) * xd
        y[ik] = (R - r1[jk, ik]) * yd
    ax.plot3D(x, y, z, "b")
# 3. Visualization

plt.show()
