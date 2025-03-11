select month(start_date) AS 'MONTH', CAR_ID, count(*) AS 'RECORDS'
from car_rental_company_rental_history
where start_date >= '2022-08-01'
  and start_date < '2022-11-01'
  and car_id in (
    select car_id
    from car_rental_company_rental_history
    where start_date >= '2022-08-01'
      and start_date < '2022-11-01'
    group by car_id
    having count(*) >= 5
)
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc;