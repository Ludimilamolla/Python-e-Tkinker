import tkinter as tk

# Função - add tarefa na lista
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

# Função - excluir tarefa 
def excluir_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        indice = selecao[0]
        lista_tarefas.delete(indice)

# Janela principal
janela = tk.Tk()
janela.title("Lista de Tarefas")

# Cria caixa de add tarefas
entrada_tarefa = tk.Entry(janela, width=30)
entrada_tarefa.grid(row=0, column=0, padx=10, pady=10)

# Botão add tarefas
botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_tarefa)
botao_adicionar.grid(row=0, column=1, padx=10, pady=10)

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, width=40, height=10)
lista_tarefas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botão para excluir tarefas
botao_excluir = tk.Button(janela, text="Excluir Selecionada", command=excluir_tarefa)
botao_excluir.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
