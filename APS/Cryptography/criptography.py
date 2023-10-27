import random
import string

printable_chars = ''.join([chr(i) for i in range(32, 127)])

def generate_shuffled_characters(key):
    seed_value = sum([ord(char) for char in key])
    random.seed(seed_value)
    
    shuffled_chars = list(printable_chars)
    random.shuffle(shuffled_chars)
    
    return ''.join(shuffled_chars)

def generate_fully_shuffled_matrix(key):
    shuffled_chars = generate_shuffled_characters(key)
    matrix_size = len(shuffled_chars)
    
    matrix = []
    for i in range(matrix_size):
        first_char = shuffled_chars[i]
        remaining_chars = list(shuffled_chars[:i] + shuffled_chars[i+1:])
        random.shuffle(remaining_chars)
        
        row = first_char + ''.join(remaining_chars)
        matrix.append(row)
    
    return matrix

def cipher_with_fixed_matrix(message, key):
    matrix = generate_fully_shuffled_matrix(key)
    
    ciphered_message = ""
    for idx, char in enumerate(message):
        key_char = key[idx % len(key)]
        
        row_idx = matrix[0].index(key_char)
        col_idx = matrix[0].index(char)
        
        ciphered_char = matrix[row_idx][col_idx]
        ciphered_message += ciphered_char

    return ciphered_message

def decipher_with_fixed_matrix(ciphered_message, key):
    matrix = generate_fully_shuffled_matrix(key)
    
    deciphered_message = ""
    for idx, char in enumerate(ciphered_message):
        key_char = key[idx % len(key)]
        
        col_idx = matrix[0].index(key_char)
        row_idx = matrix[col_idx].index(char)
        
        deciphered_char = matrix[0][row_idx]
        deciphered_message += deciphered_char

    return deciphered_message

def save_secret_table_to_file(key):
    matrix = generate_fully_shuffled_matrix(key)
    with open("secret_table.txt", "w") as file:
        for row in matrix:
            file.write(row + "\n")
    print("\033[3;30;47mTabela de criptografia salva em secret_table.txt!\033[m")

##

def criptor_cesar(msn, key):
    str_final = ""
    for x in msn:
        if x.isalpha():
            shift = 26 if x.isupper() else 26
            new_value = (ord(x) - ord('A' if x.isupper() else 'a') + key) % shift
            new_char = chr(new_value + ord('A' if x.isupper() else 'a'))
            str_final += new_char
        elif x.isnumeric():
            new_value = (int(x) + key) % 10
            new_char = str(new_value)
            str_final += new_char
        else:
            str_final += x
    return str_final

def descriptor_cesar(msn, key):
    str_final = ""
    for x in msn:
        if x.isalpha():
            shift = 26 if x.isupper() else 26
            new_value = (ord(x) - ord('A' if x.isupper() else 'a') - key) % shift
            new_char = chr(new_value + ord('A' if x.isupper() else 'a'))
            str_final += new_char
        elif x.isnumeric():
            new_value = (int(x) - key) % 10
            new_char = str(new_value)
            str_final += new_char
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
                msn_cripto = cipher_with_fixed_matrix(msn, key)
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
                msn_descript = decipher_with_fixed_matrix(msn, key)
                print("\033[92m\033[1mMensagem descriptografada:\n" + msn_descript + "\033[0m")
            except Exception as e:
                print(f"\033[91m\033[1mErro ao criptografar a mensagem:\n{e}\033[0m")
        elif option == '6':
            key = input("\033[3;30;47mDigite a chave para gerar a tabela de criptografia (Uma string que pode conter letras, números e simbolos especiais):\033[0m\n")
            if not key.strip():
                print("\033[91m\033[1mErro: Chave vazia!\033[0m")
                return
            save_secret_table_to_file(key)
        elif option == '0':
            print("\033[3;30;47mSaindo do programa.\033[0m\n")
            break
        else:
            print("\033[91m\033[1mOpção inválida. Tente novamente.\033[0m\n")

ft_call()
