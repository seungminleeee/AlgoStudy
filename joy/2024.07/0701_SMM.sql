-- SUM, MAX, MIN 은 전체적으로 쉽네... 근데 다른건 너무 어려웡 ㅜㅜ --

SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND'