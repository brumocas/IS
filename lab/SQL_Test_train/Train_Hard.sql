-- 1) Retrieve the top 5 airports with the highest number of outbound flights
-- Sol with limit
select a.name, count(p.destination) as Outbound_Flights
from airports as a
left join patterns as p on p.destination = a.airport
group by a.airport
order by count(p.destination) desc
limit 5;

-- Sol with subquery
select a.name, count(p.destination) as Outbound_Flights
from airports as a
left join patterns as p on p.destination = a.airport
group by a.airport
having count(p.destination) in (
    select distinct count(pp.destination) from airports as aa
    left join patterns as pp on pp.destination = aa.airport
    group by aa.airport
    limit 5)
order by count(p.destination) desc;



-- 2) Find the average duration of flights for each carrier
select carrier, round(avg(duration),2) as average_tof
from patterns
group by carrier
order by average_tof desc;



-- 3) Retrieve the names of airports that have both inbound and outbound flights
-- sol 1 --
select distinct a.name
from patterns as p 
join airports as a on p.origin = a.airport
where a.name in ( 
   select aa.name
   from patterns as pp 
   join airports as aa on pp.destination = aa.airport
)
order by a.name;
-- sol 2 --
select a.name
from airports a
inner join (
    select distinct origin
    from patterns
) as outbound on a.airport = outbound.origin
inner join (
    select distinct destination
    from patterns
) as inbound on a.airport = inbound.destination
order by a.name;



-- 4) Find the model of aircraft used by carriers operating flights from Porto to Lisboa
select a1.city as origin, a2.city as destination, m.model
from patterns as p
join airports as a1 on a1.airport = p.origin
join airports as a2 on a2.airport = p.destination
join models as m on p.model = m.model
where a1.city = 'Porto' and a2.city = 'Lisboa';



-- 5) Retrieve the details of the longest flight pattern
select p.flight, a1.name as origin, a2.name as destination, p.carrier, p.duration, p.model
from patterns as p
join airports as a1 on a1.airport = p.origin
join airports as a2 on a2.airport = p.destination
where p.duration = (select max(pp.duration) from patterns as pp);



-- 6) Find the carriers that operate flights to destinations with more than one airport
select carrier
from patterns
group by carrier
having count(distinct destination) > 1;



-- 7) Write a query to find all airports that are not the origin of any flight pattern
-- solution 1 --
select a.name
from airports as a
left join patterns as p on p.origin = a.airport
where p.origin is null;

-- solution 2 --
select name
from airports
where airport not in (select distinct origin from patterns);



-- 8) Retrieve the names of carriers that operate flights with a duration longer than the average duration of all flights
select distinct carrier
from patterns 
where duration > (select avg(duration) from patterns);



-- 9) Find the airports where the total duration of all outbound flights exceeds the total duration of inbound flights
SELECT a1.name, MAX(p.duration)
FROM patterns AS p
JOIN airports AS a1 ON p.origin = a1.airport
GROUP BY a1.airport
HAVING MAX(p.duration) > (
    SELECT MAX(pp.duration)
    FROM patterns AS pp
    JOIN airports AS a2 ON pp.destination = a2.airport
    WHERE a2.airport = a1.airport
);



-- 10) Find the average number of engines for aircraft manufactured by each manufacturer
sol manufacturer , Round(avg(engines),2)
from models
group by manufacturer;



-- 11) Number of flights departing from each city
select a.city, count(p.origin) as Departures
from airports as a
join patterns  as p on p.origin = a.airport
group by a.city;



-- 12) Identify the carriers that operate flights using aircraft with more engines than the average number of engines across all aircraft
select distinct p.carrier
from patterns as p
join models as m on m.model = p.model
where m.engines > ( select avg(engines) from models )



-- 13) Find the flight patterns with the longest duration for each carrier
SELECT p.carrier, p.flight, p.duration
FROM patterns p
JOIN (
    SELECT carrier, MAX(duration) AS max_duration
    FROM patterns
    GROUP BY carrier
) AS max_durations ON p.carrier = max_durations.carrier AND p.duration = max_durations.max_duration;



-- 14) Retrieve the carriers that operate flights to destinations where the average flight duration is above a certain threshold (e.g., 120 minutes)
SELECT DISTINCT p.carrier
FROM patterns p
JOIN (
    SELECT destination, AVG(duration) AS avg_duration
    FROM patterns
    GROUP BY destination
) AS avg_durations ON p.destination = avg_durations.destination
WHERE avg_durations.avg_duration > 120;




