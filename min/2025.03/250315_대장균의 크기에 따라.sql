WITH RATIO_DATA AS (
    SELECT ID, CUME_DIST() OVER(ORDER BY SIZE_OF_COLONY DESC) RATIO
    FROM ECOLI_DATA
)

SELECT ID,
    CASE 
        WHEN RATIO <= 0.25 THEN 'CRITICAL'
        WHEN RATIO <= 0.50 THEN 'HIGH'
        WHEN RATIO <= 0.75 THEN 'MEDIUM'
        WHEN RATIO <= 1 THEN 'LOW'
    END AS COLONY_NAME
FROM RATIO_DATA
ORDER BY ID
;