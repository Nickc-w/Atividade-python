catalogo = [
    {'titulo': 'O nome do vento', 'autor': 'Patrick Rothfuss', 'ano': 2009},
    {'titulo': 'A guerra da papoula','autor': 'R.F.Kuang', 'ano': 2018},
    {'titulo': 'O assasino do rei', 'autor': 'Robin Hobb', 'ano': 1996},
    {'titulo': 'O castelo animado', 'autor': 'Diana Wynne Jones', 'ano': 1986}
    ]

print("\033[33m=-\033[m"*20)
print("            BIBLIOTECA NCSC")
print("\033[33m=-\033[m"*20)

while True:
    print('\n')
    print('\033[33m{:=^30}'.format("\033[mMENU\033[33m"))
    print('''\033[mO que deseja fazer ? 
\033[36m[1]\033[m Adicionar livro 
\033[36m[2]\033[m Listar todos os livros
\033[36m[3]\033[m Busca pelo titulo
\033[36m[4]\033[m Sair ''')
    print('\033[33m=\033[m'*22)
    resp = int(input(": "))

    if resp == 4:
        print("\033[36mObrigada, até a proxima!")
        break

    elif resp == 1:
        print("\033[31mClaro!\033[m Informe o.... ")
        titulo = input("\033[31mTitulo: ").lower().strip().capitalize()
        titulo = " ".join(titulo.split())
        autor = input("Autor: ").lower().strip().capitalize()
        autor = " ".join(autor.split())
        ano = int(input("Ano: "))
        dicionario = {'titulo': titulo,'autor': autor,'ano': ano}
        catalogo.append(dicionario)
        print("\033[36mLivro adicionado com sucesso! ")

    elif resp == 2:
        print("\t\t\tLIVROS:")
        for livro in catalogo:
            print('\033[33m-'*30)
            for chave,valor in livro.items():
                print(f' \033[31m{chave}\033[m = {valor}')

    elif resp == 3:
        achei = 0
        busca = input("Claro! Informe o nome do livro que deseja procurar: ").lower().strip().capitalize()
        busca = " ".join(busca.split())
        for livro in catalogo:
            if livro['titulo'] == busca:
                achei+=1
                nome = livro
        if achei == 0:
            print("LIVRO \033[31mNAO\033[m ENCONTRADO")
        else:
            print("LIVRO \033[31mENCONTRADO\033[m!")
            print("\033[33m{:-^30}".format("\033[mDADOS\033[33m"))
            for chave,valor in nome.items():
                print(f"\033[31m{chave}\033[m = {valor}")
            print('\033[33m-' * 30)

    else:
        print("\033[32mOpcao invalida.Tente novamente")
