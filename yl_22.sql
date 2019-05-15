SELECT * FROM yl21_Books;
SELECT SUM(yl21_Books.stock_saldo) FROM yl21_Books;

select MIN(price), MAX(price),avg(price)
from yl21_Books;

select max(price)
FROM yl21_Books
where type = 'used';

select type AS'Tüüp', round(avg(price),2)AS 'Keskmine hind', count(id)AS 'Hulk'
FROM yl21_Books
group BY type;

select title AS'Pealkiri', price AS 'Hind', type AS 'Tüüp'
from yl21_Books
where type ='used' and price > (select avg(price)from yl21_Books where type = 'new')
group by title order by price asc;


select release_date AS 'Aasta', yl21_Books.title AS 'Pealkiri'
from yl21_Books 
where MOD(release_date,2) = 0 
order by release_date asc;

select language AS 'Keel', count(id) AS'Hulk'
from yl21_Books
group by language
order by count(id) desc;

SELECT title AS 'PEALKIRI'
FROM yl21_Books
WHERE price > (SELECT AVG(yl21_Books.price)
from yl21_Orders
left join yl21_Books
on yl21_Books.id = yl21_Orders.book_id
left join yl21_Book_Authors
on yl21_Book_Authors.book_id = yl21_Books.id
group by yl21_Book_Authors.author_id
order by count(*) desc limit 1);
