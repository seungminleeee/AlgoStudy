select u.USER_ID, u.NICKNAME, sum(b.price) AS "TOTAL_SALES"
from used_goods_board b
join used_goods_user u
on b.writer_id = u.user_id
where b.status = 'DONE'
group by u.user_id, u.nickname
having sum(b.price) >= 700000
order by total_sales asc;