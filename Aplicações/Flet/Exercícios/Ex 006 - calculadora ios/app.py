import flet as ft

def main(page:ft.Page):

    textAC = ft.Text(
        value="AC",
        size=25,
        text_align=ft.TextAlign.CENTER,
        color="#000000"
    )

    btnAC = ft.TextButton(
        content=textAC,
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor="#A6A6A6"
            )
        )
        
        


    page.add(btnAC)


ft.app(target=main)