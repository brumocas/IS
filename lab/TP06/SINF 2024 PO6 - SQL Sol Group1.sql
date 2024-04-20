-- Question 1 --
select distinct h.city
from hospital as h;

-- Question 2 --
select c.name
from city as c
left join hospital as h on c.name = h.city
where h.city is null;

-- Question 3 --
select city, count(*) as "Number of hospitals"
from hospital
group by city
order by "Number of hospitals" desc
limit 2;

select city
from hospital
group by city
order by count(id) desc
limit 2;

-- Question 4 --
select h.name, s.name
from hospital as h
join hospital_speciallity as hs on h.id = hs.hosp
join specialty as s on s.key = hs.spec
where hs.end_year = 0
order by h.name, s.name asc;

select distinct hospital.name, specialty.name
from hospital, specialty, hospital_speciallity
where hospital.id = hosp and spec = specialty.key and end_year = 0
order by hospital.name, specialty.name;

-- Question 5 --
SELECT s.name, COUNT(hosp) as "Number of hospitals"
FROM hospital_speciallity as hs
JOIN specialty as s ON hs.spec = s.key
WHERE hs.end_year = 0
GROUP BY s.name 
HAVING COUNT(hosp) > 1
ORDER BY s.name ASC;

SELECT specialty.name, count(hospital.name)
FROM hospital, specialty, hospital_speciallity
WHERE hospital.id=hosp AND spec=specialty.key AND end_year = 0
GROUP BY specialty.name
HAVING count(hospital.name)>1
ORDER BY specialty.name

-- Question 6 --
select c.name, count(h.id)
from city as c
left join hospital as h on c.name = h.city
group by c.name
order by count(h.id) desc

SELECT city.name, count(hospital.name)
FROM city
FULL OUTER JOIN hospital ON city.name=hospital.city
GROUP BY city.name
ORDER BY count(hospital.name) desc







