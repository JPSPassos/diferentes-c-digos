import customtkinter as ctk
from tkinter import messagebox, ttk
import tkinter as tk

class aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
        
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("Cadastro de Alunos")
janela.geometry('700x400')

lista_alunos = []

def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    
    if nome == '' or idade == '':
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return
    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
        return
    
    novo_aluno = aluno(nome, idade)
    lista_alunos.append(novo_aluno)

    tabela.insert('', 'end', values=(novo_aluno.nome, novo_aluno.idade))

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)

frame_form = ctk.CTkFrame(janela)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky='n')

frame_tabela = ctk.CTkFrame(janela)
frame_tabela.grid(row=0, column=1, padx=20, pady=20, sticky='n')

label_titulo = ctk.CTkLabel(frame_form, text="Cadastro de Alunos", font=('Arial', 20))
label_titulo.pack(pady=10)

label_nome = ctk.CTkLabel(frame_form, text="Nome:")
label_nome.pack()
entry_nome = ctk.CTkEntry(frame_form, placeholder_text="Digite o nome")
entry_nome.pack(pady=5)

label_idade = ctk.CTkLabel(frame_form, text="Idade:")
label_idade.pack()
entry_idade = ctk.CTkEntry(frame_form, placeholder_text="Digite a idade")
entry_idade.pack(pady=5)

botao_cadastrar = ctk.CTkButton(frame_form, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=10)

label_lista = ctk.CTkLabel(frame_tabela, text="Lista de Alunos", font=('Arial', 20))
label_lista.pack(pady=10)

tabela = ttk.Treeview(frame_tabela, columns=("Nome", "Idade"), show='headings', height=10)
tabela.heading("Nome", text="Nome")
tabela.heading("Idade", text="Idade")
tabela.pack()

janela.mainloop()