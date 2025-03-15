# 하... 25.5 같은 소수점을 놓쳤삼 ... 
select ID,
case when COLONY_PER <= 25 then 'CRITICAL' 
    when COLONY_PER > 25 and COLONY_PER <= 50  then 'HIGH'  
    when COLONY_PER > 50 and COLONY_PER <= 75 then 'MEDIUM'  
    when COLONY_PER > 75 then 'LOW'  
    end as COLONY_NAME
from (select ID, 
      percent_rank() over (order by SIZE_OF_COLONY desc) * 100 
      as COLONY_PER
      from ECOLI_DATA) as ECOLI_DATA2
order by ID;