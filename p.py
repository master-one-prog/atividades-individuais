class Veiculo:
    def mover(self, carga):
        if isinstance(carga, str):
            print(f"Veículo leva {carga}")
        elif isinstance(carga, float):
            print(f"Veículo com {carga} kilos")
        elif isinstance(carga, int) and carga == 1:
            print(f"Veículo com 1 carga")
        else:
            print("Veículo não tem capacidade para esse transporte")

class Caminhao(Veiculo):
    def mover(self, carga):
        if isinstance(carga, str):
            print(f"Caminhão leva {carga}")
        elif isinstance(carga, float):
            print(f"Caminhão com {carga} kilos")
        elif isinstance(carga, int):
            print(f"Caminhão com {carga} cargas")
        

# Programa principal
veiculos = [Veiculo(), Caminhao(), Veiculo(), Caminhao()]
cargas_str = ['alimento', 'areia', 'carga viva', 'mobília']
cargas_float = [10.5, 25.5, 5.2, 32.8]
cargas_int = [1, 3, 5, 10]

for i, v in enumerate(veiculos):
    v.mover(cargas_str[i])
    v.mover(cargas_float[i])
    v.mover(cargas_int[i])
    print("---")