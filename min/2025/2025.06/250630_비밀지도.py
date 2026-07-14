def solution(n, arr1, arr2):
    binarr1 = []
    binarr2 = []
    
    for a in arr1:
        nums = bin(a)[2:].zfill(n)
        binarr1.append(nums)
    
    for b in arr2:
        nums = bin(b)[2:].zfill(n)
        binarr2.append(nums)
    
    ans = []
    for i in range(n):
        st = ''
        for j in range(n):
            if binarr1[i][j] == '1' or binarr2[i][j] == '1':
                st += '#'
            else:
                st += ' '
        ans.append(st)
    
    return ans