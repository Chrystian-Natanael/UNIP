import random
import string

caracteres_printaveis = ''.join([chr(i) for i in range(32, 127)])

def gerar_caracteres_aleatorios(key):
    seed = sum([ord(char) for char in key])
    random.seed(seed)
    
    lista_misturada = list(caracteres_printaveis)
    random.shuffle(lista_misturada)
    
    return ''.join(lista_misturada)

def gerar_tabela_aleatoria(key):
    lista_misturada = gerar_caracteres_aleatorios(key)
    tamanho_tabela = len(lista_misturada)
    
    tabela = []
    for i in range(tamanho_tabela):
        primeiro_char = lista_misturada[i]
        char_restantes = list(lista_misturada[:i] + lista_misturada[i+1:])
        random.shuffle(char_restantes)
        
        row = primeiro_char + ''.join(char_restantes)
        tabela.append(row)
    
    return tabela

def cifer_tabela(message, key):
    tabela = gerar_tabela_aleatoria(key)
    
    cifer_msn = ""
    for idx, char in enumerate(message):
        chave_char = key[idx % len(key)]
        
        idx_linha = tabela[0].index(chave_char)
        idx_coluna = tabela[0].index(char)
        
        cifer_char = tabela[idx_linha][idx_coluna]
        cifer_msn += cifer_char

    return cifer_msn

def decifer_tabela(cifer_msn, key):
    tabela = gerar_tabela_aleatoria(key)
    
    msn_decif = ""
    for idx, char in enumerate(cifer_msn):
        chave_char = key[idx % len(key)]
        
        idx_coluna = tabela[0].index(chave_char)
        idx_linha = tabela[idx_coluna].index(char)
        
        decifer_char = tabela[0][idx_linha]
        msn_decif += decifer_char

    return msn_decif

def salvar_tabela(key):
    tabela = gerar_tabela_aleatoria(key)
    with open("Tabela_secreta.txt", "w") as file:
        for linha in tabela:
            file.write(linha + "\n")
    print("\033[3;30;47mTabela de criptografia salva em Tabela_secreta.txt!\033[m")

##

def criptor_cesar(msn, key):
    str_final = ""
    for x in msn:
        if x.isalpha():
            char = 26 if x.isupper() else 26
            novo_valor = (ord(x) - ord('A' if x.isupper() else 'a') + key) % char
            novo_char = chr(novo_valor + ord('A' if x.isupper() else 'a'))
            str_final += novo_char
        elif x.isnumeric():
            novo_valor = (int(x) + key) % 10
            novo_char = str(novo_valor)
            str_final += novo_char
        else:
            str_final += x
    return str_final

def descriptor_cesar(msn, key):
    str_final = ""
    for x in msn:
        if x.isalpha():
            char = 26 if x.isupper() else 26
            novo_valor = (ord(x) - ord('A' if x.isupper() else 'a') - key) % char
            novo_char = chr(novo_valor + ord('A' if x.isupper() else 'a'))
            str_final += novo_char
        elif x.isnumeric():
            novo_valor = (int(x) - key) % 10
            novo_char = str(novo_valor)
            str_final += novo_char
        else:
            str_final += x
    return str_final

def gen_password ():
    import random

    let_upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
    let_lower = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    c_esp = '!@#$%&*()[]?/|.+-=_'

    comp = let_upper + let_lower + num + c_esp
    try:
        digit = int(input('\033[3;30;47mDigite o valor que deseja ter no tamanho da sua senha:\033[m\n'))
    except ValueError:
                print("\033[91m\033[1mErro: Numero invalido!\033[0m\n")
                return
    password = "".join(random.sample(comp, digit))

    idx = 0
    arr = []
    arr.append(password)
    print('Sua senha é:\n', password)
    
    while True:
        resp = input('\033[3;30;47mDeseja gerar outra senha? [s / n]\033[m\n')
        n_password = "".join(random.sample(comp, digit))
        
        if resp.lower() == 'n':
            break
        elif resp.lower() == 's':
            print(n_password)
            arr.append(n_password)
            idx += 1
        else:
            print('\033[91m\033[1mresposta invalida\033[0m\n')
    
    print(f'\033[3;30;47mAs senhas que foram geradas são, respectivamente:\033[m\n{arr}\n')
    print(f'\033[3;30;47mVocê gerou um total de {idx + 1} senhas\033[m\n')

