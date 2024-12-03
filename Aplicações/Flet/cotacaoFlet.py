import flet as ft

def main(page: ft.Page):

    def consulta_cnpj(e):

        valor_informado = box.value

        if type(valor_informado) != int:
            novo_texto = "Digite apenas Números"
        else:
            import requests
            import json
            
            url = f"https://economia.awesomeapi.com.br/json/last/{selecao.value}-BRL"

            r = requests.get(url=url)
            r = r.json()

            cotacao = float(r[f"{selecao.value}BRL"]["bid"])

            valor = valor_informado * cotacao

            novo_texto = f"Resultado: R$ {float(valor):,.2f}"

        caixa_resposta.value = novo_texto
        page.update()





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
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("EUR"),
            ft.dropdown.Option("BTC")])

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

    botao_converter = ft.TextButton(
        "Converter",
        on_click=consulta_cnpj
        )

    caixa_resposta = ft.Text(
        "Resultado: "
        )

    page.add(ft.Row([botao_converter, caixa_resposta]))


ft.app(target=main)