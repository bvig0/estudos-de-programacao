USE aprendendo_mysql;
SELECT * FROM clientes;
SELECT * FROM cidades;

-- Mostra os clientes e as cidades ligadas a eles, mas apenas os que tiverem ligação
SELECT clientes.nome, cidades.nome FROM clientes INNER JOIN cidades ON clientes.cidade_id = cidades.id;

-- Mostrando o nome do cliente e o nome da cidade onde ele mora com apelido nas colunas
SELECT clientes.id, clientes.nome AS clientes, cidades.nome AS cidades FROM clientes INNER JOIN cidades ON clientes.cidade_id = cidades.id;

SELECT clientes.nome AS clientes, clientes.data_nascimento, cidades.nome AS cidades, cidades.uf 
FROM  cidades
INNER JOIN clientes 
ON clientes.cidade_id = cidades.id;

/* Mostra os clientes e as cidades ligadas a eles independente se tiver ou não uma ligação  com a cidade.
Caso o cliente não tenha cidade ligado a ele, vai aparecer 'NULL' no nome da cidade */
SELECT clientes.nome AS cliente, cidades.nome AS cidade FROM clientes LEFT JOIN cidades ON clientes.cidade_id = cidades.id;


/* Mostra cidades ligadas aos clientes independente se tiver ou não uma ligação  com o cliente.
Caso o cidade não tenha um cliente ligado a ela, vai aparecer 'NULL' no nome da cliente */
SELECT clientes.nome AS cliente, cidades.nome AS cidade, cidades.uf FROM clientes RIGHT JOIN cidades ON clientes.cidade_id = cidades.id;

-- Mostrando todos os clientes e todas as cidades, mesmo sem correspondência
SELECT clientes.nome AS cliente, cidades.nome AS cidade, cidades.uf FROM clientes LEFT JOIN cidades ON clientes.cidade_id = cidades.id
UNION
SELECT clientes.nome cliente, cidades.nome, cidades.uf FROM clientes RIGHT JOIN cidades ON clientes.cidade_id = cidades.id;

-- Combinando cada cliente com cada cidade
SELECT clientes.nome AS cliente, cidades.nome AS cidade, cidades.uf FROM clientes CROSS JOIN cidades;

-- Comparando clientes que moram na mesma cidade
SELECT c1.id, c1.nome AS cliente01, c2.nome AS cliente02 
FROM clientes c1 
INNER JOIN clientes c2 
ON c1.cidade_id = c2.cidade_id 
WHERE c1.id <> c2.id;