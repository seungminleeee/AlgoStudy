# sql 조건문 한동안 안썼더니 또 까먹음 ;;;;; CASE WHEN THEN END) <- END 로 끝내줘야함. 
# if 같은 거랄까 ... ㅎㅎ  

SELECT ORDER_ID, PRODUCT_ID, LEFT(OUT_DATE, 10), 
(CASE WHEN OUT_DATE <= '2022-05-01' THEN '출고완료' 
      WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
      WHEN OUT_DATE IS NULL THEN '출고미정' END
 ) AS '출고완료'
FROM FOOD_ORDER
ORDER BY ORDER_ID;
