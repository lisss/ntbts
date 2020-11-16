-- AND and BETWEEN

select *
from web_events
where channel in ('organic', 'adwords')
and occurred_at between '2016-01-01' and '2017-01-01'
order by occurred_at desc;


-- OR
select name, primary_poc
from accounts
where (name like 'C%' or name like 'W%')
    and ((primary_poc like '%ana%' or primary_poc like '%Ana%')
    and primary_poc not like '%eana%');


-- INNER JOIN
SELECT orders.standard_qty, orders.gloss_qty, orders.poster_qty, accounts.website, accounts.primary_poc
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;

--
select a.primary_poc, w.occurred_at, w.channel
from web_events as w
join accounts as a
on w.account_id = a.id
where a.name = 'Walmart';

select r.name as reg_name, s.name sales_rep_name, a.name acc_name
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
order by a.name;

select r.name as reg_name, a.name acc_name, o.total_amt_usd/(o.total + 0.01) as unit_price
from orders as o
join accounts as a
on o.account_id = a.id
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id;


--
select r.name as reg_name, s.name as sales_rep_name, a.name as acc_name
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
where r.name = 'Midwest'
order by a.name;

select r.name as reg_name, s.name as sales_rep_name, a.name as acc_name
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
where r.name = 'Midwest' and s.name like 'S%'
order by a.name;

select r.name as reg_name, s.name as sales_rep_name, a.name as acc_name
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
where r.name = 'Midwest' and s.name like '% K%'
order by a.name;

select r.name as reg_name, a.name as acc_name, o.total_amt_usd/(o.total + 0.01) as unit_price
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
join orders as o
on o.account_id = a.id
where o.standard_qty > 100;

select r.name as reg_name, a.name as acc_name, o.total_amt_usd/(o.total + 0.01) as unit_price
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
join orders as o
on o.account_id = a.id
where o.standard_qty > 100 and o.poster_qty > 50
order by unit_price;

select r.name as reg_name, a.name as acc_name, o.total_amt_usd/(o.total + 0.01) as unit_price
from accounts as a
join sales_reps as s
on a.sales_rep_id = s.id
join region as r
on s.region_id = r.id
join orders as o
on o.account_id = a.id
where o.standard_qty > 100 and o.poster_qty > 50
order by unit_price desc;

select distinct a.name, e.channel
from accounts as a
join web_events as e
on e.account_id = a.id
where a.id = 1001;

select o.occurred_at, a.name, o.total, o.total_amt_usd
from orders as o
join accounts as a
on o.account_id = a.id
where o.occurred_at between '2015-01-01' and '2016-01-01';

-- AGGREGATION

SELECT COUNT(*) as acc_num
FROM accounts;

SELECT COUNT(accounts.id) as acc_num
FROM accounts;

SELECT COUNT(id) as acc_num
FROM accounts;

SELECT COUNT(1) as acc_num
FROM accounts;


select sum(poster_qty)
from orders

select standard_amt_usd + gloss_amt_usd as standard_gloss_amt_usd
from orders

SELECT SUM(standard_amt_usd)/SUM(standard_qty) AS standard_price_per_unit
FROM orders;

-- bonus: find a median
SELECT Sales Median FROM
(SELECT a1.Name, a1.Sales, COUNT(a1.Sales) Rank
FROM Total_Sales a1, Total_Sales a2
WHERE a1.Sales < a2.Sales OR (a1.Sales=a2.Sales AND a1.Name <= a2.Name)
group by a1.Name, a1.Sales
order by a1.Sales desc) a3
WHERE Rank = (SELECT (COUNT(*)+1) DIV 2 FROM Total_Sales);

select min(occurred_at)
from orders
-- same as
select occurred_at
from orders
order by occurred_at
limit 1


select max(occurred_at)
from web_events
-- same as
select occurred_at
from web_events
order by occurred_at desc
limit 1

