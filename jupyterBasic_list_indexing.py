- 인덱싱, 슬라이싱
    
    arr1 = np.array([2,3,5,7,11, 13, 17, 19, 23,29, 31])
    array2[0]
    array2[-1]
    
    2
    
    31
    
    
    arr1 = np.array([2,3,5,7,11, 13, 17, 19, 23,29, 31])
    print(arr1[0])
    print(arr1[2])
    arr2 = np.array([2,1,3])
    arr1[arr2]
    
    2
    5
    
    Out[26]: array([5, 3, 7])
    
    
    
    In [27]: arr1[2:7]
    
    Out[27]: array([ 5,  7, 11, 13, 17])
    
    
    ### 2번 인덱스부터 10번까지 2,4,6,8,10
    
    In [28]: `arr1[2:11:2]`
    
    Out[28]: `array([ 5, 11, 17, 23, 31])`