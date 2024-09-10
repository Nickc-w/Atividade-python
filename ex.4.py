print("\n\033[31m{:=^40}".format("\033[33m TURMA \033[m\033[31m"))
notas = [6.3, 7.5, 9.2, 5.1, 6.8]
cont = 0
print(f'\033[mMedia: \033[34m{sum(notas)/len(notas):.2f}')
print(f'\033[mNotas: \033[34m{notas}')


for i in range (0,len(notas)):
    if notas[i] > 6:
        cont+=1

print(f'\033[mNotas acima da media(6): \033[34m{cont}')
print("\033[31m="*27)