def ft_call():
    while True:
        print("\n\n\n\n\033[3;30;47mEscolha uma opção: \033[m\n")
        print("\033[3;30;47m1 - Criptografia de César \033[m\n")
        print("\033[3;30;47m2 - Descriptografia de César \033[m\n")
        print("\033[3;30;47m3 - Gerador de Senhas \033[m\n")
        print("\033[3;30;47m4 - cifra secreta \033[m\n")
        print("\033[3;30;47m5 - decifra secreta \033[m\n")
        print("\033[3;30;47m6 - Tabela de criptografia própria \033[m\n")
        print("\033[3;30;47m0 - Sair \033[m\n")

        option = input("\033[3;30;47mDigite o número da opção desejada:\033[m\n\n")

        if option == '1':
            msn = input("\033[3;30;47mDigite a mensagem a ser criptografada:\033[m\n\n")
            if not msn.strip():
                print("\033[91m\033[1mErro: Mensagem vazia!\033[0m\n")
                return
            try:
                key = int(input("\033[3;30;47mDigite a chave de criptografia (Apenas números):\033[m\n"))
            except ValueError:
                print("\033[91m\033[1mErro: Chave inválida!\033[0m\n")
                return
            try:
                msn_cripto = criptor_cesar(msn, key)
                print("\033[92m\033[1mMensagem criptografada:\n" + msn_cripto + "\033[0m")
            except Exception as e:
                print(f"\033[91m\033[1mErro ao criptografar a mensagem:\n{e}\033[0m")
        elif option == '2':
            msn = input("\033[3;30;47mDigite a mensagem a ser descriptografada:\033[m\n")
            if not msn.strip():
                print("\033[91m\033[1mErro: Mensagem vazia!\033[0m\n")
                return
            try:
                key = int(input("\033[3;30;47mDigite a chave de descriptografia (Apenas números):\033[0m\n"))
            except ValueError:
                print("\033[91m\033[1mErro: Chave inválida!\033[0m\n")
                return
            try:
                msn_descript = descriptor_cesar(msn, key)
                print("\033[92m\033[1mMensagem descriptografada:\n" + msn_descript + "\033[0m")

            except Exception as e:
              print(f"\033[91m\033[1mErro ao criptografar a mensagem:\n{e}\033[0m")
        elif option == '3':
            gen_password()
        elif option == '4':
            msn = input("\033[3;30;47mDigite a mensagem a ser criptografada:\033[0m\n")
            if not msn.strip():
                print("\033[91m\033[1mErro: Mensagem vazia!\033[0m")
                return
            try:
                key = input("\033[3;30;47mDigite a chave de criptografia (Uma string que pode conter letras, números e simbolos especiais):\033[0m\n")
            except ValueError:
                print("\033[91m\033[1mErro: Chave inválida!\033[0m\n")
                return
            try:
                msn_cripto = cifer_tabela(msn, key)
                print("\033[92m\033[1mMensagem criptografada:\n" + msn_cripto + "\033[0m")
            except Exception as e:
                 print(f"\033[91m\033[1mErro ao criptografar a mensagem:\n{e}\033[0m")
        elif option == '5':
            msn = input("\033[3;30;47mDigite a mensagem a ser descriptografada:\033[0m\n")
            if not msn.strip():
                print("\033[91m\033[1mErro: Mensagem vazia!\033[0m\n")
                return
            try:
                key = input("\033[3;30;47mDigite a chave de descriptografia (Uma string que pode conter letras, números e simbolos especiais):\033[0m\n")
            except ValueError:
                print("\033[91m\033[1mErro: Chave inválida!\033[0m\n")
                return
            try:
                msn_descript = decifer_tabela(msn, key)
                print("\033[92m\033[1mMensagem descriptografada:\n" + msn_descript + "\033[0m")
            except Exception as e:
                print(f"\033[91m\033[1mErro ao criptografar a mensagem:\n{e}\033[0m")
        elif option == '6':
            key = input("\033[3;30;47mDigite a chave para gerar a tabela de criptografia (Uma string que pode conter letras, números e simbolos especiais):\033[0m\n")
            if not key.strip():
                print("\033[91m\033[1mErro: Chave vazia!\033[0m")
                return
            salvar_tabela(key)
        elif option == '0':
            print("\033[3;30;47mSaindo do programa.\033[0m\n")
            break
        else:
            print("\033[91m\033[1mOpção inválida. Tente novamente.\033[0m\n")

ft_call()
