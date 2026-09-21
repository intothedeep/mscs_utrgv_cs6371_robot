import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.image as mpimg
import pdb
# imshow: Function that handles both rgb and grayscale image and shows them accordingly.
# Parameters: 
#    img: input img
# Return: None

def imshow(img):
    if len(img.shape) < 3:
        plt.imshow(img, cmap="gray")
    elif img.shape[2] == 1:
        plt.imshow(np.resize(img,(img.shape[0],img.shape[1])), cmap="gray")
    else:
        plt.imshow(img)

# low pass filter
def lowPassFilter(lpfw, lpfh):
    print("Please create a (lpfw x lpfh) Low Pass Filter matrix")
    
    #******** please add your code here ************
    #lowPass = 
    
    print(lowPass)
    return lowPass

# it applies the filter on the image and generates a new image
# input: image, filter
# output: out
def conv(image, filter):
    iw,ih = image.shape
    fw,fh = filter.shape    
    out = np.zeros((iw-fw+1,ih-fh+1)) #it does not include the pixel on the boundary
    
    # please select fw x fh sub images in the image. Then, apply the filter on the sub images.
    
    #******** please add your code here ************
    
    # Return the resulting image "out"
    return out

img = mpimg.imread("original.jpg")
imshow(img)
plt.show()
print(img.shape)


fig = plt.figure(1, figsize=(18, 16))
print(" ================ Low Pass Filter ===================")

for i in range(3,8,2):
    # subplot the figure in 1x3
    splot = plt.subplot(1, 3, (i-1)//2)
    splot.set_xlabel(str(i)+"x"+str(i))
    
    # use different box size to filter the image
    (lpfw,lpfh) = (i,i)
    low_image = conv(img, lowPassFilter(lpfw, lpfh))
    imshow(low_image)
    cv2.imwrite("low"+str(i)+"x"+str(i)+".jpg",low_image)    
plt.show()

