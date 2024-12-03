import flet as ft

def main(page: ft.Page):

    page.fonts = {
        "Montserrat": "https://github.com/JulietaUla/Montserrat/blob/master/fonts/ttf/Montserrat-Regular.ttf"
    }

    texto_base = ft.Text(
        "Cotação de Moedas", 
        font_family="Montserrat",
        size=42,
        weight=ft.FontWeight.W_100
        )
    
    page.add(ft.Row([texto_base]))


    escolha_moeda = ft.Text(
        "Escolha a Moeda:", 
        font_family="Montserrat",
        size=31,
        weight=ft.FontWeight.W_100
    )
    
    selecao = ft.Dropdown(
        value="Opções", 
        color="White", 
        border_color="White",
        options=[
            ft.dropdown.Option("Op1"),
            ft.dropdown.Option("Op2"),
            ft.dropdown.Option("Op3")])

    page.add(ft.Row([escolha_moeda, selecao]))



    valor_a_converter = ft.Text(
        "Valor a Converter:", 
        font_family="Montserrat",
        size=31,
        weight=ft.FontWeight.W_100
    )
    
    box = ft.TextField(
        border_color="White"
    )

    page.add(ft.Row([valor_a_converter, box]))

    page.add(ft.Row())

    botao_converter = ft.TextButton("Converter")

    page.add(ft.Row([botao_converter]))


ft.app(target=main)