"""
[PGS] 귤 고르기 / LV2
"""
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    arr = sorted(counter.values(), reverse=True)

    count = 0
    kind = 0
    for gyul in arr:
        count += gyul
        kind += 1

        if count >= k:
            return kind