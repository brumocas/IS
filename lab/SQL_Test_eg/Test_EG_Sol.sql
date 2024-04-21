-- Question 1 --
select c.id, c.nome
from candidato as c
left join autarquia as a on a.cod = c.cod
where a.designacao = 'Lisboa'

-- Question 2 --
select count(c.*) as quantidade
from candidato as c
join partido as p on p.sigla = c.sigla
where c.votos > 1 and p.nome = 'Partido da Direita'

-- Question 3 --
select p.nome, avg(c.idade) as media
from candidato as c
join partido as p on p.sigla = c.sigla
group by p.nome
order by avg(c.idade) desc, p.nome asc

-- Question 4 --
select p.nome
from candidato as c
join partido as p on p.sigla = c.sigla
group by p.nome
having avg(c.idade) > 45

-- Question 5 --
select a.cod, a.designacao
from autarquia as a
left join candidato as c on c.cod = a.cod 
full join partido as p on p.sigla = c.sigla
where p.nome = 'Partido do Meio' or p.nome is null
group by a.cod
having count(c.*) < 1

-- Question 6 --
select a.designacao, 
count(case when e.votou = 'false' then 1 end) as quantidade
from autarquia as a
left join eleitor as e on e.cod = a.cod
group by a.designacao

-- Question 7 --
select a.designacao
from autarquia as a
left join eleitor as e on e.cod = a.cod
group by a.designacao
having count(e.*) = (
  	select max(num_votes) 
  	from (
      	select count(*) as num_votes
      	from eleitor
      	group by cod
      ) as max_votes
 )

select a.designacao
from autarquia as a
join eleitor as e on e.cod = a.cod
group by a.cod
having count(e.*) = (
	select count(ee.*)
    from autarquia as aa
    join eleitor as ee on ee.cod = aa.cod
    group by aa.cod
  	order by count(ee.*) desc
  	limit 1
)

-- Question 8 --
select a.cod
from autarquia as a
JOIN candidato as c on c.cod = a.cod
where c.sigla = 'PD' 
group by a.cod
having sum(c.votos) > (
  	select sum(cc.votos) from autarquia as aa
	JOIN candidato as cc on cc.cod = aa.cod
  	where cc.sigla != 'PD' and cc.cod = a.cod
  	group by aa.cod
)



