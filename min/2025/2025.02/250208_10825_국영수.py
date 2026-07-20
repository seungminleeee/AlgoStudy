N = int(input())
student = [[0]*4 for _ in range(N)]

for i in range(N):
    name, k, e ,m = map(str, input().split())
    student[i] = [name, int(k), int(e), int(m)]

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(student[i][0])