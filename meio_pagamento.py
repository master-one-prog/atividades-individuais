from abc import ABC, abstractmethod

class Meio_de_pagamento(ABC):
    def __init__(self, status):
        self.status = status
    
    @abstractmethod
    def processar_pagamento(self):
        pass
    
    
    @abstractmethod
    def cancelar_pagamento(self):
        pass

    @abstractmethod
    def gerar_comprovante(self):
        pass

class Cartao_de_Credito(Meio_de_pagamento):
    def __init__(self, status, numero_cartao):
        super().__init__(status)

        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        self.status = 'Aprovado'
        print("Pagamento Processado!")

    def cancelar_pagamento(self):
        self.status = 'cancelado'
        print("Pagamento cancelado!")
    
    def gerar_comprovante(self):
        
