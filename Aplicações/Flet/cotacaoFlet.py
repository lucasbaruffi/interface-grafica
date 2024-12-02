import flet as ft

def main(page: ft.Page):

    page.fonts = {
        "Montserrat Regular": "/Flet/fonts/MontserratAlternates-Regular.otf"
    }

    texto_base = ft.Text("Cotação de Moedas", font_family="Montserrat Regular")

    page.add(ft.Row([texto_base]))

    pass


ft.app(target=main)