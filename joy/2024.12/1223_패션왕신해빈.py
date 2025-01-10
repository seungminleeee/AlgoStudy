# 흑흑 여기서 조합의 방법만 생각했는데 아니었다 단순 확률 문제였다 ;;; 
# 전체에서 - 여집합을 빼줌 

tc = int(input())
for i in range(tc):
    n = int(input())
    dict = {}
    for j in range(n):
        name, wear = input().split()
        if wear in dict:
            dict[wear] += 1
        else:
            dict[wear] = 1
    
    result = 1
    # hat, turban = 2 / sunglasses = 1 => hat, turban, 둘다 X = 3 / sunglasses, 선택X = 2 
    for cnt in dict.values(): 
        result *= (cnt + 1)

    print(result - 1) # headgear 도 선택 X / eyewear 도 선택 X 은 안되는거니까 안되는경우 빼줌 
    
    

