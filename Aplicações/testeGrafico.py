from tkinter import *

# É necessário criar uma função a ser executada no clique do botão
def mostrarCotacao():
    texto = """Dólar: 5,50
Euro: 7,00
BTC: 15368,00"""

    # Modifica o texto adicionando as informações
    texto_cotacoes["text"] = texto

# Essa é a abertura da Janela
janela = Tk()

# Define o título da Janela
janela.title("Cotação Atual das Moedas")

# A Janela é responsiva, então vale adicionar primeiro os elementos 
# para ver como fica

# Adicionar texto:
texto_orientacao = Label(janela, text="Clique no botão para exibir a cotação das Moedas")

# Colocar no Grid
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)


# Criar Botão:

botao = Button(janela, text="Buscar Cotações", command=mostrarCotacao)
botao.grid(column=0, row=1, padx=10, pady=10)



# Texto Dinâmico com o resultado:

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

# Isso mantém a Janela funcionano em Loop
janela.mainloop()