import random

senha = []
contrasenha = []
historico = []
acerto = False

digitos = int(input('Qual será a quantidade de dígitos do código? : '))
for x in range (digitos): 
    senha.append (str(random.randrange(0,9)))

while acerto == False:
    print (f"O código é : {senha}")
    print (f"Histórico: {historico}")
    entrada = input('Digige a sua tentativa: ')
    historico.append(entrada)
    while len(entrada) != digitos:
        print('O código possui {digitos} dígitos! tente novamente')
        entrada = input('Digige a sua tentativa: ')
    contrasenha = list(entrada)
    pts = 0
    for x in range(digitos):
        if senha[x] == contrasenha[x]:
            pts += 1 
        if pts == digitos:
            acerto = True
    msg = f"Você acertou {pts} números!" if acerto != True else "Você acertou o código! Parabéns!!"
    print (msg)
    print (" ")
