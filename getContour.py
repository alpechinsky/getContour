import numpy as np
import cv2 as cv

im = cv.imread('/Users/holigunz/my/univer/3course/nikitin/ProximalFemur.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 200, 255, 0)

#ret,thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im, contours, 2, (255,0,255), 2)
print(contours[2])
cv.imshow('im', im)

#cv.waitKey()
#cv.destroyAllWindows()

contour = contours[2]
f = open("contourBone.txt","w")
for id, point in enumerate(contour):
    if (id % 2 != 0):
        x = point[0][0]
        y = point[0][1]
        f.write(str(x) + " " + str(-y + 300) + " 0\n")
f.write(str(contour[1][0][0]) + " " + str(-contour[1][0][1] + 300) + " 0\n")
f.close()
