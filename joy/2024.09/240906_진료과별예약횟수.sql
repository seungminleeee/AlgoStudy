# ORDER BY 에서는 별칭 사용 가능한데 문자여도 그냥 써도 된다 ㅎ.. 새롭게 알게된사실! 
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드;