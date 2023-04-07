idade = 14

def verify_age(idade):
    if idade >= 18:
        print ('maior idade')
    else:
        print('Nao tem idade')
verify_age(idade)    


def verify_age_no_params():
    age = input('qual sua idade ?')
    age = int(age)
    if age >= 18:
        print('Ja pode dirigir')
    else:
        print('Nao pode dirigir')    

verify_age_no_params()
