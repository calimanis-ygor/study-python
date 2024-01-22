import os


def finalizar_app():
    os.system('cls')  # no mac e linux 'clear'
    print('Encerrando a aplicação\n')


# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def par_impar():
    number = int(input('Digite um número:'))
    if number % 2 == 0:
        print(f'O número {number} é par')
    else:
        print(f'O número {number} é impar')


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

def classifica_idade():
    idade = int(input('Digite sua idade: '))
    if 0 < idade <= 12:
        print('Criança')
    elif 12 < idade <= 18:
        print('Adolescente')
    elif idade > 18:
        print('Adulto')
    else:
        print('Valor inválido')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def login_senha():
   usuario_correto = 'ygor'
   senha_correta = '1234'
   usuario = input('Digite seu usuário: ')
   senha = input('Digite sua senha: ')

   if usuario == usuario_correto and senha == senha_correta:
       print('Bem vindo Ygor!')
   else:
       print('Usuário ou senha incorretos!')    

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.
       
def determina_quadrante():
    print('Digite as coordenadas (x,y) de um ponto\n')
    x = int(input('Digite a coordenada x: '))
    y = int(input('Digite a coordenada y: '))

    if x > 0  and y > 0:
        print('O ponto está no primeiro quadrante')
    elif x < 0 and y > 0:
        print('O ponto está no segundo quadrante')
    elif x < 0 and y < 0:
        print('O ponto está no terceiro quadrante')
    elif x > 0 and y < 0:
        print('O ponto está no segundo quadrante')
    else:
        print('O ponto está localizado no eixo ou origem.')

def escolhe_opcao():
    while True:
        print(
            '1. Par ou impar',
            '2. Classifica idade',
            '3. Login e senha',
            '4. Determinar quadrante',
            '5. Encerrar aplicação',
            sep='\n',
        )
        opcao_escolhida = int(input('Escholha uma opção: '))
        match opcao_escolhida:
            case 1:
                par_impar()
            case 2:
                classifica_idade()
            case 3:
                login_senha()
            case 4:
                determina_quadrante()
            case 5:
                finalizar_app()
                break


def main():
    escolhe_opcao()


if __name__ == '__main__':
    main()
