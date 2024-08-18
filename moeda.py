import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

#CRIANDO  VETORES PARA ARMAZENAR A FREQUENCIA ABSOLUTA DE MOEDAS CARA , COROA E A QUANTIDADE TOTAL DE JOGADAS
dados_cara =[]
dados_coroa =[]
jogadas=[]


#LOOP ANINHADO PARA FETERMINAR A FREQUENCIA RELATIVA DO LANÇAMENTO EM CARA E COROA ENTRE LANÇAMENTOS DE INTERVALO 1-10000
for iterator in range (1,10001):

  #SEMPRE QUE INCIAR O LOOP PRINCIPAL A FREQUEUCNIA RELATIVA SERÁ RESETADA PARA ZERO
  fr_cara = 0
  fr_coroa = 0


  print(iterator)


  for i in range(0,iterator):

    #GERAR UM NUMERO ALEATORIO ENTRE 0 E 1
    moeda = random.randrange(0,2)

    #MOEDA == 0 (CARA)
    #MOEDA == 1 (COROA)

    if(moeda == 0):
      fr_cara +=1

    elif(moeda == 1):
      fr_coroa +=1



  #CALCULANDO FREQUENCIA RELATIVA DE CARA E COROA
  fr_coroa =fr_coroa/(iterator)
  fr_cara =fr_cara/(iterator)


  #ADICIONADO A QUANTIDADE DE JOGADA E FREQUENCIA RELATIVA DE CARA E COROA EM VETORES
  jogadas.append(iterator)
  dados_cara.append(fr_cara)
  dados_coroa.append(fr_coroa)


#DEFININDO O ESTILO DO GRAFICO E O SEU TAMANHO
plt.style.use('ggplot')
plt.figure(figsize=(12, 8))

#ADICIONANDO AO GRAFICO AO EIXO X O NUMERO DE JOGADAS E O EIXO Y A FREQUENCIA RELATIVA DE CARA E COROA
plt.plot(jogadas,dados_cara)
plt.plot(jogadas,dados_coroa)

#CRIANDO UMA LINHA HORIZONTAL NO EIXO Y = 0.5

plt.axhline(y=0.5, color='black', linestyle='--')

#DETERMINANDO OS LABELS DO EIXO X E Y
plt.xlabel('NÚMERO DE LANÇAMENTOS')
plt.ylabel("FREQUENCIA RELATIVA")

#ADICIONANDO LEGENDAS AO GRÁFICO
plt.legend(['Cara', 'Coroa' , 'FREQUENCIA RELATIVA TENDENDO À 0.5'])


#SALVANDO O GRÁFICO EM .png
plt.savefig('frequencia_relativa.png')


#Criando um Dataframe que armazena em três colunas(FREQUENCIA CARA , FREQUENCIA COROA , QUANTIDADE DE JOGADADAS)

planilha= pd.DataFrame({'FREQUENCIA CARA ': dados_cara,'FREQUENCIA COROA ':dados_coroa,'QUANTIDADE DE JOGADAS':jogadas})


#EXPORTANDO DATAFRAME PARA UMA PLANILHA .xlsx
planilha.to_excel('planilha.xlsx')


plt.show()






