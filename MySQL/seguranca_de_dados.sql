use aprendendo_mysql;

-- CRIAR UM USUÁRIO
CREATE USER 'usuario_teste'@'localhost' IDENTIFIED BY 'senha123';

-- ALTERAR UM USUÁRIO
ALTER USER 'usuario_teste'@'localhost' IDENTIFIED BY 'nova_senha321';

-- REMOVER UM USUÁRIO
DROP USER 'usuario_teste'@'localhost';

-- CONCEDER PERMISSÕES A UM USUÁRIO
GRANT SELECT ON aprendendo_mysql.clientes TO 'usuario_teste'@'localhost';
GRANT SELECT, UPDATE, DELETE ON aprendendo_mysql.clientes TO 'usuario_teste'@'localhost';

-- REMOVER PERMISSÕES DE UM USUÁRIO,
REVOKE DELETE ON aprendendo_mysql.clientes FROM 'usuario_teste'@'localhost';

-- VERIFICAR AS PERMISSÕES DE UM USUÁRIO
SHOW GRANTS FOR 'usuario_teste'@'localhost'