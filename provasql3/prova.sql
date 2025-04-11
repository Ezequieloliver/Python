CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY AUTO_INCREMENT, 
    ProdutoID INT NOT NULL,                   
    FornecedorID INT NOT NULL,                
    Quantidade INT NOT NULL,                 
    DataEntrada DATE NOT NULL,                

    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);
