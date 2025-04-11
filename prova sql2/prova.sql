CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL
);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES 
    (1, 'Notebook Dell Inspiron', 15, 4299.90),
    (2, 'Smartphone Samsung Galaxy S23', 32, 3899.00),
    (3, 'Tablet Apple iPad Pro', 8, 5999.99);