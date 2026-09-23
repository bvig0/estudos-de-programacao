CREATE DATABASE aprendendo_mysql;
USE aprendendo_mysql;

-- Criando uma Tabela
CREATE TABLE clientes (
    id int primary key auto_increment,
    nome varchar(100),
    idade int,
    email varchar(100)
);

CREATE TABLE teste_deletar (
    id int primary key auto_increment,
    nome varchar(100) not null,
    idade int,
    email varchar(100) unique
);

-- Deletando uma Tabela INTEIRA
DROP TABLE teste_deletar;

-- Inserindo vários registros na Tabela
INSERT INTO clientes(nome, idade, email) 
VALUES 
("Teste1", 1700, "teste1@email.com"),
("Teste2", 22, "teste2@email.com"),
("Teste3", 35, "teste3@email.com");

-- Inserindo apenas um registro na Tabela
INSERT INTO clientes(nome, idade, email)  VALUES ("Teste4", 47, "teste4@email.com");

-- Mostrando todos os dados da Tabela
SELECT * FROM clientes;

-- Mostrando apenas algumas colunas
SELECT nome, email FROM clientes;

-- Alterando a idade do cliente
UPDATE Clientes SET idade = 20 WHERE id = 1;

-- Sem o WHERE, todos os registros da coluna idade são alterados para 20, veja no exemplo abaixo
UPDATE Clientes SET idade = 20;

-- Deletando um registro
DELETE FROM Clientes WHERE id = 4;

/* Isso remove apenas o cliente cujo `id` seja `4`. Sem WHERE:
```sql
DELETE FROM Clientes;
```
Isso remove todos os registros da tabela. A tabela continua existindo, mas fica vazia. */

-- Adicionando varias colunas
ALTER TABLE clientes 
ADD cpf varchar(10) unique, ADD cia varchar(100);

-- Removendo uma coluna
ALTER TABLE clientes
DROP COLUMN cia;

-- Alterando o tipo da coluna
ALTER TABLE clientes
MODIFY nome varchar(200);