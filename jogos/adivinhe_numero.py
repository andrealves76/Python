import random

print('*****************************************')
print('*** Bem vindo(a) ao adivinhe o número ***')
print('*****************************************\n')

print('Escolha um nível de dificuldade: 1-Fácil 2-Médio 3-Difícil')

pontos = 100
rodada = 0
numero_secreto = random.randrange(0, 101)

nivel = int(input("Escolha um  nivel \n"))


if nivel == 1:
    tentativas = 15
elif nivel == 2:
    tentativas = 10
else:
    tentativas = 5

while rodada < tentativas:
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
    print(f"Tentativa {rodada} de {tentativas}")
print(f"O número secreto era {numero_secreto}, sua pontuação final foi {pontos}")
