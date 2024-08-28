-- 서브쿼리 사용
SELECT * FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE)FROM FOOD_PRODUCT)

-- ORDER BY LIMIT 사용
SELECT * FROM FOOD_PRODUCT
ORDER BY PRICE DESC LIMIT 1