select avg(standard_amt_usd) as avg_usd_std,
    avg(gloss_amt_usd) as avg_usd_gloss,
    avg(poster_amt_usd) as avg_usd_poster,
    avg(standard_qty) as avg_qty_std,
    avg(gloss_qty) as avg_qty_gloss, 
    avg(poster_qty) as avg_qty_poster
from orders

-- not sure i've got it
SELECT *
FROM (SELECT total_amt_usd
      FROM orders
      ORDER BY total_amt_usd
      LIMIT ((select count(*) from orders)/2)) AS Table1
ORDER BY total_amt_usd DESC
LIMIT 2;


select a.name, o.occurred_at
from accounts as a
join orders as o
on o.account_id = a.id
order by o.occurred_at
limit 1;

select a.name, sum(o.total_amt_usd)
from accounts as a
join orders as o
on o.account_id = a.id
group by a.name;

select e.occurred_at, e.channel, a.name
from web_events e
join accounts a
on e.account_id = a.id
order by e.occurred_at desc
limit 1;

select channel, count(channel) as was_used
from web_events
group by channel;

select a.primary_poc
from web_events e
join accounts a
on e.account_id = a.id
order by e.occurred_at
limit 1;

select a.name, min(o.total_amt_usd)
from accounts a
join orders o
on a.id = o.account_id
group by o.total_amt_usd, a.name
order by o.total_amt_usd;

select r.name, count(s.id) as num_reps
from region r
join sales_reps s
on r.id = s.region_id
group by r.name
order by num_reps;


select a.name, avg(o.standard_qty) as s_qty_avg, avg(o.gloss_qty) as g_qty_avg, avg(o.poster_qty)  as p_qty_avg
from accounts as a
join orders as o
on o.account_id = a.id
group by a.name;


select a.name, avg(o.standard_amt_usd) as s_per_order_avg, avg(o.gloss_amt_usd) as g_per_order_avg, avg(o.poster_amt_usd) as p_per_order_avg
from accounts as a
join orders as o
on o.account_id = a.id
group by a.name;

select s.name, e.channel, count(e.channel) as occurences
from web_events as e
join accounts as a
on e.account_id = a.id
join sales_reps as s
on s.id = a.sales_rep_id
group by s.name, e.channel
order by occurences desc;

select r.name, e.channel, count(e.channel) as occurences
from web_events as e
join accounts as a
on e.account_id = a.id
join sales_reps as s
on s.id = a.sales_rep_id
join region as r
on r.id = s.region_id
group by r.name, e.channel
order by occurences desc;

-- DISTINCT
SELECT a.id as "account id", r.id as "region id", 
a.name as "account name", r.name as "region name"
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id;

SELECT s.id, s.name, COUNT(*) num_accounts
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.id, s.name
ORDER BY num_accounts;

-- HAVING
SELECT s.id, s.name, COUNT(*) num_accounts
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.id, s.name
HAVING COUNT(*) > 5
ORDER BY num_accounts;

SELECT a.id, a.name, COUNT(*) num_orders
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
HAVING COUNT(*) > 20
ORDER BY num_orders;

SELECT a.id, a.name, COUNT(*) num_orders
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY num_orders desc
LIMIT 1;

SELECT a.id, a.name, SUM(o.total_amt_usd) total
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
HAVING SUM(o.total_amt_usd) > 30000
ORDER BY total DESC;

SELECT a.id, a.name, SUM(o.total_amt_usd) total
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
HAVING SUM(o.total_amt_usd) < 1000
ORDER BY total DESC;

SELECT a.id, a.name, SUM(o.total_amt_usd) total
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY total DESC
LIMIT 1;

SELECT a.id, a.name, SUM(o.total_amt_usd) total
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY total
LIMIT 1;

select a.name, count(*) as fb_contacts
from accounts as a
join web_events as e
on e.account_id = a.id
group by a.name
HAVING COUNT(*) > 6 AND w.channel = 'facebook'
order by fb_contacts desc;

