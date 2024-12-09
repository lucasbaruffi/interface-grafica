import flet as ft

def main(page:ft.Page):

    def print_hello_world(e):
        hello_world.visible = not(hello_world.visible)
        page.update()

    btn = ft.TextButton(
        text="Clique Aqui!",
        on_click=print_hello_world,
    )

    hello_world = ft.Text(
        value="Olá Mundo!",
        visible=False,
    )

    page.add(
        ft.Column(
            [btn,hello_world,]
        )
    )

ft.app(target=main)