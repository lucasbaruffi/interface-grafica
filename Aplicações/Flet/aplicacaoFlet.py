# A ideia aqui é tentar algo com Flet... (precisa dar pip install flet)

import flet as ft

def main(page: ft.Page): # Esses ":" definem o tipo da variável, poderia ser "int", "str" e tal - para debug
    page.title= "Meu App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    # Lógica:
    def somar(e):
        caixa_texto.value = str(int(caixa_texto.value) + 1)
        page.update()
        
    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) - 1)
        page.update()
        pass

    # Criar itens da página
    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER, color="#E3116C")
    botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar)


    # Adiciona itens na página
    page.add(
        ft.Row([botao_menos, caixa_texto, botao_mais], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main) # Roda o aplicativo e informa a "página" de início