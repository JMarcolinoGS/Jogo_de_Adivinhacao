import random
choice_number = input("Dígite um numero para começarmos!:")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é numerico. Favor execute novamente e informe um numero")
    quit()

random_number = random.randint(0,choice_number)

n_choices = 0

while True:
    answer_user = input("Adivinhe o numero:")
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("digite um numero")
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print("Acertou o número!")
        break

    elif answer_user > random_number:
        print("Chutou alto,tente um número menor")
    else:
        print("O numero é maior que isto")

    print("Nº de tentativas:" + str(n_choices))

