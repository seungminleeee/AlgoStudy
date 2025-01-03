# 피보나치 수5
n = int(input())
def fibo(n):
    arr = [0, 1] + [0] * (n-1)
    for i in range(2, n+1): #2번째 요소 부터 n까지 
        arr[i] = arr[i-1] + arr[i-2]
        
    return arr[n]

print(fibo(n))