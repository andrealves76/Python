import random

print('*****************************************')
print('*** Bem vindo(a) ao adivinhe o número ***')
print('*****************************************\n')

print('Escolha um nível de dificuldade: 1-Fácil 2-Médio 3-Difícil')

nivel = 0
pontos = 1000

def retorno():
    nivel = int(input("digite nivel \n"))

    if nivel == 1:
        print('facil')
        pass
    elif nivel == 2:
        print('medio')
        pass
    elif nivel == 3:
        print('dificil')
        pass
    else:
        print('Valor digitado deve ser 1, 2 ou 3')
        return retorno()


retorno()

if nivel == 1:
    tentativas = 20
elif nivel == 2:
    tentativas = 15
else:
    tentativas = 10

rodada = 0
numero_secreto = random.randrange(0, 101)
while (rodada < tentativas):
    rodada += 1
    chute = int(input('Digite um número entre 0 e 100: \n'))
    if chute == numero_secreto:
        print(f'Parabéns!! Você acertou! Sua pontuação é {pontos}')
        break
    else:
        if chute < numero_secreto:
            print('Não foi dessa vez! Tente novamente com um número maior.')
        else:
            print('Não foi dessa vez! Tente novamente com um número menor.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

print(f"O número secreto era {numero_secreto}, sua pontuação final foi {pontos}")
