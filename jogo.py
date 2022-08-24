from random import randrange
print("Digite um número de 0 a 9:",end='\n')

#numero_secreto = randrange(0,9)
numero_secreto = 5
tentativa = 0
while(tentativa < 3):
    tentativa +=1
    chute = int(input("digite seu numero: "))
    if chute == numero_secreto:
        print("Você acertou o número, parabéns!!")
    else:
        if chute > numero_secreto:
            print('Você errou! O numero é menor, tente novamente \n')
        else:
            print('Você errou! O numero é maior, tente novamente \n')
print(f'O numero secreto era {numero_secreto}\n')

