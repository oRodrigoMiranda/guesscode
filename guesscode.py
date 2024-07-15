import random

senha = [str(random.randrange(0,9)),str(random.randrange(0,9)),str(random.randrange(0,9)),str(random.randrange(0,9))]
contrasenha = historico = []
#historico = []
acerto = False
while acerto == False:
    print (f"O código é : {senha}")
    print (f"Histórico: {historico}")
    entrada = input('Digige a senha: ')
    historico.append(entrada)
    contrasenha = list(entrada)
    pts = 0
    for x in range(len(contrasenha)):
        if senha[x] == contrasenha[x]:
            pts += 1 
        if pts == 4:
            acerto = True
    msg = f"Você acertou {pts} números!" if pts<4 else "Você acertou o código! Parabéns!!"
    print (msg)
    print (" ")
