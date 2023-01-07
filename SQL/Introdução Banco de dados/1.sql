CREATE TABLE Usuarios(
 usuario NUMBER(6),
 nome VARCHAR2(100),
 dt_cadastro DATE,
 dt_nascimento DATE,
 veterinario NUMBER(1),
 CONSTRAINT usuario_pk PRIMARY KEY(usuario),
 CONSTRAINT veterinario_ck CHECK (veterinario = '0' or veterinario = '1'));
 
CREATE TABLE Consultas(
 consulta NUMBER(6),
 veterinario NUMBER(6),
 animal NUMBER(6),
 dt_consulta DATE,
 observação VARCHAR(1000),
 faltou NUMBER(1),
 atendente NUMBER(6),
 dt_cadastro DATE,
 CONSTRAINT consulta_pk PRIMARY KEY(consulta),
 CONSTRAINT veterinario_fk FOREIGN KEY (veterinario) REFERENCES Usuarios(usuario),
 CONSTRAINT animal_fk FOREIGN KEY (animal) REFERENCES Animais(animal),
 CONSTRAINT atendente_fk FOREIGN KEY (atendente) REFERENCES Usuarios(usuario),
 CONSTRAINT faltou_ck CHECK (faltou = '0' or faltou = '1'));
 
CREATE TABLE Clientes(
 cliente NUMBER(6),
 nome VARCHAR2(100),
 dt_nascimento DATE,
 CONSTRAINT cliente_pk PRIMARY KEY(cliente));
 
CREATE TABLE Animais(
 animal NUMBER(6),
 nome VARCHAR2(100),
 raca NUMBER(3) NOT NULL,
 tutor NUMBER(6),
 dt_nascimento DATE,
 CONSTRAINT animal_pk PRIMARY KEY(animal),
 CONSTRAINT raca_fk FOREIGN KEY(raca) REFERENCES Racas(raca),
 CONSTRAINT tutor_fk FOREiGN KEY(tutor) REFERENCES Clientes(cliente));
 
CREATE TABLE Racas(
 raca NUMBER(3),
 nome VARCHAR2(100),
 CONSTRAINT raca_pk PRIMARY KEY(raca));
