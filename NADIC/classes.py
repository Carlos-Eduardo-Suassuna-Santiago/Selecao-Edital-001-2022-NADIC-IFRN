class Candidato():
    def __init__(self,nome,cpf_candidato,data_nascimento,endereco,numero_candidato):
        self.nome = nome
        self.cpf_candidato = cpf_candidato
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.numero_candidato = numero_candidato
        
    def __str__(self) -> str:
        ficha = ("Nome: {}\nCPF: {}\nData de nascimento: {}\nEndereço: {}\nNumero do candidato: {}".format(self.nome,self.cpf_candidato,self.data_nascimento,self.endereco,self.numero_candidato))
        return str(ficha)

#def votacao():
    
    
c1 = Candidato('Fulano',111222333,'01/05/1994','Rua do sol, bairro esperança',1)
c2 = Candidato('Ciclano',222333444,'01/05/1994','Avenida da esperança, bairro das capivaras',2)
c3 = Candidato('Beltrano',333444555,'01/05/1994','Rua projetada, bairro Joao XXVIII',3)