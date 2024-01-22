# 1 - Crie uma lista para cada informação a seguir:

#     Lista de números de 1 a 10;
#     Lista com quatro nomes;
#     Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Ygor', 'Henrique', 'Pedro', 'Hariel']
ano_nascimento_atual = [2003, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.


def percorre_lista():
    for i in numeros:
        print(f'- {i}\n')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.


def soma_impares():
    soma_impares = 0
    for i in range(1, 11, 2):
        soma_impares += i
    print(soma_impares, '\n')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.


def imprime_decresente():
    for i in range(10, 0, -1):
        print(i, '\n')

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.


def imprime_tabuada():
    numero = int(input('Digite um número para gerar sua tabuada: '))
    for i in range(1, 11):
        resultado = i * numero
        print(f'{numero} x {i} = {resultado}')


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

def soma_lista():
    numeros = [5, 8, 7, 6]
    soma = 0

    try:
        for numero in numeros:
            soma += numero
        print(f'Soma dos elementos: {soma}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


def calcula_media():
    numeros = [15, 20, 25, 30]
    soma = 0
    try:
        for i in numeros:
            soma += i
            media = soma/len(numeros)
        print(f'A média dos numeros da lista {numeros} é {media}')
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def main():
    # percorre_lista()
    # soma_impares()
    # imprime_decresente()
    # imprime_tabuada()
    # soma_lista()
    calcula_media()


if __name__ == "__main__":
    main()
