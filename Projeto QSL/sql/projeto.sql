CREATE TABLE Materias (
    MateriaID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT,
    CargaHoraria INT NOT NULL
);

SELECT * FROM Materias;

INSERT INTO Materias (Nome, Descricao, CargaHoraria)
VALUES ('Matemática', 'Álgebra e Geometria', 80);

UPDATE Materias 
SET CargaHoraria = 100 
WHERE MateriaID = 1;

DELETE FROM Materias WHERE MateriaID = 1;



CREATE TABLE Professores (
    ProfessorID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Registro VARCHAR(20) UNIQUE NOT NULL,
    CPF VARCHAR(14) UNIQUE NOT NULL,
    Email VARCHAR(100),
    Telefone VARCHAR(20),
    DataContratacao DATE NOT NULL
);

SELECT * FROM Professores;

INSERT INTO Professores (Nome, Registro, CPF, DataContratacao)
VALUES ('João Silva', 'PROF123', '123.456.789-00', '2023-01-15');

UPDATE Professores 
SET Email = 'joao.silva@escola.com' 
WHERE ProfessorID = 1;

DELETE FROM Professores 
WHERE ProfessorID = 1 
AND NOT EXISTS (SELECT 1 FROM ProfessorTurma WHERE ProfessorID = 1);



CREATE TABLE Alunos (
    AlunoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    CPF VARCHAR(14) UNIQUE NOT NULL,
    DataNascimento DATE NOT NULL,
    Email VARCHAR(100),
    Telefone VARCHAR(20),
    Endereco TEXT
);
SELECT * FROM Alunos;

INSERT INTO Alunos (Nome, CPF, DataNascimento)
VALUES ('Maria Oliveira', '987.654.321-00', '2010-05-20');

UPDATE Alunos 
SET Telefone = '(11) 9999-8888' 
WHERE AlunoID = 1;

DELETE FROM Alunos 
WHERE AlunoID = 1 
AND NOT EXISTS (SELECT 1 FROM Matriculas WHERE AlunoID = 1);


CREATE TABLE Turmas (
    TurmaID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL,
    AnoLetivo INT NOT NULL,
    Periodo VARCHAR(20) NOT NULL
);


CREATE TABLE ProfessorTurma (
    ProfessorTurmaID INT PRIMARY KEY AUTO_INCREMENT,
    ProfessorID INT NOT NULL,
    TurmaID INT NOT NULL,
    MateriaID INT NOT NULL,
    FOREIGN KEY (ProfessorID) REFERENCES Professores(ProfessorID),
    FOREIGN KEY (TurmaID) REFERENCES Turmas(TurmaID),
    FOREIGN KEY (MateriaID) REFERENCES Materias(MateriaID),
    UNIQUE (TurmaID, MateriaID) 
);
SELECT * FROM Turmas;

INSERT INTO Turmas (Nome, AnoLetivo, Periodo)
VALUES ('1º Ano A', 2023, 'Manhã');

INSERT INTO ProfessorTurma (ProfessorID, TurmaID, MateriaID)
VALUES (1, 1, 1);

INSERT INTO Matriculas (AlunoID, TurmaID, DataMatricula)
VALUES (1, 1, '2023-02-01');

SELECT 
    t.Nome AS Turma,
    p.Nome AS Professor,
    m.Nome AS Materia,
    GROUP_CONCAT(a.Nome SEPARATOR ', ') AS Alunos
FROM 
    Turmas t
JOIN ProfessorTurma pt ON t.TurmaID = pt.TurmaID
JOIN Professores p ON pt.ProfessorID = p.ProfessorID
JOIN Materias m ON pt.MateriaID = m.MateriaID
LEFT JOIN Matriculas mat ON t.TurmaID = mat.TurmaID
LEFT JOIN Alunos a ON mat.AlunoID = a.AlunoID
GROUP BY t.TurmaID, pt.ProfessorTurmaID;


CREATE TABLE Matriculas (
    MatriculaID INT PRIMARY KEY AUTO_INCREMENT,
    AlunoID INT NOT NULL,
    TurmaID INT NOT NULL,
    DataMatricula DATE NOT NULL,
    FOREIGN KEY (AlunoID) REFERENCES Alunos(AlunoID),
    FOREIGN KEY (TurmaID) REFERENCES Turmas(TurmaID),
    UNIQUE (AlunoID, TurmaID) 
);