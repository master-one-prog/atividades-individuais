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