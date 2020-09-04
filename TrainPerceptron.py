import pandas
import random
dados=pandas.read_csv("dados_2D_reta.csv") 
w1=random.random()
w2=random.random()#pesos sinapticos aleatorios
erro=1 #erro é iniciado como 1 para entrar no loop
while(erro!=0):
    for i in range(70): #treina só parte dos dados 
        u=(dados.loc[i,"x"]*w1)+(dados.loc[i,"y"]*w2)-1 #produto interno "x" e "y" são as colunas 
        if(u>0):# função que transforma os resultados em 1 e -1
            u=1
        else:
            u=-1
        if(dados.loc[i,"classificacao"]!=u):
            w1=w1+0.1*(dados.loc[i,"classificacao"]-u)*dados.loc[i,"x"]
            w2=w2+0.1*(dados.loc[i,"classificacao"]-u)*dados.loc[i,"y"]
            erro= erro+1
        else:
            erro=0
              
        pass
print(w1,w2)
for i in range(200): #a partir daqui os pesos são testados 
    u=((dados.loc[i,"x"]*w1)+(dados.loc[i,"y"]*w2))-1
    if(u>0):
        u=1
    else:
        u=-1
    if(u!=dados.loc[i,"classificacao"]):
        erro=erro+1 #quantidade de erros depois do perceptron 
print(erro)






