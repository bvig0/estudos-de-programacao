# Exercícios de Consulta SQL

Exercícios usando a tabela `clientes`, sem utilizar `JOIN`.

## 🟢 Básicos

**1.** Mostre o nome e a idade dos clientes que possuem mais de 25 anos.

**2.** Mostre os clientes que têm exatamente 19 anos.

**3.** Mostre os clientes que moram na cidade de ID `1`.

**4.** Mostre o nome e o email dos clientes que possuem email cadastrado.

**5.** Mostre os clientes que têm idade entre 20 e 25 anos.

**6.** Mostre os clientes cujo nome começa com `A`.

## 🟡 Intermediários

**7.** Mostre o nome e a idade dos clientes, ordenando pela idade do menor para o maior.

**8.** Mostre o nome e a idade dos clientes, ordenando pela idade do maior para o menor.

**9.** Mostre os 5 clientes mais velhos.

**10.** Mostre os clientes que moram nas cidades de ID `1`, `2` ou `3`.

**11.** Mostre os clientes cujo nome termina com `a`.

**12.** Mostre os clientes cujo nome contém `an`.

**13.** Mostre os clientes que não possuem idade cadastrada.

**14.** Mostre os clientes que não possuem cidade cadastrada.

## 🟠 Misturando cláusulas

**15.** Mostre o nome e a idade dos clientes com mais de 20 anos, ordenados do mais velho para o mais novo.

**16.** Mostre os 3 clientes mais novos que têm mais de 18 anos.

**17.** Mostre os clientes das cidades `1` ou `2`, ordenados alfabeticamente pelo nome.

**18.** Mostre os clientes cujo nome começa com `J` e que têm mais de 18 anos.

**19.** Mostre os clientes que têm entre 18 e 25 anos e ordene pelo nome.

**20.** Mostre apenas os nomes dos clientes das cidades `1`, `2` e `3`, sem repetir nomes.

**21.** Mostre os 5 primeiros clientes, ordenados alfabeticamente pelo nome.

**22.** Mostre os clientes que possuem email cadastrado e ordene pelo nome.

## 🔴 Desafio

**23.** Mostre o nome, idade e email dos clientes com idade entre 18 e 25 anos, cujo nome contenha a letra `a`, ordenados do mais velho para o mais novo, mostrando apenas os 5 primeiros.

**24.** Mostre os nomes dos clientes que têm idade cadastrada, possuem cidade cadastrada e têm mais de 20 anos.

**25.** Mostre os clientes que não moram nas cidades `1`, `2` ou `3`.

**26.** Mostre os clientes cujo nome tenha exatamente 5 letras.

**27.** Mostre os clientes cujo nome começa com `M` ou `C`.

**28.** Mostre os nomes dos clientes com mais de 20 anos que moram nas cidades `2`, `3` ou `5`, ordenados alfabeticamente e limitados aos 3 primeiros.

## 📌 Regras

Tente resolver usando apenas:

`SELECT`, `FROM`, `WHERE`, `AS`, `IN`, `BETWEEN`, `LIKE`, `DISTINCT`, `ORDER BY` e `LIMIT`.

**Não utilize `JOIN`.**