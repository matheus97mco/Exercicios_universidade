SELECT nome, COUNT(faltou) AS Quantidade_consultas_em_2021 FROM Consultas JOIN Usuarios ON Consultas.veterinario = Usuarios.usuario GROUP BY 
nome, dt_consulta, faltou HAVING TO_CHAR(dt_consulta,'yyyy') = 2021 AND FALTOU = 0
