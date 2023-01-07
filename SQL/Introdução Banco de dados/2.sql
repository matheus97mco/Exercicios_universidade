#'inserindo Usuarios'
INSERT INTO Usuarios (usuario,nome,dt_cadastro,dt_nascimento,veterinario) VALUES('1000','Alceu Nunes',sysdate,'10/05/1983','1')
INSERT INTO Usuarios (usuario,nome,dt_cadastro,dt_nascimento,veterinario) VALUES('1010','Pedro Costa','11/05/2020','24/05/1995','0')
INSERT INTO Usuarios (usuario,nome,dt_cadastro,dt_nascimento,veterinario) VALUES('1020','Tales Junior',sysdate,'12/12/1972','1')
INSERT INTO Usuarios (usuario,nome,dt_cadastro,dt_nascimento,veterinario) VALUES('1112','Ana Silva','28/01/2021','10/11/2000','1')
INSERT INTO Usuarios (usuario,nome,dt_cadastro,dt_nascimento,veterinario) VALUES('1210','Maria Jose','05/11/2021','03/07/1967','0')
INSERT INTO Usuarios (usuario,nome,dt_cadastro,dt_nascimento,veterinario) VALUES('1314','Gil','07/12/2020','03/07/1990','1')

#'inserindo Consultas'
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('1','1000','100','20/06/2021','nenhuma','0','1010','20/06/2021')
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('2','1020','104','06/10/2020','pulga','0','1010','15/10/2020')
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('3','1112','106','18/03/2022','nenhuma','1','1010','30/03/2022')
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('4','1314','102',sysdate,'nenhuma','0','1210',sysdate)
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('5','1000','105','29/09/2019','nenhuma','1','1210','29/09/2019')
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('6','1020','108','20/04/2021','atropelamento/fratura','0','1010','2
4/04/2021')
INSERT INTO Consultas(consulta,veterinario,animal,dt_consulta,observação,faltou,atendente,dt_cadastro) VALUES('7','1314','101','10/10/2020','nenhuma','1','1210','11/10/2020')

#inserindo Clientes'
INSERT INTO Clientes (cliente,nome,dt_nascimento) VALUES('1','Ludovico','29/04/1978')
INSERT INTO Clientes (cliente,nome,dt_nascimento) VALUES('2','Percival','21/09/1960')
INSERT INTO Clientes (cliente,nome,dt_nascimento) VALUES('3','Matheus','12/11/1997')
INSERT INTO Clientes (cliente,nome,dt_nascimento) VALUES('4','Ana','05/05/1995')
INSERT INTO Clientes (cliente,nome,dt_nascimento) VALUES('5','Carla','23/10/1970')
INSERT INTO Clientes (cliente,nome,dt_nascimento) VALUES('6','Maria','12/12/2002')

#inserindo Animais'
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('100','toto','101','1','10/05/2019')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('101','bilu','201','6','10/05/2019')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('102','rex','110','2','03/11/2015')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('103','luna','105','4','20/02/2017')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('104','bolt','125','3','01/09/2019')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('105','monstrinho','110','5','18/08/2020')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('106','bob','101','6','11/02/2014')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('107','silvia','201','6','10/05/2019')
INSERT INTO Animais (animal,nome,raca,tutor,dt_nascimento) VALUES('108','latinha','000','','')

#'inserindo Racas'
INSERT INTO Racas (raca,nome) VALUES ('101','Labrador')
INSERT INTO Racas (raca,nome) VALUES ('125','Golden')
INSERT INTO Racas (raca,nome) VALUES ('110','Pug')
INSERT INTO Racas (raca,nome) VALUES ('105','Maltes')
INSERT INTO Racas (raca,nome) VALUES ('201','Persa')
INSERT INTO Racas (raca,nome) VALUES ('000','Vira-Lata')
