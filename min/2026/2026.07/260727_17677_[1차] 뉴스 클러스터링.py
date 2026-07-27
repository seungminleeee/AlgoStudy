def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    A = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2])
    
    B = []
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            A.append(str2[i:i+2])
    
    Bcopy = B.copy()
    I = []
    for a in A:
        if a in Bcopy:
            I.append(a)
            Bcopy.remove(b)
    
    U = A + B
    for i in I:
        U.remove(i)
    
    print(I, U)
#     answer = int((len(I) / len(U)) * 65536)
    
#     return answer