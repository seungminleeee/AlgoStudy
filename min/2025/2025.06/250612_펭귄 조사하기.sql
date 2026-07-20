select species, island
from penguins
group by island, species
order by island, species