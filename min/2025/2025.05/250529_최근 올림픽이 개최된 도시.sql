select year, upper(substr(city, 0, 4)) as city
from games
where year >= 2000
order by year desc