CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS (Todas)

select * from bairro;
select * from cambio;
select * from caracteristica;
select * from categoria;
select * from classificado;
select * from combustivel;
select * from imovel;
select * from imovel_caracteristica;
select * from marca;
select * from modelo;
select * from municipio;
select * from opcional;
select * from tipo;
select * from veiculo;
select * from veiculo_opcional;

CONSULTAS DAS TABELAS COM FILTROS WHERE (Mínimo 3

select * from imovel where vagas_garagem < 2
select * from imovel where quantidade_quartos = 2
select * from imovel
inner join classificado ON imovel.idclassificado = classificado.idclassificado
where valor < 100000

CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS (Mínimo 2)

select * from imovel where vagas_garagem < 2 AND quantidade_quartos = 2
select * from veiculo where ano = 2010 AND quilometragem < 40000  AND quantidade_porta = 4

CONSULTAS QUE USAM OPERADORES LIKE (Mínimo 3)

select * from veiculo
inner join classificado ON veiculo.idclassificado = classificado.idclassificado
where titulo like '%toyota%'

select * from opcional
inner join veiculo_opcional ON opcional.idopcional = veiculo_opcional.idopcional
inner join veiculo ON veiculo_opcional.idveiculo = veiculo.idveiculo
where opcional.nome like '%vidro elétrico%' or opcional.nome like '%trava elétrico%'

select * from veiculo
inner join combustivel ON veiculo.idcombustivel= combustivel.idcombustivel
inner join categoria ON veiculo.idcategoria = categoria.idcategoria
WHERE combustivel.nome LIKE '%Gasolina%' AND categoria.nome LIKE '%Carro%'

ATUALIZAÇÃO E EXCLUSÃO DE DADOS (Mínimo 6)

delete from imovel;
delete from veiculo;
delete from cidade;

update caracteristica set nome = 'Ar condicionado' where nome like '%Ar condicionado%'
update opcional set nome = 'Ar condicionado' where nome like '%ar condicionado%'
update municipio set nome = 'Teste' where idmunicipio = 1


CONSULTAS COM JUNÇÃO E ORDENAÇÃO (Todas Junções)

SELECT * FROM veiculo
INNER JOIN modelo ON veiculo.idmodelo = modelo.idmodelo
INNER JOIN marca ON veiculo.idmarca = marca.idmarca
INNER JOIN combustivel ON veiculo.idcombustivel = combustivel.idcombustivel
INNER JOIN cambio ON veiculo.idcambio = cambio.idcambio
INNER JOIN categoria ON veiculo.idcategoria = categoria.idcategoria
INNER JOIN classificado ON veiculo.idclassificado = classificado.idclassificado
INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
INNER JOIN municipio ON classificado.idbairro = municipio.idmunicipio
LIMIT 10

SELECT * FROM imovel
INNER JOIN tipo ON imovel.idtipo = tipo.idtipo
INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
INNER JOIN municipio ON classificado.idbairro = municipio.idmunicipio
LIMIT 10

select * from opcional
inner join veiculo_opcional ON opcional.idopcional = veiculo_opcional.idopcional
inner join veiculo ON veiculo_opcional.idveiculo = veiculo.idveiculo

select * from caracteristica
inner join imovel_caracteristica ON caracteristica.idcaracteristica = imovel_caracteristica.idcaracteristica
inner join imovel ON imovel_caracteristica.idimovel = imovel.idimovel


CONSULTAS COM GROUP BY (Mínimo 5)

SELECT bairro.nome, count(*) AS total  FROM imovel
INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
GROUP BY bairro.nome

SELECT municipio.nome, count(*) AS total FROM imovel
INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
INNER JOIN municipio ON classificado.idbairro = municipio.idmunicipio
GROUP BY municipio.nome

SELECT classificado.cep, count(*) AS total FROM imovel
INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
GROUP BY classificado.cep


SELECT bairro.nome, AVG(valor) AS total  FROM imovel
INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
where idtipo = 2
GROUP BY bairro.nome

SELECT marca.nome, veiculo.ano, count(*)  FROM veiculo
INNER JOIN classificado ON veiculo.idclassificado = classificado.idclassificado
INNER JOIN marca ON veiculo.idmarca = marca.idmarca
GROUP BY marca.nome, veiculo.ano order by 3 desc


CONSULTAS COM LEFT E RIGHT JOIN (Mínimo 4)

CONSULTAS COM SELF JOIN E VIEW (Todas Possíveis)

SUBCONSULTAS (Mínimo 3)

select * from veiculo where idveiculo IN (select idveiculo from veiculo where quantidade_porta < 5000)

select * from veiculo where idveiculo 
IN (select idveiculo from veiculo where quantidade_porta = 4 and quilometragem > 50000)

select 
(select avg(valor) media from veiculo 
inner join classificado on veiculo.idclassificado = classificado.idclassificado
inner join bairro on classificado.idbairro = bairro.idbairro
where valor <> 0 and ano > 2010 and  bairro.nome like '%Serra%')
,
(select min(valor) menor from veiculo 
inner join classificado on veiculo.idclassificado = classificado.idclassificado
inner join bairro on classificado.idbairro = bairro.idbairro
where valor <> 0 and ano > 2010 and  bairro.nome like '%Serra%')
,
(select max(valor) maior from veiculo 
inner join classificado on veiculo.idclassificado = classificado.idclassificado
inner join bairro on classificado.idbairro = bairro.idbairro
where valor <> 0 and ano > 2010 and  bairro.nome like '%Serra%')


update bairro set nome = 'Sem Bairro' where nome = ''
update cambio set nome = 'Sem Cambio' where nome = ''
update combustivel set nome = 'Sem Combustivel' where nome = ''

