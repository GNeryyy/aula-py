import tkinter as tk
from tkinter import ttk

#Criação da janela

janela = tk.Tk()
janela.title = ("Combobox")
janela.geometry = ("500x250")

#Componente Label
ttk.Label (janela, text = "Combobox Widget", background = 'blue', foreground = 'white', font = ("Times New Roman", 15)).grid (row = 0, column=1)

ttk.Label (janela, text = "Selecione um mês: ", font = ("Times New Roman",10)).grid (column=0,row = 5, padx = 10, pady = 25)

n = tk.StringVar ()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)

escolha ['valeus'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro').grid (column = 1, row = 5)
escolha.grid (column = 1, row = 5)
escolha.current ()

janela.mainloop ()
