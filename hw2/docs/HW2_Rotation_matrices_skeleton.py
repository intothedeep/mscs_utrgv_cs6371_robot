import numpy as np
import math as m
  
# rotation matrix on x axis
def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
  
# rotation matrix on y axis
def Ry(theta):
  # please write your code here.
  

# rotation matrix on z axis
def Rz(theta):
  # please write your code here.


# please give the values of the three angles
phi =
theta = 
psi = 
print("phi =", phi)
print("theta  =", theta)
print("psi =", psi)
  
  
# given the vector v1 =(1,2,3), calculate the vector v2 after the XYZ rotation.
v1 = np.array([[1],[2],[3]])
v2 =  
print("The vector v2 is", np.round(v2, decimals=2))

# given the vector v1 =(1,2,3), calculate the vector v3 after the YZX rotation.
v3 = 
print("The vector v3 is", np.round(v3, decimals=2))