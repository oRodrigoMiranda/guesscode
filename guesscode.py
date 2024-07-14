senha = ['1','2','3','4']
contrasenha = []
historico = []
acerto = False

while acerto == False:
    print (f"Histórico: {historico}")
    entrada = input('Digige a senha: ')
    historico.append(entrada)
    contrasenha = list(entrada)
    pts = 0
    for x in range(len(contrasenha)):
        if senha[x] == contrasenha[x]:
            pts += 1 
        if pts == 4:
            print ("Você acertou a senha! Parabéns!!!!")
            acerto = True
    print (f"Você acertou {pts} números!")
    print (" ")
    


