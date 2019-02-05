# Fennell, Matthew
# CPTR 454
# HW 4 Programming Problem

# Implement quickhull in the language of your choice.

# Preliminary Steps:
# 1) Ask the user for the number of points to be generated
# 2) Randomly generate the appropriate number of points in an array S
# 3) Sort the entries in S in a nondecreasing order by x-values

# Quickhull Steps
# 1) Determine the farthest "left" and farthest "right" points (xMin, xMax) (arbitrary)
# 2) Sort points as left or right of the line between xMin and xMax into S1 and S2
# 3) To construct the upper hull, find the point in S1 furthest from the line
# 4) Drop points inside the triangle formed
# 5) Repeat for the points left of pMax p1 and right of pMax pN
# 6) Concatenate all the max points, you've got a hull
# 7) Repeat for the lower hull


# Things to keep in mind:
# if q(x1,y1), q(x2,y2), and q(x3,y3) are 3 points, the area of the triangle is:
# 1/2(x1y2+x3y1+x2y3-x3y2-x2y1-x1y3) (positive if q3 is left of q1q2)
# Basically, if that's negative, a point is right, if positive, left.

import sys
import random

#print("This is the name of the script: ",sys.argv[0])
#print("Number of arguments: ",len(sys.argv))
#print("The arguments are: ",str(sys.argv))

if(len(sys.argv)==2):
    pointsNum = int(sys.argv[1])
else:
    print("Please input the number of points to be generated: ")
    pointsNum = int(input())

print(pointsNum, "points will be generated.")

S = []

for point in range(pointsNum):
    point = (random.randint(0,100),random.randint(0,100))
    S.append(point)

S.sort(key=lambda tup: tup[0])


# 1) Determine the farthest "left" and farthest "right" points
xMin = S[0]
xMax = S[len(S)-1]
print("Min: ",S[0])
print("Max: ",S[len(S)-1])

S.pop(0)
S.pop()

# 2) Sort points as left or right of the line from xMin to xMax
S1 = []
S2 = []

for point in S:
    triArea = (1/2)*((xMin[0]*xMax[1])+(point[0]*xMin[1])+(xMax[0]*point[1])-(point[0]*xMax[1])-(xMax[0]*xMin[1])-(xMin[0]*point[1]))
    if(triArea>0):
        S1.append(point)
    else:
        S2.append(point)



print("Left of Line")
for x in S1:
    print(x)

print("Right of Line")
for x in S2:
    print(x)
