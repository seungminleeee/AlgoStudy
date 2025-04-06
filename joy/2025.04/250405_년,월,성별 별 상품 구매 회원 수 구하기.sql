SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH, I.GENDER AS GENDER, COUNT(DISTINCT O.USER_ID) AS USER
FROM ONLINE_SALE O
JOIN USER_INFO I
ON O.USER_ID = I.USER_ID
WHERE I.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;
