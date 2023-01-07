SELECT Clientes.nome, COUNT(animal) AS Quantidade_Animais FROM Clientes JOIN Animais ON Clientes.cliente = Animais.tutor GROUP BY Clientes.nome
