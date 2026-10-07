use aprendendo_mysql;

-- COUNT
SELECT COUNT(*) AS quantidade FROM clientes;
SELECT COUNT(email) AS emails_cadastrados FROM clientes;

-- SUM
SELECT SUM(idade) AS soma_idades FROM clientes;

-- AVG
SELECT AVG(idade) AS media_idade FROM clientes;

-- MAX
SELECT MAX(idade) AS maior_idade FROM clientes;

-- MIN
SELECT MIN(idade) AS menor_idade FROM clientes;

-- GROUP BY
SELECT cidade_id, COUNT(*) AS quantidade_de_habitantes FROM clientes GROUP BY cidade_id;

-- HAVING
SELECT cidade_id, COUNT(*) AS quantidade_de_habitantes FROM clientes GROUP BY cidade_id HAVING COUNT(*) > 2;