select a.name, count(*) as fb_contacts
from accounts as a
join web_events as e
on e.account_id = a.id
where e.channel = 'facebook'
group by a.name
order by fb_contacts desc
limit 1;

SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
GROUP BY a.id, a.name, w.channel
ORDER BY use_of_channel DESC
LIMIT 10;


-- DATE
 SELECT DATE_PART('year', occurred_at) ord_year,  SUM(total_amt_usd) total_spent
 FROM orders
 GROUP BY 1
 ORDER BY 2 DESC;

 SELECT DATE_PART('month', occurred_at) month_,  SUM(total_amt_usd) total_spent
 FROM orders
 WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
 GROUP BY 1
 ORDER BY 2 DESC;

 SELECT DATE_PART('year', occurred_at) year_,  COUNT(*) total_orders
 FROM orders
 GROUP BY 1
 ORDER BY 2 DESC;

  SELECT DATE_PART('month', occurred_at) month_,  COUNT(*) total_orders
 FROM orders
 WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
 GROUP BY 1
 ORDER BY 2 DESC;

  SELECT DATE_TRUNC('month', o.occurred_at) month_,  SUM(o.gloss_amt_usd) gloss_total
 FROM orders as o
 JOIN accounts as a
 ON o.account_id = a.id
 WHERE a.name = 'Walmart'
 GROUP BY 1
 ORDER BY 2 DESC
 LIMIT 1;


 -- CASE
 select account_id, total_amt_usd,
	case when total_amt_usd >= 3000 then 'Large'
    else 'Small' end as level
from orders;

select
	case
    	when total >= 2000 then 'At Least 2000'
        when total between 1000 and 2000 then 'Between 1000 and 2000'
    	else 'Less than 1000' end as total_cat,
    count(*)
from orders
group by 1;

select a.name, sum(o.total_amt_usd) as total_usd,
	case
    	when o.total_amt_usd > 200000 then 'Over 200K'
        when o.total_amt_usd between 100000 and 200000 then '100K - 200K'
        else 'Under 100K' end as level
from orders as o
join accounts as a
on o.account_id = a.id
group by a.name, o.total_amt_usd
order by 2 desc;

SELECT a.name, SUM(total_amt_usd) total_spent, 
     CASE WHEN SUM(total_amt_usd) > 200000 THEN 'top'
     WHEN  SUM(total_amt_usd) > 100000 THEN 'middle'
     ELSE 'low' END AS customer_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
WHERE occurred_at > '2015-12-31' 
GROUP BY 1
ORDER BY 2 DESC;

select s.name, count(o.*) as total_orders,
	case
    	when count(o.*) > 200 then 'top'
        else 'not' end as is_top
from orders o
join accounts as a
on a.id = o.account_id
join sales_reps as s
on a.sales_rep_id = s.id
group by s.name
order by 2 desc;

select s.name, count(o.*) as total_orders, 	sum(o.total_amt_usd) as total_usd,
	case
    	when count(o.*) > 200 or sum(o.total_amt_usd) > 750000 then 'top'
        when count(o.*) between 150 and 200 or sum(o.total_amt_usd) between 500000 and 750000 then 'middle'
        else 'not' end as is_top
from orders o
join accounts as a
on a.id = o.account_id
join sales_reps as s
on a.sales_rep_id = s.id
group by s.name
order by 3 desc;


-- SUBQUERIES

--We want to find the average number of events for each day for each channel. The first table will provide us the number of events for each day and channel, and then we will need to average these values together using a second query.
SELECT channel, AVG(events) AS average_events
FROM (SELECT DATE_TRUNC('day',occurred_at) AS day,
             channel, COUNT(*) as events
      FROM web_events 
      GROUP BY 1,2) sub
GROUP BY channel
ORDER BY 2 DESC;

