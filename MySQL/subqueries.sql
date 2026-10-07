use aprendendo_mysql;

-- Clientes que moram em cidades que são de SP usando o UF.
SELECT nome, cidade_id FROM clientes WHERE cidade_id IN (SELECT id FROM cidades WHERE uf = "SP");

-- Clientes que moram em São Paulo.
SELECT nome, cidade_id FROM clientes WHERE cidade_id = (SELECT id FROM cidades WHERE nome = "São Paulo");

-- Clientes que não moram em cidades de SP.
SELECT nome, cidade_id FROM clientes WHERE cidade_id NOT IN (SELECT id FROM cidades WHERE uf = "SP");

-- Clientes mais velhos que o João:
SELECT nome, idade FROM clientes WHERE idade > (SELECT idade FROM clientes WHERE nome = "João Silva");

-- Clientes mais novos que a Maria:
SELECT nome, idade FROM clientes WHERE idade < (SELECT idade FROM clientes WHERE nome = "Maria Santos");

-- Clientes com idade maior ou igual à idade do Beatriz:
SELECT nome, idade FROM clientes WHERE idade >= (SELECT idade FROM clientes WHERE nome = 'Beatriz Ramos');

-- Clientes com idade menor ou igual à idade da Juliana:
SELECT nome, idade FROM clientes WHERE idade <= (SELECT idade FROM clientes WHERE nome = 'Juliana Lima');

-- Verifica se existe pelo menos uma cidade de SP:
SELECT nome FROM clientes WHERE EXISTS (SELECT id FROM cidades WHERE uf = 'SP');