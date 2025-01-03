# 백준 2460번 지능형 기차2
max_v = 0
train_per = 0
for i in range(10):
    per1, per2 = map(int, input().split())
    max_v += per2 - per1
    train_per = max(train_per, max_v)
      
print(train_per)




     
    
