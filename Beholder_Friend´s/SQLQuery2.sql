Use BD_BF

CREATE TABLE Usuarios 
(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Nome VARCHAR(10),
    Senha VARCHAR(20),
    Email VARCHAR(50)
);

CREATE TABLE Personagens
(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    NomePersonagem VARCHAR(50),
    Raca VARCHAR(50),
    Classe VARCHAR(50),
    Nivel INT,
    Divindade VARCHAR(50),
    UsuarioID INT,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(ID)
);

