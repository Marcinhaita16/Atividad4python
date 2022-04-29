nome = input("digite seu primeiro nome: ")

primeiraletra = nome[0:1].upper()
restantenome = nome[1:10].lower()

nome = primeiraletra + restantenome  

dia = input("dia do nascimento: ")
mes = input("mes do nascimento: ")
ano = input("ano do nascimento: ")


print("{} nasceu no dia: {}/{}/{}".format(nome, dia, mes, ano))