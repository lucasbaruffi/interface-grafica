import flet as ft

def main(page:ft.Page):

    orange = "#FF9F0A"
    lettet_bg_orange = "#FFFFFF"
    white_gray = "#A6A6A6"
    lettet_bg_white_gray = "#000000"
    dark_gray = "#333333"
    lettet_bg_dark_gray = "#FFFFFF"

    # Linha 1 ----
    btnAC = ft.TextButton(
        content=ft.Text(
            value="AC",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_white_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=white_gray
            )
        )

    btnIndef = ft.TextButton(
        content=ft.Text(
            value="?",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_white_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=white_gray
            )
        )       

    btnPercent = ft.TextButton(
        content=ft.Text(
            value="%",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_white_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=white_gray
            )
        )

    btnDiv = ft.TextButton(
        content=ft.Text(
            value="÷",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_orange
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=orange
            )
        )       


    # Linha 2 ----

    btn7 = ft.TextButton(
        content=ft.Text(
            value="7",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btn8 = ft.TextButton(
        content=ft.Text(
            value="8",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )       

    btn9 = ft.TextButton(
        content=ft.Text(
            value="9",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btnX = ft.TextButton(
        content=ft.Text(
            value="x",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_orange
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=orange
            )
        )     

    # Linha 3 ----

    btn4 = ft.TextButton(
        content=ft.Text(
            value="4",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btn5 = ft.TextButton(
        content=ft.Text(
            value="5",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )       

    btn6 = ft.TextButton(
        content=ft.Text(
            value="6",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btnSub = ft.TextButton(
        content=ft.Text(
            value="-",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_orange
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=orange
            )
        )       


    # Linha 4 ----

    btn1 = ft.TextButton(
        content=ft.Text(
            value="1",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btn2 = ft.TextButton(
        content=ft.Text(
            value="2",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )       

    btn3 = ft.TextButton(
        content=ft.Text(
            value="3",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btnAdd = ft.TextButton(
        content=ft.Text(
            value="+",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_orange
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=orange
            )
        )     



    # Linha 5 ----

    btn0 = ft.TextButton(
        content=ft.Text(
            value="0",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )       

    btnDot = ft.TextButton(
        content=ft.Text(
            value=".",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_dark_gray
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=dark_gray
            )
        )

    btnEqual = ft.TextButton(
        content=ft.Text(
            value="=",
            size=25,
            text_align=ft.TextAlign.CENTER,
            color=lettet_bg_orange
        ),
        width=80,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(100),
            bgcolor=orange
            )
        )     

    page.add(
        ft.Row([btnAC,btnIndef,btnPercent,btnDiv]),
        ft.Row([btn7,btn8,btn9,btnX]),
        ft.Row([btn4,btn5,btn6,btnSub]),
        ft.Row([btn1,btn2,btn3,btnAdd]),
        ft.Row([btn0,btnDot,btnEqual]))


ft.app(target=main)