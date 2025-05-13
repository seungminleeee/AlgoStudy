"""
[BOJ] 시리얼 번호 / 실버3
"""
n = int(input())

serial_numbers = []
for _ in range(n):
    serial_numbers.append(input())

serial_numbers.sort(key=lambda x: (len(x), sum(int(num) for num in x if num.isdigit()), x))

for number in serial_numbers:
    print(number)