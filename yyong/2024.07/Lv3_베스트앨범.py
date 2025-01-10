# 장르의 최댓값 배열 어떻게 하는지 고민됐는데 마침 영원이 면접때 문제가 생각나서 힙으로 관리했음!

from heapq import heappop, heappush, heapify


def solution(genres, plays):
    answer = []
    N = len(genres)
    
    genres_count = {}  # 총 재생 횟수
    genres_heap = {}   # 장르별 노래 재생 횟수 정렬
    
    for i in range(N):
        genre = genres[i]
        play_count = plays[i]
        
        if genre in genres_count:
            genres_count[genre] += play_count
        else:
            genres_count[genre] = play_count
        
        # 장르의 최댓값 최대힙으로 관리
        if genre in genres_heap:
            heappush(genres_heap[genre], (-play_count, i))
        else:
            genres_heap[genre] = [(-play_count, i)]
            heapify(genres_heap[genre])
            
    
    # 총 재생 정렬
    sorted_genres = sorted(genres_count.keys(), key=lambda x: genres_count[x], reverse=True)
    
    # 노래 뽑기
    for genre in sorted_genres:
        if genre in genres_heap:
            for _ in range(2):
                if genres_heap[genre]:
                    num, idx = heappop(genres_heap[genre])
                    answer.append(idx)
                else:
                    break
    
    return answer
