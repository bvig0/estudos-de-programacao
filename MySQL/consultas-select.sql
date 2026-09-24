USE aprendendo_mysql;
SELECT * FROM clientes;

-- Clientes com 20 anos
SELECT nome, idade FROM clientes WHERE idade = 20;

-- Clientes com mais de 20 anos
SELECT nome, idade FROM clientes WHERE idade > 20;

-- Cliente com um nome específico
SELECT nome FROM clientes WHERE nome = "Lúcio Monteiro";

-- Pesquisando uma cidade pelo seu nome
SELECT nome FROM cidades WHERE nome = "São Paulo";

-- Pesquisando uma cidade pelo seu nome
SELECT nome, uf FROM cidades WHERE uf = "SP";

-- Clientes entre 18 e 24 anos
SELECT * FROM clientes WHERE idade >= 18 and idade <= 24;

-- Alterando temporariamente o nome da coluna
SELECT nome AS funcionarios FROM clientes;

-- Dando apelidos para várias colunas
SELECT nome AS cliente, cidade_id AS cidade FROM clientes;

-- Dando um apelido para a tabela
SELECT c.nome, c.email FROM clientes AS c;

-- Clientes que têm 18, 19 ou 20 anos
SELECT nome, idade 
FROM clientes 
WHERE idade IN (18, 19, 20);

-- Cidades chamadas São Paulo ou Santos
SELECT nome, uf 
FROM cidades
WHERE nome IN ("São Paulo", "Santos");
 
 -- Clientes com idade entre 18 e 25 anos
 SELECT nome, idade 
 FROM clientes 
 WHERE idade BETWEEN 18 AND 25;
 
 -- Clientes nascidos entre 2000 e 2007
 SELECT nome, data_nascimento 
 FROM clientes 
 WHERE data_nascimento BETWEEN '2000-01-01' and '2007-12-31';
 
 -- Ordenando clientes pela idade em ordem crescente. Do mais novo para o mais velho.
 SELECT nome, idade 
 FROM clientes 
 ORDER BY idade ASC;
 
 -- Ordenando clientes pela idade em ordem decrescente. Do mais velho para o mais novo
SELECT nome, idade
FROM clientes
ORDER BY idade DESC;

-- Ordenando clientes pelo nome em ordem alfabética
SELECT nome, email
FROM clientes
ORDER BY nome ASC;

-- Ordenando primeiro pela idade e depois pelo nome
SELECT nome, idade
FROM clientes
ORDER BY idade ASC, nome ASC;
 
-- Nomes que começam com "L"
SELECT nome 
FROM clientes 
WHERE nome LIKE 'L%';

-- Nomes que terminam com "a"
SELECT nome 
FROM clientes 
WHERE nome LIKE '%a';

-- Nomes que contêm "an"
SELECT nome
FROM clientes
WHERE nome LIKE '%an%';

-- Retorna cada idade apenas uma vez
SELECT DISTINCT idade FROM clientes;

-- Retorna cada cidade_id apenas uma vez
SELECT DISTINCT cidade_id FROM clientes;

-- Retorna cada uf apenas uma vez
SELECT DISTINCT uf FROM cidades;

-- Retorna apenas os 5 primeiros clientes
SELECT * FROM clientes LIMIT 5;

-- Pula os 2 primeiros e retorna os próximos 5
SELECT * FROM clientes LIMIT 5 OFFSET 2;
