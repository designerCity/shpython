import numpy as np
array1 = numpy.array([2,3,5,7,11,13,17,19,23,29])
type(array1)
numpy.ndarray
array1.shape
(10,)
array2 = numpy.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
type(array2)
numpy.ndarray
array2.shape
(3, 4)
array2
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
array1.size
10
array2.size
12
arr1 = np.array([2,3,5,7,11, 13, 17, 19, 23,29, 31])
print(arr1[0])
print(arr1[2])
arr2 = np.array([2,1,3])
arr1[arr2]
2
5
array([5, 3, 7])
arr1[2:7]
array([ 5,  7, 11, 13, 17])
arr1[2:11:2]
array([ 5, 11, 17, 23, 31])
