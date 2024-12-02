from tkinter import *

janela = Tk()

# Define Título e Favicon
janela.title("Cotação de Valores")
janela.iconbitmap("Aplicações\money.ico")

# Tamanho da Janela
janela.geometry("557x340")

# Primeiro texto
texto_titulo = Label(janela, text="Cotação de Moedas", font=("Montserrat-regular", 42))

texto_titulo.grid(padx=34, pady=25)



janela.mainloop()

# Parei pois achei meio zuado, a qualidade visual da interface é borrada e não dá para selecionar os textos, como se fosse uma imagem...