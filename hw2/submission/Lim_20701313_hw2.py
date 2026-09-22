import math as m

import numpy as np


# rotation matrix on x axis
def Rx(theta):
    return np.matrix([[1, 0, 0], [0, m.cos(theta), -m.sin(theta)], [0, m.sin(theta), m.cos(theta)]])


# rotation matrix on y axis
def Ry(theta):
    return np.matrix([[m.cos(theta), 0, m.sin(theta)], [0, 1, 0], [-m.sin(theta), 0, m.cos(theta)]])


# rotation matrix on z axis
def Rz(theta):
    return np.matrix([[m.cos(theta), -m.sin(theta), 0], [m.sin(theta), m.cos(theta), 0], [0, 0, 1]])


# please give the values of the three angles
phi = m.pi / 2
theta = m.pi / 4
psi = m.pi / 2
print("phi =", phi)
print("theta  =", theta)
print("psi =", psi)


# given the vector v1 =(1,2,3), calculate the vector v2 after the XYZ rotation.
# X first, then Y, then Z: the matrix applied last stands leftmost.
v1 = np.array([[1], [2], [3]])
v2 = Rz(psi) * Ry(theta) * Rx(phi) * v1
print("The vector v2 is", np.round(v2, decimals=2))

# given the vector v1 =(1,2,3), calculate the vector v3 after the YZX rotation.
v3 = Rx(phi) * Rz(psi) * Ry(theta) * v1
print("The vector v3 is", np.round(v3, decimals=2))
