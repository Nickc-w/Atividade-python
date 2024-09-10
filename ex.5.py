from random import choice
from time import sleep

print("\033[33m=\033[m"*30)
print("PEDRA....PAPEL....E TESOURA!!!")
print("\033[33m=\033[m"*30)
print("Vamos começar \033[31m;)\033[m ")
sleep(1)

escolhas = ('pedra','papel','tesoura')
print('''Escolha uma opçao :
         [\033[34mpedra\033[m]
         [\033[34mpapel\033[m]
         [\033[34mtesoura\033[m]''')

empat = venci = compv = 0


while True:
    comp = choice(escolhas)
    print("\033[33mPEDRA....")
    sleep(1)
    print("PAPEL....")
    sleep(1)
    print("E TESOURA!\033[m")
    opcao = input("Opcao: ").lower().strip()
    while opcao not in escolhas:
        opcao = input("inválido.Tente novamente: ").lower().strip()

    print(f'Computador escolheu: {comp}')

    if comp == opcao:
        print("\033[36mEMPATE\033[m\n")
        empat +=1
    elif ((opcao == 'pedra' and comp == 'tesoura') or
        (opcao == 'tesoura' and comp == 'papel') or
        (opcao == 'papel' and comp == 'pedra')):
        print("\033[35mVOCE VENCEU!\033[m\n")
        venci+=1
    else:
        print("\033[31mVOCE PERDEU!\033[m\n")
        compv+=1

    resp = input('Quer continuar?[S/N] ').upper().strip()
    while resp not in 'SN':
        resp = input('Opcao invalida.Quer continuar?[S/N] ').upper().strip()
    if resp == 'N':
        break

print("\033[33m-\033[m"*30)
print("RESULTADO")
print("\033[33m-\033[m"*30)
print(f"Vitorias suas: \033[35m{venci}\033[m ")
print(f"Vitorias do comp: \033[31m{compv}\033[m")
print(f"Empates: \033[36m{empat}")






