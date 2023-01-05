1-Criar todas as tabelas no banco de dados Oracle, colocando as restrições conforme especificada. Para a tabela ALUNOS_CURSOS, existe a restrição check para a coluna STATUS, nesta coluna só deve deixar adicionar os seguintes valores:
  A - Aprovado R - Reprovado C – Cursando 

create table Alunos(
    aluno NUMBER(5),
    nome VARCHAR2(50) NOT NULL,
    nascimento DATE NOT NULL,
    cpf NUMBER(11) NOT NULL,
    celular NUMBER(11),
    nome_mae VARCHAR2(50),
    nome_pai VARCHAR2(50) NOT NULL,
    sexo CHAR(1),
    CONSTRAINT aluno_pk PRIMARY KEY(aluno),
    CONSTRAINT cpf_uk UNIQUE(cpf));

create table Alunos_cursos(
    aluno NUMBER(5),
    curso NUMBER(2),
    status char(1),
    CONSTRAINT aluno_curso_pk PRIMARY KEY(aluno,curso),
    CONSTRAINT aluno_fk FOREIGN KEY (aluno) REFERENCES Alunos(aluno),
    CONSTRAINT curso_fk FOREIGN KEY (curso) REFERENCES Cursos(curso),
    CONSTRAINT status_ck CHECK (status = 'A' or status = 'R' or status = 'C'));

create table Docentes(
    docente NUMBER(5),
    nome VARCHAR2(50) NOT NULL,
    cpf NUMBER(11),
    CONSTRAINT docente_pk PRIMARY KEY(docente),
    CONSTRAINT cpf_docente_uk UNIQUE(cpf));

create table Matriculas(
    matricula NUMBER(6),
    cadastro DATE NOT NULL,
    componente NUMBER(3),
    aluno NUMBER(5),
    curso NUMBER(2),
    pontuacao NUMBER(5,2),
    CONSTRAINT matricula_pk PRIMARY KEY(matricula),
    CONSTRAINT componente_fk FOREIGN KEY (componente) REFERENCES Componentes(componente),
    CONSTRAINT aluno_matricula_fk FOREIGN KEY (aluno) REFERENCES Alunos(aluno),
    CONSTRAINT curso_matricula_fk FOREIGN KEY (curso) REFERENCES Cursos(curso));

create table Componentes(
    componente NUMBER(3),
    nome VARCHAR2(30) NOT NULL,
    preco NUMBER(5,2),
    carga_horaria NUMBER(3,1) NOT NULL,
    docente NUMBER(5),
    CONSTRAINT componente_pk PRIMARY KEY(componente),
    CONSTRAINT nome_componente_uk UNIQUE(nome),
    CONSTRAINT docente_fk FOREIGN KEY (docente) REFERENCES Docentes(docente));
    
create table Cursos(
    curso NUMBER(2),
    nome VARCHAR2(20) NOT NULL,
    CONSTRAINT curso_pk PRIMARY KEY(curso),
    CONSTRAINT nome_uk UNIQUE(nome));  
