USE aprendendo_mysql;

-- 1. Mostre o nome e a idade dos clientes que possuem mais de 25 anos.
SELECT nome, idade FROM clientes WHERE idade > 25;

-- 2. Mostre os clientes que têm exatamente 19 anos.
SELECT nome, idade FROM clientes WHERE idade = 19;

-- 3. Mostre os clientes que moram na cidade de ID 1.
SELECT id, nome, cidade_id FROM clientes WHERE cidade_id = 1;

-- 4. Mostre o nome e o email dos clientes que possuem email cadastrado.
SELECT id, nome, email FROM clientes WHERE email IS NOT NULL;

-- 5. Mostre os clientes que têm idade entre 20 e 25 anos.
SELECT nome, idade FROM clientes WHERE idade BETWEEN 20 AND 25;

-- 6. Mostre os clientes cujo nome começa com A.
SELECT nome FROM clientes WHERE nome LIKE "A%";

-- 7. Mostre o nome e a idade dos clientes, ordenando pela idade do menor para o maior.
SELECT nome, idade FROM clientes ORDER BY idade;

-- 8. Mostre o nome e a idade dos clientes, ordenando pela idade do maior para o menor.
SELECT nome, idade FROM clientes ORDER BY idade DESC;

-- 9. Mostre os 5 clientes mais velhos.
SELECT nome, idade FROM clientes ORDER BY idade DESC LIMIT 5;

-- 10. Mostre os clientes que moram nas cidades de ID 1, 2 ou 3.
SELECT id, nome, cidade_id FROM clientes WHERE cidade_id IN (1, 2, 3);

-- 11. Mostre os clientes cujo nome termina com a.
SELECT id, nome FROM clientes WHERE nome LIKE "%a";

-- 12. Mostre os clientes cujo nome contém an.
SELECT id, nome FROM clientes WHERE nome LIKE "%an%";

-- 13. Mostre os clientes que não possuem idade cadastrada.
SELECT id, nome, idade FROM clientes WHERE idade IS NULL;

-- 14. Mostre os clientes que não possuem cidade cadastrada.
SELECT id, nome, cidade_id FROM clientes WHERE cidade_id IS NULL;

-- 15. Mostre o nome e a idade dos clientes com mais de 20 anos, ordenados do mais velho para o mais novo.
SELECT nome, idade FROM clientes WHERE idade > 20 ORDER BY idade DESC;

-- 16. Mostre os 3 clientes mais novos que têm mais de 18 anos.
SELECT nome, idade FROM clientes WHERE idade > 18 ORDER BY idade LIMIT 3;

-- 17. Mostre os clientes das cidades 1 ou 2, ordenados alfabeticamente pelo nome.
SELECT nome, cidade_id FROM clientes WHERE cidade_id IN (1, 2) ORDER BY nome;

-- 18. Mostre os clientes cujo nome começa com J e que têm mais de 18 anos.
SELECT nome, idade FROM clientes WHERE nome LIKE "J%" AND idade > 18;

-- 19. Mostre os clientes que têm entre 18 e 25 anos e ordene pelo nome.
SELECT nome, idade FROM clientes WHERE idade BETWEEN 18 AND 25 ORDER BY nome;

-- 20. Mostre as idades diferentes dos clientes das cidades 1, 2 e 3, sem repetir valores.
SELECT DISTINCT idade FROM clientes WHERE cidade_id IN (1, 2, 3);

-- 21. Mostre os 5 primeiros clientes, ordenados alfabeticamente pelo nome.
SELECT nome FROM clientes ORDER BY nome LIMIT 5;

-- 22. Mostre os clientes que possuem email cadastrado e ordene pelo nome.
SELECT id, nome, email FROM clientes WHERE email IS NOT NULL ORDER BY nome;

-- 23. Mostre o nome, idade e email dos clientes com idade entre 18 e 25 anos, cujo nome contenha a letra a, ordenados do mais velho para o mais novo, mostrando apenas os 5 primeiros.
SELECT nome, idade, email FROM clientes WHERE nome LIKE "%a%" AND idade BETWEEN 18 AND 25 ORDER BY idade DESC LIMIT 5;

-- 24. Mostre os nomes dos clientes que têm idade cadastrada, possuem cidade cadastrada e têm mais de 20 anos.
SELECT nome, idade FROM clientes WHERE idade IS NOT NULL AND cidade_id IS NOT NULL AND idade > 20;

-- 25. Mostre os clientes que não moram nas cidades 1, 2 ou 3.
SELECT nome, cidade_id FROM clientes WHERE cidade_id NOT IN (1, 2, 3);

-- 26. Mostre os clientes cujo nome tenha pelo menos 11 caracteres.
SELECT id, nome FROM clientes WHERE nome LIKE "___________%";

-- 27. Mostre os clientes cujo nome começa com L ou J.
SELECT id, nome FROM clientes WHERE nome LIKE "L%" OR nome LIKE "J%";

-- 28. Mostre os nomes dos clientes com mais de 20 anos que moram nas cidades 2, 3 ou 5 e ordenados alfabeticamente.
SELECT id, nome, idade, cidade_id FROM clientes WHERE idade > 20 AND cidade_id IN (2, 3, 5) ORDER BY nome;