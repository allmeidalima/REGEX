import re
import unicodedata

#remove acentos e caracteres especiais
def remove_acento(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([letra for letra in nfkd if not unicodedata.combining(letra)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

print(f"{'*' * 26}\n Indentificador de Vogais \n{'*' * 26}")

vogal = ["a","e","i","o","u"]

while True:
    palavra = input("Digite uma palavra: ")
    if palavra == "sair":
        break
    print()
    print(f"{palavra} tem {len(palavra)} letras")
    #conta = palavra.lower()
    resultado = {}

    #a = palavra.find("a")
    #print(a)
    #   for i in vogal:
        #   if i in palavra:
            #   resultado[i] = palavra.count(i)
        
    palavra_sem_acento = remove_acento(palavra).lower()
    
    for l in palavra_sem_acento:
        if l in vogal:
            resultado[l] = palavra_sem_acento.count(l)
            print(f"{l} é uma vogal")
        elif re.search('[0-9]', l):
            print(f'{l} isso é um numero')
        elif re.search('Ç|ç', l):
            print(f'{l} é uma consoante')
        # elif re.search('[^A-z]', l):
            # resultado[l] = palavra.count(l)
            # print(f'{l} é uma vogal')
        else:
            print(f"{l} é uma consoante")
    
    print(resultado)