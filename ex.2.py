from unicodedata import normalize
from time import sleep
print("\n")
print("\033[36m="*30)
print("\033[33mO ALUNO ESTA NA TURMA OU NAO?\033[m")
print("\033[36m=\033[m"*30)
turma = ('André', 'Fernanda', 'Luiz')
turmaS = ( )
sleep(0.5)
print("Vamos descobrir \033[31m;)\033[m !!!")

nome = input("Informe o nome de um aluno: ").lower().title().strip()

def remover_acento(nome1):
    return normalize('NFKD', nome1).encode('ASCII', 'ignore').decode('ASCII')


for aluno in turma:
    turmaS += (remover_acento(aluno),)

if nome in turmaS:
    print("\033[33mHmmm\033[m")
    sleep(1)
    print(f'O aluno {nome} \033[33mESTÁ\033[m na turma!')
else:
    print("\033[33mHmmm\033[m")
    sleep(1)
    print(f'O aluno {nome} \033[33mNÃO\033[m esta na turma!')

