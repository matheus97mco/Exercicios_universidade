SELECT nome,dt_nascimento FROM Clientes WHERE TO_CHAR(dt_nascimento,'yyyy') BETWEEN 1980 AND 1998 UNION SELECT nome,dt_nascimento FROM Usuarios WHERE 
TO_CHAR(dt_nascimento,'yyyy') BETWEEN 1980 AND 1998
