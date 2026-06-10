class Onibus:
    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.moto = nome_motorista
        self.assentos = [False]*num_assentos
    
    def __len__(self):
        return len(self.assentos)

    def __getitem__(self, indice):
        if indice > len(self.assentos) or indice < 0:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        else:
            return self.assentos[indice]  

    def __setitem__(self, indice, valor):
        if indice > len(self.assentos) or indice < 0:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        else:
            if not isinstance(valor, bool):
                raise TypeError(f"Valor deve ser booleano (True/False)")
            
            else:
                # tudo valido
                self.assentos[indice] = valor


onibus = Onibus(231, 'Carlos Eduardo', 10)

print(len(onibus))

onibus[0] = True
onibus[1] = True

print(onibus)