select avg(standard_qty) as avg_std, avg(gloss_qty) as avg_gloss, avg(poster_qty) as avg_poster, sum(total_amt_usd) from orders
where date_trunc('month', occurred_at) =
  (select min(date_trunc('month', occurred_at)) as min_occured
  from orders)


-- 1.
SELECT t3.rep_name, t3.region_name, t3.total_amt
FROM(SELECT region_name, MAX(total_amt) total_amt
     FROM(SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
             FROM sales_reps s
             JOIN accounts a
             ON a.sales_rep_id = s.id
             JOIN orders o
             ON o.account_id = a.id
             JOIN region r
             ON r.id = s.region_id
             GROUP BY 1, 2) t1
     GROUP BY 1) t2
JOIN (SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
     FROM sales_reps s
     JOIN accounts a
     ON a.sales_rep_id = s.id
     JOIN orders o
     ON o.account_id = a.id
     JOIN region r
     ON r.id = s.region_id
     GROUP BY 1,2
     ORDER BY 3 DESC) t3
ON t3.region_name = t2.region_name AND t3.total_amt = t2.total_amt;

-- 2.
SELECT r.name, COUNT(o.total) total_orders
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
JOIN region r
ON r.id = s.region_id
GROUP BY r.name
HAVING SUM(o.total_amt_usd) = (
      SELECT MAX(total_amt)
      FROM (SELECT r.name region_name, SUM(o.total_amt_usd) total_amt
              FROM sales_reps s
              JOIN accounts a
              ON a.sales_rep_id = s.id
              JOIN orders o
              ON o.account_id = a.id
              JOIN region r
              ON r.id = s.region_id
              GROUP BY r.name) sub);

-- 3.
SELECT COUNT(*)
FROM (SELECT a.name
       FROM orders o
       JOIN accounts a
       ON a.id = o.account_id
       GROUP BY 1
       HAVING SUM(o.total) > (SELECT total 
                   FROM (SELECT a.name act_name, SUM(o.standard_qty) tot_std, SUM(o.total) total
                         FROM accounts a
                         JOIN orders o
                         ON o.account_id = a.id
                         GROUP BY 1
                         ORDER BY 2 DESC
                         LIMIT 1) inner_tab)
             ) counter_tab;


-- 4.
select e.channel, count(*) as ev_cnt
from web_events as e
join accounts as a
on e.account_id = a.id
where e.account_id =
    (select t2.acc_id
    from
    (select a.id as acc_id, sum(o.total_amt_usd) total
    from accounts as a
    join orders as o
    on o.account_id = a.id
    group by 1
    order by 2 desc
    limit 1) t2)
group by e.channel


-- 5.
SELECT AVG(tot_spent)
FROM (SELECT a.id, a.name, SUM(o.total_amt_usd) tot_spent
      FROM orders o
      JOIN accounts a
      ON a.id = o.account_id
      GROUP BY a.id, a.name
      ORDER BY 3 DESC
       LIMIT 10) temp;

-- 6.
SELECT AVG(avg_amt)
FROM (SELECT o.account_id, AVG(o.total_amt_usd) avg_amt
    FROM orders o
    GROUP BY 1
    HAVING AVG(o.total_amt_usd) > (SELECT AVG(o.total_amt_usd) avg_all
                                   FROM orders o)) temp_table;


-- WITH

-- 1.
WITH regions AS (SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
             FROM sales_reps s
             JOIN accounts a
             ON a.sales_rep_id = s.id
             JOIN orders o
             ON o.account_id = a.id
             JOIN region r
             ON r.id = s.region_id
             GROUP BY 1, 2),
    total_amt AS (SELECT region_name, MAX(total_amt) total_amt
        FROM regions
        GROUP BY 1)

SELECT regions.rep_name, regions.region_name, regions.total_amt
FROM total_amt
JOIN regions
ON regions.region_name = total_amt.region_name AND regions.total_amt = total_amt.total_amt;

