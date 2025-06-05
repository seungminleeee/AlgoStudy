select round(sum(tip), 2) AS tip_daily, day
from tips
group by day
order by tip_daily desc
limit 1;