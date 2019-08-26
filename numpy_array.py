import numpy as N

matrix = N.arange(1,101)

matrix.shape = (10, 10)

print matrix

print "Slice with all numbers end with 5: "
print matrix[:,4]

print "The sub-matrix is"
print matrix[3:6,4:8]

tempMatrix = matrix[3:6,4:8]

print "The vector form of sub-matrix is"

print tempMatrix.flatten(1)
