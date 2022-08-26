import random

print('*****************************************')
print('*** Bem vindo(a) ao adivinhe o número ***')
print('*****************************************\n')

print('Escolha um nível de dificuldade: 1-Fácil 2-Médio 3-Difícil')
nivel_dificuldade = int(input())
#if nivel_dificuldade != 1 or nivel_dificuldade !=2 or nivel_dificuldade !=3 :

print('Valor digitado deve ser 1, 2 ou 3')
if nivel_dificuldade == 1:
    tentativas = 20
elif nivel_dificuldade ==2:
    tentativas = 15
else:
    tentativas = 10

rodada = 0
numero_secreto = random.randrange(0,101)
while(rodada < tentativas):
    rodada += 1
    chute = int(input('Digite um número entre 0 e 100: \n'))
    if chute == numero_secreto:
        print('Parabéns!! Você acertou!')
        break
    else:
        if chute < numero_secreto:
            print('Não foi dessa vez! Tente novamente com um número maior.')
        else:
            print('Não foi dessa vez! Tente novamente com um número menor.')

print(f"O número secreto era {numero_secreto}")