-- 2.
WITH reg_tot AS (SELECT r.name region_name, SUM(o.total_amt_usd) total_amt
              FROM sales_reps s
              JOIN accounts a
              ON a.sales_rep_id = s.id
              JOIN orders o
              ON o.account_id = a.id
              JOIN region r
              ON r.id = s.region_id
              GROUP BY r.name),
    is_sum_eq AS (
      SELECT MAX(total_amt)
      FROM reg_tot)

SELECT r.name, COUNT(o.total) total_orders
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
JOIN region r
ON r.id = s.region_id
GROUP BY r.name
HAVING SUM(o.total_amt_usd) = (SELECT * FROM is_sum_eq);

-- 3.
WITH inner_tab AS (SELECT a.name act_name, SUM(o.standard_qty) tot_std, SUM(o.total) total
                         FROM accounts a
                         JOIN orders o
                         ON o.account_id = a.id
                         GROUP BY 1
                         ORDER BY 2 DESC
                         LIMIT 1),
    cnt AS (SELECT a.name
       FROM orders o
       JOIN accounts a
       ON a.id = o.account_id
       GROUP BY 1
       HAVING SUM(o.total) > (SELECT total FROM inner_tab))
    
SELECT COUNT(*)
FROM cnt;

-- 4.
WITH t2 as (select a.id as acc_id, sum(o.total_amt_usd) total
        from accounts as a
        join orders as o
        on o.account_id = a.id
        group by 1
        order by 2 desc
        limit 1)

select e.channel, count(*) as ev_cnt
from web_events as e
join accounts as a
on e.account_id = a.id
where e.account_id = (SELECT acc_id FROM t2)
group by e.channel

-- 5.
WITH spent AS (SELECT a.id, a.name, SUM(o.total_amt_usd) tot_spent
      FROM orders o
      JOIN accounts a
      ON a.id = o.account_id
      GROUP BY a.id, a.name
      ORDER BY 3 DESC
       LIMIT 10)
SELECT AVG(tot_spent) from spent

-- 6.
WITH t1 AS (SELECT AVG(o.total_amt_usd) avg_all
                FROM orders o),
    t2 AS (SELECT o.account_id, AVG(o.total_amt_usd) avg_amt
    FROM orders o
    GROUP BY 1
    HAVING AVG(o.total_amt_usd) > (SELECT * from t1))
SELECT AVG(avg_amt)
FROM t2;


-- LESSON 5: LEFT & RIGHT

-- 1.
select RIGHT(website, 3) as ext, COUNT(*)
from accounts
group by ext

-- 2.
select LEFT(name, 1) as start_let, COUNT(*) as cnt
from accounts
group by start_let
order by cnt desc

-- 3.
SELECT SUM(num) nums, SUM(letter) letters
FROM (SELECT name, CASE WHEN LEFT(UPPER(name), 1) ~ '^\d+$'
                       THEN 1 ELSE 0 END AS num, 
         CASE WHEN LEFT(UPPER(name), 1) ~ '^\d+$' 
                       THEN 0 ELSE 1 END AS letter
      FROM accounts) t1;

-- 4.
SELECT SUM(vowels) vowels, SUM(other) other
FROM (SELECT name, CASE WHEN LEFT(UPPER(name), 1) IN ('A','E','I','O','U') 
                        THEN 1 ELSE 0 END AS vowels, 
          CASE WHEN LEFT(UPPER(name), 1) IN ('A','E','I','O','U') 
                       THEN 0 ELSE 1 END AS other
         FROM accounts) t1;


-- LESSON 6: Window functions

-- 1. Creating a Running Total Using Window Functions
SELECT standard_amt_usd,
       SUM(standard_amt_usd) OVER (ORDER BY occurred_at) AS running_total
FROM orders


