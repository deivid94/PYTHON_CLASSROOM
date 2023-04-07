
## comparar valores maior de 18
## verificar se forem true
# tem permisaao para dirigir or not
idades = [13,14,18,24,22,30,11]
permissoes = []

def verifica_idades(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)

verifica_idades(idades, permissoes)                

for permissao in permissoes:
    if permissao == True:
        print('voce tem permissao para dirigir')
    else:
        print('voce nao tem permissao para dirigir')    

