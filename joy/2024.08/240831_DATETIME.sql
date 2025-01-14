# DATE_FORMAT => 날짜 가공하는 방법 원하는 포맷으로 바꾸는 방법 
# LEFT(DATETIME, 10) => 왼쪽부터 자르는 방법도 있음 
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME, LEFT(DATETIME, 10) AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;