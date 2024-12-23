# 1차 .. 틀림 ㅜㅜ 
# 문자열 합치기 CONCAT(A,'@@') => A@@
# 소수점 반올림 ROUND (젭알 기억하자..)
SELECT ROUTE, 
CONCAT(ROUND(SUM(D_BETWEEN_DIST), 2),'km') AS TOTAL_DISTANCE, 
CONCAT(ROUND(AVG(D_BETWEEN_DIST), 3),'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE 
GROUP BY ROUTE
ORDER BY TOTAL_DISTANCE DESC;

# 정답코드 .. ORDER BY 에서는 별칭을 쓸 수 없기 때문에 SUM(D_BETWEEN_DIST) 이렇게 써줘야함 .. 
SELECT ROUTE, 
CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1),'km') AS TOTAL_DISTANCE, 
CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2),'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE 
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC;