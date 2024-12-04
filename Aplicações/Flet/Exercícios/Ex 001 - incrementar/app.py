import flet as ft

def main(page: ft.Page):

    def incrementar(e):
        result.value = result.value + 1
        page.update()

    def diminuir(e):
        result.value = result.value - 1
        page.update()
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    btMais = ft.IconButton(ft.icons.ADD, on_click=incrementar)
    btMenos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)

    result = ft.Text(value=0)

    page.add(ft.Row([btMenos, result, btMais], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)