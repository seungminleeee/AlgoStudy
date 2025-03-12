select a.ID,
    case
        when b.rk <= 0.25 then 'CRITICAL'
        when b.rk <= 0.50 then 'HIGH'
        when b.rk <= 0.75 then 'MEDIUM'
        else 'LOW'
    end as COLONY_NAME
from ecoli_data a
join
(
    select id, percent_rank() over (order by size_of_colony desc) as rk
    from ecoli_data
) b
on a.id = b.id;