-- 2. Creating a Partitioned Running Total Using Window Functions
SELECT standard_amt_usd, DATE_TRUNC('year', occurred_at) as occured_year,
	SUM(standard_amt_usd) OVER (PARTITION BY DATE_TRUNC('year', occurred_at) ORDER BY occurred_at) AS running_total
FROM orders

-- 3. Ranking Total Paper Ordered by Account
select id, account_id, total,
rank() over(partition by account_id order by total desc) as total_rank
from orders

-- 4. Aggregates in Window Functions with and without ORDER BY
SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS dense_rank,
       SUM(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month',occurred_at)) AS max_std_qty
FROM orders

-- remove ORDER BY and see what happens
SELECT id,
       account_id,
       standard_qty,
       DATE_TRUNC('month', occurred_at) AS month,
       DENSE_RANK() OVER (PARTITION BY account_id) AS dense_rank,
       SUM(standard_qty) OVER (PARTITION BY account_id) AS sum_std_qty,
       COUNT(standard_qty) OVER (PARTITION BY account_id) AS count_std_qty,
       AVG(standard_qty) OVER (PARTITION BY account_id) AS avg_std_qty,
       MIN(standard_qty) OVER (PARTITION BY account_id) AS min_std_qty,
       MAX(standard_qty) OVER (PARTITION BY account_id) AS max_std_qty
FROM orders

-- 5. Shorten Your Window Function Queries by Aliasing
-- initial query
SELECT id,
       account_id,
       DATE_TRUNC('year',occurred_at) AS year,
       DENSE_RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at)) AS dense_rank,
       total_amt_usd,
       SUM(total_amt_usd) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at)) AS sum_total_amt_usd,
       COUNT(total_amt_usd) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at)) AS count_total_amt_usd,
       AVG(total_amt_usd) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at)) AS avg_total_amt_usd,
       MIN(total_amt_usd) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at)) AS min_total_amt_usd,
       MAX(total_amt_usd) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at)) AS max_total_amt_usd
FROM orders


SELECT id,
       account_id,
       DATE_TRUNC('year',occurred_at) AS year,
       DENSE_RANK() OVER account_year_window AS dense_rank,
       total_amt_usd,
       SUM(total_amt_usd) OVER account_year_window AS sum_total_amt_usd,
       COUNT(total_amt_usd) OVER account_year_window AS count_total_amt_usd,
       AVG(total_amt_usd) OVER account_year_window AS avg_total_amt_usd,
       MIN(total_amt_usd) OVER account_year_window AS min_total_amt_usd,
       MAX(total_amt_usd) OVER account_year_window AS max_total_amt_usd
FROM orders
WINDOW account_year_window as (PARTITION BY account_id ORDER BY DATE_TRUNC('year',occurred_at))


-- 6. Comparing a Row to Previous Row
SELECT occurred_at,
       total_amt_usd,
       LEAD(total_amt_usd) OVER (ORDER BY occurred_at) AS lead,
       LEAD(total_amt_usd) OVER (ORDER BY occurred_at) - total_amt_usd AS lead_difference
FROM (
SELECT occurred_at,
       SUM(total_amt_usd) AS total_amt_usd
  FROM orders 
 GROUP BY 1
) sub

-- 7. Percentiles with Partitions
SELECT
       account_id,
       occurred_at,
       standard_qty,
       NTILE(4) OVER (PARTITION BY account_id ORDER BY standard_qty) AS standard_quartile
  FROM orders 
 ORDER BY account_id DESC

 SELECT
       account_id,
       occurred_at,
       gloss_qty,
       NTILE(2) OVER (PARTITION BY account_id ORDER BY gloss_qty) AS gloss_half
  FROM orders 
 ORDER BY account_id DESC

 SELECT
       account_id,
       occurred_at,
       total_amt_usd,
       NTILE(100) OVER (PARTITION BY account_id ORDER BY total_amt_usd) AS total_percentile
  FROM orders 
 ORDER BY account_id DESC
