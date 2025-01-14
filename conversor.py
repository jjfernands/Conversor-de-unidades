import tkinter as tk
from tkinter import messagebox

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def centimetros_para_metros(cm):
    return cm / 100

def metros_para_centimetros(m):
    return m * 100

def realizar_conversao():
    try:
        valor = float(entry_valor.get())
        opcao = var_opcao.get()

        if opcao == "Celsius para Fahrenheit":
            resultado = celsius_para_fahrenheit(valor)
            label_resultado.config(text=f"Resultado: {resultado:.2f} °F")
        
        elif opcao == "Fahrenheit para Celsius":
            resultado = fahrenheit_para_celsius(valor)
            label_resultado.config(text=f"Resultado: {resultado:.2f} °C")
        
        elif opcao == "Centímetros para Metros":
            resultado = centimetros_para_metros(valor)
            label_resultado.config(text=f"Resultado: {resultado:.2f} m")
        
        elif opcao == "Metros para Centímetros":
            resultado = metros_para_centimetros(valor)
            label_resultado.config(text=f"Resultado: {resultado:.2f} cm")
        
        else:
            messagebox.showerror("Erro", "Selecione uma opção de conversão.")
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor numérico válido.")

janela = tk.Tk()
janela.title("Conversor de Unidades")

label_instrucoes = tk.Label(janela, text="Insira o valor e escolha a conversão:")
label_instrucoes.pack(pady=10)

entry_valor = tk.Entry(janela)
entry_valor.pack(pady=5)

var_opcao = tk.StringVar(value="Escolha uma opção")
opcoes = ["Celsius para Fahrenheit", "Fahrenheit para Celsius", "Centímetros para Metros", "Metros para Centímetros"]
menu_opcoes = tk.OptionMenu(janela, var_opcao, *opcoes)
menu_opcoes.pack(pady=5)

botao_converter = tk.Button(janela, text="Converter", command=realizar_conversao)
botao_converter.pack(pady=10)

label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack(pady=10)

janela.mainloop()
