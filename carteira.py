class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo
    
    def conversao(self, valor_yuan):
        if self.moeda == 'USD':
            return self.saldo * 0.14
        elif self.moeda == 'BRL':
            return self.saldo * 0.85

    def __add__(self, valor_yuan):
        if self.moeda != 'CNY':
            return self.saldo + self.conversao(valor_yuan)
        else:
            return self.saldo + valor_yuan
    def __sub__(self, valor_yuan):
        if self.moeda != 'CNY':
            return self.saldo - self.conversao(valor_yuan)
        else:
            return self.saldo - valor_yuan
    
    def __str__(self):
        return f"Você tem {self.saldo}, {self.moeda}"


carteira_usd = Carteira("USD", 10.0)
print("Soma de carteira_USD + 10 Yuan =", carteira_usd+10.0)
print("Subtração de carteira_USD - 10 Yuan =", carteira_usd-10.0)