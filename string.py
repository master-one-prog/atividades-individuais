# Questão 1
nome = input("Qual seu nome?")
sobre = input("Qual seu sobrenome? ")
print (f"bem vindo(a), {nome} {sobre}! ")

# Questão 2

frase = input("Digite uma frase")
print(len(" "))

# qst 3

nome3 =  input("Informe o nome: ")

for cont in range(len(nome3)):
    print(nome3[0:cont  + 1])

# qst 4

numero = (input("Informe o numero: "))
if len(numero) == 8:
    print(f"9{numero[:4]}-{numero[4:9]}")

elif len(numero) < 8:
    print("QUANTIDADE INVALIDA")

else:
    if numero[0] == '9':
        print(f"{numero[:5]}-{numero[5:9]}")
    else:
        print("NUMERO INVALIDO")
    

# qst 5
total = 0
indice = []
frase = input("Informe uma frase: ")
for i in range(len(frase)):
    if frase[i] in "aeiou":
        total += 1
        indice.append(i)
print("Numero de letras:",total)
print("indice:",indice)