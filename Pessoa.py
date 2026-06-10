class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"seu nome é {self.nome} e tem {self.altura} de altura"

    def __gt__(self, other):
        return self.altura > other.altura 

    def __lt__(self, other):
        return self.altura < other.altura

    
lista = [] # lista  vazia

qnt = int(input("Quantas pessoas serão adicionadas?"))

for i in range(qnt):
    # dados pessoa i
    nome = input("Nome: ") 
    altura = float(input("Altura (em metros): "))
    
    # criar objeto Pessoa
    pessoa = Pessoa(nome, altura)

    # inclui na lista
    lista.append(pessoa)

    
print(max(lista))
print(min(lista))
for pessoa in sorted(lista):
    print(Pessoa)