# Inicialize contadores para números pares e ímpares

pares = 0

impares = 0

 

# Peça ao usuário para inserir 10 números inteiros

for _ in range(10):

   numero = int(input("Digite um número inteiro: "))

   if numero % 2 == 0:

       pares += 1  # Se o número for par, incremente o contador de pares

   else:

       impares += 1  # Se o número for ímpar, incremente o contador de ímpares

 

# Imprima a quantidade de números pares e ímpares

print(f"Quantidade de números pares: {pares}")

print(f"Quantidade de números ímpares: {impares}")