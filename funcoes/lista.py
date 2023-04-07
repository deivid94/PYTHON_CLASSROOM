numeros = [10,20,14,13,12,4,7,8,9,14,17,18]

def verifica_idade_dirigir(idade):
    for idade in numeros:
        if idade >= 18:
            print('voce pode dirigir')
        else:
            print('voce nao pode dirigir')    

verifica_idade_dirigir(numeros)