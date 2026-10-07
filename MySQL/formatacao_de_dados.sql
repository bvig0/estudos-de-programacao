use aprendendo_mysql;
			/* DADOS TEXTUAIS */
-- CONCAT
SELECT CONCAT(nome, ' - ', email) AS cliente FROM clientes;
SELECT CONCAT('Cliente: ', nome) AS informacao FROM clientes;

-- UPPER
SELECT UPPER(nome) AS NOME_MAIUSCULO FROM clientes;

-- LOWER
SELECT LOWER(nome) AS nome_minusculo FROM clientes;

-- LENGTH
SELECT nome, LENGTH(nome) AS tamanho_do_texto FROM clientes;

-- SUBSTRING
SELECT nome, SUBSTRING(nome, 1, 7) AS parte_nome FROM clientes;

-- TRIM
SELECT TRIM('   João Silva   ') AS nome;
-- Remove espaços dos dois lados
SELECT nome, TRIM(nome) AS nome_corrigido FROM clientes WHERE id IN (16, 19);
-- Remove espaços apenas do lado esquerdo
SELECT nome, LTRIM(nome) AS nome_corrigido FROM clientes WHERE id in (16, 18, 19);
-- Remove espaços apenas do lado direito
SELECT nome, RTRIM(nome) AS nome_corrigido FROM clientes WHERE id IN (16, 17);

-- REPLACE
SELECT nome, REPLACE(nome, 'a', '@') AS nome_bugado FROM clientes;
SELECT nome, REPLACE(nome, 'e', '3') AS nome_bugado FROM clientes;
SELECT nome, REPLACE(nome, 'o', '0') AS nome_bugado FROM clientes;
SELECT nome, REPLACE(nome, '-', ' ') AS nome_bugado FROM clientes;


			/* DADOS NUMÉRICOS */
-- ROUND
SELECT ROUND(15.678, 2) AS valor;
SELECT ROUND(15.678) AS valor_arredondado_para_cima;
SELECT ROUND(15.468) AS valor_arredondado_para_baixo;
SELECT ROUND( 3.14159265358979323846, 2) AS valor_de_pi;

-- CEIL = ARREDONDAR UM NÚMERO PARA CIMA
SELECT CEIL(15.01) AS valor;

-- FLOOR = ARREDONDAR UM NÚMERO PARA BAIXO
SELECT FLOOR(15.90) AS valor;

-- ABS
SELECT ABS(-25) AS valor;

-- MOD
SELECT MOD(10, 3) AS resto;
SELECT MOD(10, 2) AS resto;


			/* DADOS TEMPORAIS */
-- DATE_FORMAT
SELECT DATE_FORMAT(data_nascimento, '%d/%m/%Y') AS nascimento FROM clientes;
SELECT DATE_FORMAT(data_nascimento, '%d/%m/%y') AS nascimento FROM clientes; 
SELECT DATE_FORMAT(data_nascimento, '%m.%d.%Y') AS nascimento FROM clientes;

-- YEAR
SELECT nome, YEAR(data_nascimento) AS ano, data_nascimento FROM clientes;

-- MONTH
SELECT nome, MONTH(data_nascimento) AS mes, data_nascimento FROM clientes;

-- DAY
SELECT nome, DAY(data_nascimento) AS dia, data_nascimento FROM clientes;

-- DATEDIFF
SELECT DATEDIFF('2026-10-01', '2026-09-01') AS dias;
SELECT DATEDIFF('2027-09-02', '2026-09-02') AS dias;

-- DATE_ADD
SELECT DATE_ADD('2026-09-01', INTERVAL 10 DAY) AS nova_data;
SELECT DATE_ADD('2026-09-01', INTERVAL 6 MONTH) AS nova_data;
SELECT DATE_ADD('2026-09-01', INTERVAL 8 YEAR) AS nova_data;
SELECT DATE_ADD(DATE_ADD(DATE_ADD('2026-09-01', INTERVAL 1 YEAR), INTERVAL 1 MONTH), INTERVAL 1 DAY) AS nova_data;

-- DATE_SUB
SELECT DATE_SUB('2026-09-01', INTERVAL 10 DAY) AS nova_data;
SELECT DATE_SUB('2026-09-01', INTERVAL 6 MONTH) AS nova_data;
SELECT DATE_SUB('2026-09-01', INTERVAL 8 YEAR) AS nova_data;
SELECT DATE_SUB(DATE_SUB(DATE_SUB('2026-09-01', INTERVAL 1 YEAR), INTERVAL 1 MONTH), INTERVAL 1 DAY) AS nova_data;
