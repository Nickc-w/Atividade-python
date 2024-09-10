from time import sleep

print("\n")
print("\033[33m="*20)
print("\033[36m  PAR OU IMPAR??\033[m")
print("\033[33m=\033[m"*20)
sleep(0.5)
print("Vamos descobrir \033[31m;)\033[m !!")

numero = int(input("Informe o numero: "))

if numero%2 == 0:
    print(f"O numero {numero} é \033[31mPAR\033[m!")
else:
    print(f"O numero {numero} é \033[31mIMPAR\033[m!")