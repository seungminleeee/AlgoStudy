"""
[PGS] 문자열 압축 / LV2
"""
def solution(s):
    n = len(s)
    result = n

    for i in range(1, n // 2 + 1):
        splited = []
        for j in range(0, n, i):
            splited.append(s[j:j + i])

        answer = ""
        cnt = 1
        for k in range(0, len(splited) - 1):
            cur, next = splited[k], splited[k + 1]

            if cur == next:
                cnt += 1
            else:
                if cnt == 1:
                    answer += cur
                else:
                    answer += f"{cnt}{cur}"
                cnt = 1

        if cnt == 1:
            answer += splited[-1]
        else:
            answer += f"{cnt}{splited[-1]}"

        result = min(len(answer), result)

    return result