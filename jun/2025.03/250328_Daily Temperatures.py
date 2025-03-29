"""
[NCD] Daily Temperatures / Mid
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            if i == n:
                res.append(0)
                continue

            cnt = 0
            idx = i + 1
            while idx < n:
                if temperatures[idx] > temperatures[i]:
                    cnt += 1
                    break
                else:
                    cnt += 1
                    idx += 1

            if idx == n:
                cnt = 0
            res.append(cnt)

        return res