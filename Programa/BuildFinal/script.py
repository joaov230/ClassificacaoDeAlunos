# Import the pandas and datetime module
import pandas as pd
import datetime as dt
import os

########### 
# Sorting function
def Sort_Tuple(tup):
  return(sorted(tup, key = lambda x: (- float(x[4]), x[5]), reverse=False)) 

########
# Reordena com 2 chaves: 1ª é a nota, a 2ª é o carimbo de data
# Considerar a data como parâmetro de desimpate
########

def Verifica_Opcao_Restante(tup):
  if (tup[2] == 'Eletricidade' and tup[3] == 'Mecânica de Usinagem'):
    return 'Metalurgia'
  if(tup[2] == 'Eletricidade' and tup[3] == 'Metalurgia'):
    return 'Mecânica de Usinagem'
  
  if(tup[2] == 'Mecânica de Usinagem' and tup[3] == 'Eletricidade'):
    return 'Metalurgia'
  if(tup[2] == 'Mecânica de Usinagem' and tup[3] == 'Metalurgia'):
    return 'Eletricidade'
  
  if(tup[2] == 'Metalurgia' and tup[3] == 'Eletricidade'):
    return 'Mecânica de Usinagem'
  if(tup[2] == 'Metalurgia' and tup[3] == 'Mecânica de Usinagem'):
    return 'Eletricidade'


##################
# The script itself

def Run_Script(filename, quantMaxDeAlunosPorTurma, cCarimbo='DATAEHORA', cNome="NOME", cTurma="TURMA", cOpcao1="OPCAO1", cOpcao2="OPCAO2", cNota="NOTA"):
  # Load the xlsx file
  excel_data = pd.read_excel(filename)

  # Read the values of the file in the dataframe
  data = pd.DataFrame(excel_data)

  dicionario = {'Eletricidade': list(), 'Mecânica de Usinagem': list(), 'Metalurgia': list()}
  maxPorTurma = quantMaxDeAlunosPorTurma

  dataTup = list()

  for i in range(0, data.__len__()):
    nome = data[cNome][i] # 0
    turma = data[cTurma][i] # 1
    opcao1 = data[cOpcao1][i] # 2
    opcao2 = data[cOpcao2][i] # 3
    media = data[cNota][i] # 4
    if (not isinstance(data[cCarimbo][i], dt.datetime)): # Se não tiver no formato datetime, transforma num
      diaehora = dt.datetime.strptime(data[cCarimbo][i], '%m/%d/%Y %H:%M:%S')
    else:
      diaehora = data[cCarimbo][i] # 5


    dataTup.append((nome,turma,opcao1,opcao2,media,diaehora))

  dataTup = Sort_Tuple(dataTup)

  dataTup2 = []

  for each in dataTup:
    dataTup2.append((each[0],each[1],each[2],each[3],each[4],each[5].strftime('%m/%d/%Y %H:%M:%S')))

  for i in range (0, len(dataTup2)):
    if(len(dicionario[dataTup2[i][2]]) < maxPorTurma): # Vai pra primeira opção
      dicionario[dataTup2[i][2]].append(dataTup2[i])
    elif(len(dicionario[dataTup2[i][3]]) < maxPorTurma): # Vai pra segunda opção
      dicionario[dataTup2[i][3]].append(dataTup2[i])
    elif(len(dicionario[Verifica_Opcao_Restante(dataTup2[i])]) < maxPorTurma): # Vai para a opção restante
      dicionario[Verifica_Opcao_Restante(dataTup2[i])].append(dataTup2[i])
    else: # Suplência da 1ª opção
      dicionario[dataTup2[i][2]].append(dataTup2[i])


  eletricidadeDF = pd.DataFrame(dicionario['Eletricidade'], columns=['NOME', 'TURMA', 'OPCAO1', 'OPCAO2', 'MEDIA', 'DIAEHORA'])
  mecanicaDF = pd.DataFrame(dicionario['Mecânica de Usinagem'], columns=['NOME', 'TURMA', 'OPCAO1', 'OPCAO2', 'MEDIA', 'DIAEHORA'])
  metalurgiaDF = pd.DataFrame(dicionario['Metalurgia'], columns=['NOME', 'TURMA', 'OPCAO1', 'OPCAO2', 'MEDIA', 'DIAEHORA'])

  dirTurma = dataTup[0][1].replace("/","")
  dirTurma = dirTurma.replace("  "," ")
  dirTurma = dirTurma.replace(" ","-")

  if (not os.path.exists('../../Oficinas')):
    os.mkdir('../../Oficinas')

  eletricidadeDF.to_excel(f'../../Oficinas/{dirTurma}-Eletricidade.xlsx', sheet_name='Classificados')
  mecanicaDF.to_excel(f'../../Oficinas/{dirTurma}-MecanicaDeUsinagem.xlsx', sheet_name='Classificados')
  metalurgiaDF.to_excel(f'../../Oficinas/{dirTurma}-Metalurgia.xlsx', sheet_name='Classificados')