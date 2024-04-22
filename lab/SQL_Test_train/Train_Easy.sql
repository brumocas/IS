-- 1) Write a SQL query to retrieve all airports located in the city of Paris.
select name 
from airports
where city = 'Paris'
order by name asc

-- 2) Write a query to display the names and manufacturers of all aircraft models in the database.
select c.name as Craft, m.manufacturer
from crafts as c
left join models as m on m.model = c.model

-- 3) Write a SQL query to find the average duration of all flight patterns.  
select avg(p.duration) as "average flight duration"
from patterns as p

-- 4) How can you retrieve the names of all airlines operating flights in Porto?
select p.carrier
from patterns as p
left join airports as a1 on p.origin = a1.airport
left join airports as a2 on p.destination = a2.airport
where a1.city = 'Porto' or a2.city = 'Porto'

-- 5) Write a query to list all flight patterns operated by TAP.
select p.*
from patterns as p
where p.carrier = 'TAP'

-- 6) How would you write a query to count the number of flight patterns originating from each airport?
select a.name, count(p.*) as num_of_flights
from patterns as p
right join airports as a on p.origin = a.airport
group by a.airport
order by count(p.*) desc

-- 7) Write a SQL query to find the crafts with the maximum number of engines among all aircraft models.
select c.name
from crafts as c 
join models as m on c.model = m.model
where m.engines = (select max(mm.engines) from models as mm)
order by m.model desc

-- 8) How can you retrieve the details of flights departing from and arriving at the same airport?
 select * from patterns where origin = destination;

-- 9) Write a query to find the total number of flights operated by each carrier.
select carrier, count(*) as num_flights from patterns group by carrier;

-- 10) How would you retrieve the names of airports and their corresponding cities in alphabetical order?
select name, city
from airports
order by name asc, city asc


