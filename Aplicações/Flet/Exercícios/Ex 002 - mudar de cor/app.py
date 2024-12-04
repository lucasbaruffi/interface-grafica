import flet as ft

def main(page:ft.Page):

    def colorChange(e):
        page.bgcolor = ft.colors.random()
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    btn = ft.IconButton(
        ft.icons.REFRESH, 
        on_click=colorChange)

    page.add(
        ft.Row([btn], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)