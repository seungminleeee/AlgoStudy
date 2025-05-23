WITH RANK_TB AS (
    SELECT MEMBER_ID, RANK() OVER (ORDER BY COUNT(*) DESC) AS RK
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
)

SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW R
INNER JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
JOIN RANK_TB T ON R.MEMBER_ID = T.MEMBER_ID
WHERE T.RK = 1
ORDER BY REVIEW_DATE ASC, R.REVIEW_TEXT ASC