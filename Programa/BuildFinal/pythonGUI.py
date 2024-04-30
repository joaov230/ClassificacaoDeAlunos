import customtkinter as ctk
import script
import os.path

padxEntry = 5

ctk.set_appearance_mode("light_mode")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x600")
my_font = ctk.CTkFont(family="Berlin Sans FB Demi", size=20, weight="bold")

def warningDeAlgo(strWarning, strSize):
    aux = ctk.CTk()
    aux.geometry(strSize)
    
    frameAux = ctk.CTkFrame(master=aux, fg_color="#fa5032")
    frameAux.pack(pady=20, padx=10, fill="both", expand=True)

    labelWarning = ctk.CTkLabel(master=frameAux, text=strWarning)
    labelWarning.pack(pady=12)

    aux.mainloop()

def SucessoDeAlgo(strSuccess, strSize):
    aux = ctk.CTk()
    aux.geometry(strSize)
    
    frameAux = ctk.CTkFrame(master=aux, fg_color="#8ef56c")
    frameAux.pack(pady=20, padx=10, fill="both", expand=True)

    labelSuccess = ctk.CTkLabel(master=frameAux, text=strSuccess)
    labelSuccess.pack(pady=12)

    aux.mainloop()

def btnRun():
    caminho = f'../../Tabelas Principais/{entryFilename.get()}'
    if (entryFilename.get() == ""):
        warningDeAlgo("Você esqueceu de colocar o nome do arquivo.", "400x90")
    elif (not (entryFilename.get().endswith(".xlsx") or entryFilename.get().endswith(".csv"))):
        warningDeAlgo("Você esqueceu de colocar a extensão .xlsx no final do nome do arquivo.", "500x90")
    elif (not os.path.exists(caminho)):
        warningDeAlgo("Cuidado! Esse arquivo que você escreveu não existe ou não está na pasta correta.", "550x90")
    elif (entryQntAlunos.get() == ""):
        warningDeAlgo("Você esqueceu de colocar a quantidade de alunos por turma.", "500x90")
    elif (not entryQntAlunos.get().isnumeric()):
        warningDeAlgo("Por favor, insira apenas números no campo de quantidade de alunos.", "540x90")
    elif (entryCarimbo.get() == "" or entryNome.get() == "" or entryTurma.get() == "" or entryOpcao1.get() == "" or entryOpcao2.get() == ""):
        warningDeAlgo("Você não preencheu um ou mais nomes das colunas.", "400x90")
    elif ((not entryCarimbo.get().isascii()) or (not entryNome.get().isascii()) or (not entryTurma.get().isascii()) or (not entryOpcao1.get().isascii()) or (not entryOpcao2.get().isascii())):
        warningDeAlgo("Não são permitidos acentos nos nomes das colunas.", "400x90")
    else:
        script.Run_Script(
            filename=caminho,
            quantMaxDeAlunosPorTurma=int(entryQntAlunos.get()),
            cCarimbo=entryCarimbo.get(),
            cNome=entryNome.get(),
            cTurma=entryTurma.get(),
            cOpcao1=entryOpcao1.get(),
            cOpcao2=entryOpcao2.get(),
            cNota=entryNota.get()
        )
        SucessoDeAlgo("As tabelas foram geradas com sucesso, verifique a pasta Oficinas.", "600x90")

# Frame
frame = ctk.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

labelTitle = ctk.CTkLabel(master=frame, text="Configuração de Variáveis", font=my_font)
labelTitle.pack(pady=10, padx=10)

entryFilename = ctk.CTkEntry(master=frame, placeholder_text="Nome do arquivo", width=250)
entryFilename.pack(pady=5, padx=padxEntry)

entryQntAlunos = ctk.CTkEntry(master=frame, placeholder_text="Alunos por turma", width=250)
entryQntAlunos.pack(pady=5, padx=padxEntry)

###### Frame de instruções

labelInstrucoes = ctk.CTkLabel(master=frame, text="INSTRUÇÕES", font=my_font)
labelInstrucoes.pack(pady=1, padx=10)

textbox = ctk.CTkTextbox(master=frame, fg_color="#c3c6c9", wrap="word", border_width=3, height=185, width=300)
textbox.pack(pady=1,padx=8)
textbox.insert("0.0", "Cada caixa de texto abaixo equivale a cada coluna da tabela principal, para cada uma delas você deve copiar o nome da coluna, exatamente como está no arquivo, e colar nas caixas de texto respectivas.\n\nO valor já escrito nelas serão os valores padrões considerados.\n\nNão são permitidos acentos nos nomes das colunas.")
textbox.configure(state="disabled")

###### Interação com o usuário

entryCarimbo = ctk.CTkEntry(master=frame, placeholder_text="DATAEHORA", width=250)
entryCarimbo.pack(pady=5, padx=padxEntry)

entryNome = ctk.CTkEntry(master=frame, placeholder_text="NOME", width=250)
entryNome.pack(pady=5, padx=padxEntry)

entryTurma = ctk.CTkEntry(master=frame, placeholder_text="TURMA", width=250)
entryTurma.pack(pady=5, padx=padxEntry)

entryOpcao1 = ctk.CTkEntry(master=frame, placeholder_text="OPCAO1", width=250)
entryOpcao1.pack(pady=5, padx=padxEntry)

entryOpcao2 = ctk.CTkEntry(master=frame, placeholder_text="OPCAO2", width=250)
entryOpcao2.pack(pady=5, padx=padxEntry)

entryNota = ctk.CTkEntry(master=frame, placeholder_text="NOTA", width=250)
entryNota.pack(pady=5, padx=padxEntry)

button = ctk.CTkButton(master=frame, text="Verificar e rodar programa", command=btnRun)
button.pack(pady=12, padx=10)

root.mainloop()