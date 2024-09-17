# SQL Server 에서 쓰는 ISNULL 계속 쓰다가 오류가 남 ㅜㅜ! 
# MySQL 에서는 IFNULL 로 NULL 인 컬럼을 대체값으로 대체해준다 이런식으로 씀 !  
# IFNULL(컬럼이름, 대체값)

SELECT ANIMAL_TYPE, 
    IFNULL(NAME, 'No name') AS NAME, 
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;