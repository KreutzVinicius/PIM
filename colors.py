import cv2
import numpy as np

redLower = np.array([0.9*255,0,0])
redUpper = np.array([255,0.1*255,0.1*255])

greenLower = np.array([0, 0.9*255, 0])
greenUpper = np.array([0.1*255,255,0.1*255])

blueLower = np.array([0, 0, 0.9*255])
blueUpper = np.array([0.1*255, 0.1*255 , 255])

blackLower = np.array([0,0,0])
blackUpper = np.array([0.1*255,0.1*255,0.1*255], dtype=np.int32)

whiteLower = np.array([0.9*255,0.9*255,0.9*255], dtype=np.int32)
whiteUpper = np.array([255,255,255])


# Read the images
img = cv2.imread("black.png")
  
# Resizing the image
image = cv2.resize(img, (700, 600))
  
# Convert Image to Image HSV
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def detectColor(rgb,lower,upper,string):

# Defining mask for detecting color
    color = cv2.inRange(rgb, lower, upper)
    sum = 0
    for i in color:
        for j in i:
            sum = sum + j
    if (sum > 10000):
        print(string)


detectColor(rgb,blueLower, blueUpper, "azul")
detectColor(rgb, blackLower, blackUpper, "preto")
  
# Display Image and Mask
# cv2.imshow("Image", image)
# cv2.imshow("Mask", mask)
  
# Make python sleep for unlimited time
# cv2.waitKey(0)