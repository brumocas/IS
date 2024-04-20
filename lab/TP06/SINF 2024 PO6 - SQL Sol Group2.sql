-- Question 1 --
SELECT s.name
from specialty as s
order by s.name desc
limit 2
offset 1

-- Question  2 --
SELECT name, tel
FROM hospital
WHERE tel LIKE '21%' OR tel LIKE '22%'
ORDER BY SUBSTR(tel,1,2) DESC, name ASC

-- Question 3 --
SELECT c.name, count(h.name)
from city as c
left join hospital as h on h.city = c.name 
group by c.name
having count(h.name) <= 3 and count(h.name) >= 0
order by count(h.name) desc

SELECT city.name, count(hospital.name)
FROM city
FULL OUTER JOIN hospital ON city.name=hospital.city
GROUP BY city.name
HAVING count(hospital.name)<4
ORDER BY count(hospital.name) DESC

-- Question 4 --
SELECT city.name AS city_name, doctor.name AS doctor_name
FROM city, hospital, doctor
WHERE city.name = hospital.city AND
 doctor.main_contract=hospital.id
ORDER by city.name, doctor.name

-- Question 5 --
SELECT s2.name AS specialty_family, s1.name AS specialty_child
FROM specialty AS s1
FULL OUTER JOIN specialty AS s2 ON s1.related = s2.key
WHERE s2.related is NULL and s2.name is not null and s2.name <> 'Pediatrics'
ORDER BY s2.name ASC , s1.name DESC

-- Question 6 --
SELECT s2.name AS family, count(s1.name)
FROM specialty AS s1
FULL OUTER JOIN specialty AS s2 ON s1.related = s2.key
WHERE s2.related is NULL
GROUP by s2.name
HAVING count(s1.name) < 4
ORDER BY s2.name

