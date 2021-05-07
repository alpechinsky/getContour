import numpy as np
import cv2 as cv
import gmsh
import sys

im = cv.imread('/Users/holigunz/my/univer/3course/nikitin/ProximalFemur.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 200, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im, contours, 2, (255,0,255), 2)
print(contours[2])
cv.imshow('im', im)
#cv.waitKey()
#cv.destroyAllWindows()

contour = contours[2]
# f = open("contourBone.txt","w")
# for id, point in enumerate(contour):
#     if (id % 2 != 0):
#         x = point[0][0]
#         y = point[0][1]
#         f.write(str(x) + " " + str(-y + 300) + " 0\n")
# f.write(str(contour[1][0][0]) + " " + str(-contour[1][0][1] + 300) + " 0\n")
# f.close()
points = []

for id, element in enumerate(contour):
    if (id % 2 != 0):
        point = [element[0][0], -element[0][1] + 300, 0]
        points.append(point)


gmsh.initialize()
gmshPoints = []

for i in range(len(points)):
    gmshPoints.append(gmsh.model.geo.addPoint(
        points[i][0], points[i][1], points[i][2]))

lines = []

for i in range(len(gmshPoints)):
    if i < len(gmshPoints) - 1:
        lines.append(gmsh.model.geo.addLine(gmshPoints[i], gmshPoints[i + 1]))
    else:
        lines.append(gmsh.model.geo.addLine(gmshPoints[i], gmshPoints[0]))

cl = gmsh.model.geo.addCurveLoop(lines)
pl = gmsh.model.geo.addPlaneSurface([cl])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(2)

gmsh.write("testoutput.stl")

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
