SELECT * FROM yl21_Books;

SELECT * FROM yl21_Books
WHERE release_date >= "2010" AND type = 'new'
ORDER BY title;

SELECT title, release_date, price, type FROM yl21_Books
WHERE release_date < '1970' AND type = 'used' AND price < 20;

SELECT YEAR(order_date) AS 'Aasta', COUNT(id) AS 'Tellimuste arv'
FROM yl21_Orders
GROUP BY YEAR (order_date);

SELECT YEAR(yl21_Orders.order_date) AS 'Aasta', COUNT(yl21_Orders.id) AS 'Tellimuste arv', ROUND(SUM(yl21_Books.price), 2) AS 'Ümardatud hind'
FROM yl21_Orders
LEFT JOIN yl21_Books  ON yl21_Orders.book_id = yl21_Books.id 
group BY YEAR (yl21_Orders.order_date);

SELECT YEAR(yl21_Orders.order_date ) AS 'Aasta',COUNT(yl21_Orders.id)AS 'Tellimuste arv',round(SUM(yl21_Books.price), 2) AS 'Hind'
FROM yl21_Orders
LEFT JOIN yl21_Books  ON yl21_Orders.book_id = yl21_Books.id
where year(yl21_Orders.order_date) = '2017';

SELECT ROUND(sum(yl21_Books.price),2)AS 'Tellimuste summa', yl21_Clients.username AS 'Kasutajanimi', COUNT(yl21_Orders.id)AS 'Tellimuste arv'
FROM yl21_Orders 
LEFT JOIN yl21_Books ON yl21_Orders.book_id = yl21_Books.id
LEFT JOIN yl21_Clients on yl21_Orders.client_id = yl21_Clients.id
WHERE YEAR(yl21_Orders.order_date) ='2017'
GROUP BY yl21_Clients.id ORDER BY SUM(price) desc;

SELECT COUNT(yl21_Orders.book_id) AS 'Tellimuste arv', yl21_Books.title AS 'Raamatu nimi'
from yl21_Orders
left join yl21_Books on yl21_Orders.book_id = yl21_Books.id
WHERE
   year(yl21_Orders.order_date) ='2017' and
   month(yl21_Orders.order_date) ='9'
GROUP BY yl21_Books.title ORDER BY COUNT(yl21_Orders.book_id) desc LIMIT 10;

SELECT title AS 'Raamatu nimi', price AS 'Hind'
from yl21_Books
where price > (select avg(price) from yl21_Books)
group by price, title
order by price;
