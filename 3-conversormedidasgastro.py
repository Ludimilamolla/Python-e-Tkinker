import tkinter as tk

# glossario gastronomico
conversoes_culinaria = {
    "Xícaras para Colheres de Sopa": 16,
    "Xícaras para Colheres de Chá": 48,
    "Colheres de Sopa para Xícaras": 1/16,
    "Colheres de Sopa para Colheres de Chá": 3,
    "Colheres de Chá para Xícaras": 1/48,
    "Colheres de Chá para Colheres de Sopa": 1/3
}

# Função - realizar a conversão
def converter_medida():
    try:
        medida_original = float(entrada_medida_original.get())
        tipo_conversao = tipo_conversao_var.get()
        fator_conversao = conversoes_culinaria[tipo_conversao]
        medida_convertida = medida_original * fator_conversao
        resultado.config(text=f"{medida_original} {tipo_conversao.split(' para ')[0]} = {medida_convertida} {tipo_conversao.split(' para ')[1]}")
    except ValueError:
        resultado.config(text="Entrada inválida")

# Cria janela principal
janela = tk.Tk()
janela.title("Conversor de Medidas de Culinária")

# Cria entrada para a medida original
entrada_medida_original = tk.Entry(janela)
entrada_medida_original.grid(row=0, column=0, padx=10, pady=10)

# Cria opções de conversão
tipo_conversao_var = tk.StringVar(value="Xícaras para Colheres de Sopa")
opcoes_conversao = tk.OptionMenu(janela, tipo_conversao_var, *conversoes_culinaria.keys())
opcoes_conversao.grid(row=0, column=1, padx=10, pady=10)

# Cria botão para converter
botao_converter = tk.Button(janela, text="Converter", command=converter_medida)
botao_converter.grid(row=0, column=2, padx=10, pady=10)

# Cria rótulo para exibir o resultado
resultado = tk.Label(janela, text="")
resultado.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

janela.mainloop()
