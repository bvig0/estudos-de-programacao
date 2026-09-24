CREATE DATABASE aprendendo_mysql;
USE aprendendo_mysql;

-- Criando a tabela de cidades
CREATE TABLE cidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL
);
-- Inserindo cidades
INSERT INTO cidades (nome, uf)
VALUES
('São Paulo', 'SP'),
('Santos', 'SP'),
('Campinas', 'SP'),
('Guarulhos', 'SP'),
('Curitiba', 'PR'),
('Belo Horizonte', 'MG');

-- Criando a tabela de clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT,
    data_nascimento DATE ,
    email VARCHAR(150) UNIQUE,
    cidade_id INT,

    FOREIGN KEY (cidade_id) REFERENCES cidades(id)
);
-- Inserindo clientes
INSERT INTO clientes (nome, idade, data_nascimento, email, cidade_id)
VALUES
('Lúcio Monteiro', 19, '2007-03-15', 'lucio@email.com', 1),
('João Silva', 20, '2006-07-22', 'joao@email.com', 1),
('Maria Santos', 25, '2001-01-10', 'maria@email.com', 2),
('Carlos Oliveira', 18, '2008-11-05', 'carlos@email.com', 3),
('Ana Costa', 30, '1996-04-18', 'ana@email.com', 4),
('Pedro Souza', 22, '2004-09-30', 'pedro@email.com', 5),
('Juliana Lima', 27, '1999-12-12', 'juliana@email.com', 6),
('Lucas Martins', 21, '2005-06-25', 'lucas@email.com', 1),
('Gabriela Rocha', 24, '2002-02-28', 'gabriela@email.com', 3),
('Rafael Almeida', 19, '2007-10-14', 'rafael@email.com', 2);

SELECT * FROM clientes;
SELECT * FROM cidades;
