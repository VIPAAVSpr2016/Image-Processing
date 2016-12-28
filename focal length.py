# import the necessary packages
import numpy as np
import cv2
 
 
def find_marker(image):
        # convert the image to grayscale, blur it, and detect edges
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)
 
        # find the contours in the edged image and keep the largest one;
        # we'll assume that this is our piece of paper in the image
        (_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        c = max(cnts, key = cv2.contourArea)
        
        cv2.drawContours(gray, cnts, -1, (0,255,0), 3)
        cv2.imshow("window title",gray)
        key = cv2.waitKey()
        if key == ord("q"):
                cv2.destroyAllWindows()
        
 
        # compute the bounding box of the of the paper region and return it
        return cv2.minAreaRect(c)
 
def distance_to_camera(knownWidth, focalLength, perWidth):
        # compute and return the distance from the maker to the camera
        return (knownWidth * focalLength) / perWidth
 
# initialize the known distance from the camera to the object, which
# in cm
KNOWN_DISTANCE = 45.0
 
# initialize the known object width, which in this case, the piece of
# width (in cm)
KNOWN_WIDTH = 27.9
 
# initialize the list of images that we'll be using
IMAGE_PATHS = ["image1.jpg","image2.jpg"]
 
# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread(IMAGE_PATHS[0])
marker = find_marker(image)
print marker
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
print focalLength

image = cv2.imread(IMAGE_PATHS[1])
marker = find_marker(image)
perWidth = marker[1][0]
distance1 = distance_to_camera(KNOWN_WIDTH, focalLength, perWidth)
print distance1, "(in cm)"
key = cv2.waitKey(1) & 0xFF
if key == ord("q"):
     
        cv2.destroyAllWindows()
       

