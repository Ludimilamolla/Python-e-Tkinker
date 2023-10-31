import tkinter as tk

# Função - visor
def atualizar_visor(valor):
    visor.config(text=valor)

# Função - calc resultado
def calcular():
    expressao = visor["text"]
    try:
        resultado = str(eval(expressao))
        atualizar_visor(resultado)
    except Exception:
        atualizar_visor("Erro")

# Função - add caractere no visor
def adicionar_caractere(caractere):
    visor.config(text=visor["text"] + caractere)

# Função - limpar visor
def limpar():
    visor.config(text="")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Cria o visor
visor = tk.Label(janela, text="", height=2, width=15, borderwidth=2, relief="solid")
visor.grid(row=0, column=0, columnspan=4)

# Cria os botões
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for botao in botoes:
    tk.Button(janela, text=botao, height=2, width=5, command=lambda b=botao: adicionar_caractere(b) if b != "=" else calcular()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botão de limpar
tk.Button(janela, text="C", height=2, width=5, command=limpar).grid(row=row, column=col)

janela.mainloop()
