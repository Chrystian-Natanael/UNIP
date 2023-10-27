'''
Boa noite!

O projeto mostrado a seguir é um exemplo desenvolvido por nós utilizando a Criptografia de César. 

 Muito conhecida por sua simplicidade, possui este nome, segundo o escritor Suetônio,
 por ter sido usada por Júlio César para se comunicar com seus generais, escondendo as mensagens. 
 Sendo assim uma das primeiras formas de criptografia usadas na história.

 Os comentários serão simples e obejtivos, com o intuito de explicar de uma forma mais confortável e
didática para os iniciantes.

Cada explicação será composta por uma string de comentário, seguindo a ordem a qual cada função, variaveis, 
métodos, serão criados ao decorrer do código do projeto.


'''

# Função para criptografar uma mensagem usando a cifra de César.
def criptor_cesar(msn, key):
    # Inicializa a string final.
    str_final = ""
    # Percorre cada caractere na mensagem.
    for x in msn:
        # Verifica se o caractere é uma letra.
        if x.isalpha():
            # Define o deslocamento com base em se a letra é maiúscula ou minúscula.
            shift = 26 if x.isupper() else 26
            # Calcula o novo valor do caractere após a aplicação da chave.
            new_value = (ord(x) - ord('A' if x.isupper() else 'a') + key) % shift
            # Converte o novo valor para um caractere.
            new_char = chr(new_value + ord('A' if x.isupper() else 'a'))
            # Adiciona o novo caractere à string final.
            str_final += new_char
        # Verifica se o caractere é um número.
        elif x.isnumeric():
            # Calcula o novo valor do número após a aplicação da chave.
            new_value = (int(x) + key) % 10
            # Converte o novo valor para uma string.
            new_char = str(new_value)
            # Adiciona o novo caractere à string final.
            str_final += new_char
        else:
            # Se o caractere não for uma letra nem um número, ele é adicionado à string final sem alterações.
            str_final += x
    # Retorna a string final após todas as transformações.
    return str_final

# Função para descriptografar uma mensagem usando a cifra de César.
def descriptor_cesar(msn, key):
    # Inicializa a string final.
    str_final = ""
    # Percorre cada caractere na mensagem.
    for x in msn:
        # Verifica se o caractere é uma letra.
        if x.isalpha():
            # Define o deslocamento com base em se a letra é maiúscula ou minúscula.
            shift = 26 if x.isupper() else 26
            # Calcula o novo valor do caractere após a aplicação da chave.
            new_value = (ord(x) - ord('A' if x.isupper() else 'a') - key) % shift
            # Converte o novo valor para um caractere.
            new_char = chr(new_value + ord('A' if x.isupper() else 'a'))
            # Adiciona o novo caractere à string final.
            str_final += new_char
        # Verifica se o caractere é um número.
        elif x.isnumeric():
            # Calcula o novo valor do número após a aplicação da chave.
            new_value = (int(x) - key) % 10
            # Converte o novo valor para uma string.
            new_char = str(new_value)
            # Adiciona o novo caractere à string final.
            str_final += new_char
        else:
            # Se o caractere não for uma letra nem um número, ele é adicionado à string final sem alterações.
            str_final += x
    # Retorna a string final após todas as transformações.
    return str_final

# Função para gerar uma senha aleatória com letras maiúsculas, minúsculas, números e caracteres especiais.
def gen_password ():
    import random

    let_upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
    let_lower = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    c_esp = '!@#$%&*()[]?/|.+-=_'

    comp = let_upper + let_lower + num + c_esp
    digit = int(input('Digite o valor que deseja ter no tamanho da sua senha: '))

    password = "".join(random.sample(comp, digit))

    idx = 0
    arr = []
    arr.append(password)
    print('Sua senha é: \n', password)
    
    while True:
        resp = input('Deseja gerar outra senha? [s / n] ')
        n_password = "".join(random.sample(comp, digit))
        
        if resp.lower() == 'n':
            break
        elif resp.lower() == 's':
            print(n_password)
            arr.append(n_password)
            idx += 1
        else:
            print('resposta invalida')
    
    print(f'As senhas que foram geradas são, respectivamente: {arr}')
    print(f'Você gerou um total de {idx + 1} senhas')

# Função para apresentar um menu para o usuário escolher entre criptografia, descriptografia e geração de senha.

def ft_call():
    while True:
        print("Escolha uma opção:")
        print("1 - Criptografia de César")
        print("2 - Descriptografia de César")
        print("3 - Gerador de Senhas")
        print("0 - Sair")

        option = input("Digite o número da opção desejada: ")

        if option == '1':
            msn = input("Digite a mensagem a ser criptografada: ")
            key = int(input("Digite a chave de criptografia: "))
            msn_cripto = criptor_cesar(msn, key)
            print("Mensagem criptografada:", msn_cripto)
        elif option == '2':
            msn = input("Digite a mensagem a ser descriptografada: ")
            key = int(input("Digite a chave de descriptografia: "))
            msn_descript = descriptor_cesar(msn, key)
            print("Mensagem descriptografada:", msn_descript)
        elif option == '3':
            gen_password()
        elif option == '0':
            print("Saindo do programa.")
        else:
            print("Opção inválida. Tente novamente.")

ft_call()