-- 모르겠어서 질문게시판 좀 봤는데 .. 
-- & 로도 할 수 있대서 이해하고 풀었어!! 
-- & => sql 에서 비트 연산자를 사용해주는거래

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME 
FROM DEVELOPERS
WHERE SKILL_CODE & 
(SELECT SUM(CODE) 
 FROM SKILLCODES
 WHERE NAME IN ('Python', 'C#'))
ORDER BY ID;