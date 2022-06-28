# 불린연산
import numpy as np
array3 = np.array([2,3,5,7,11,13,17,19,23,29,31])
array3 > 4
array([False, False,  True,  True,  True,  True,  True,  True,  True,
        True,  True])
array3 % 2 == 0
array([ True, False, False, False, False, False, False, False, False,
       False, False])
booleans = np.array([True,True,True,True,False,True,True,False,True, False ])
booleans = np.array([True,True,True,True,False,True,True,False,True, False ])


# where
# True 인 인덱스만 뽑아준다.

np.where(booleans)
(array([0, 1, 2, 3, 5, 6, 8]),)
np.where(array3 > 4)
(array([ 2,  3,  4,  5,  6,  7,  8,  9, 10]),)
filter = np.where(array3 > 4)
filter
(array([ 2,  3,  4,  5,  6,  7,  8,  9, 10]),)
array3[filter]
array([ 5,  7, 11, 13, 17, 19, 23, 29, 31])


