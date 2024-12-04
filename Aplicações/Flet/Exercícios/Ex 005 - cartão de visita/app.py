import flet as ft

def main(page: ft.Page):

    def seguir(e):
        if btnSeguir.content.value == "Seguir":
            btnSeguir.content.value = "Deixar de Seguir"
            btnSeguir.content.weight = "normal"
            btnSeguir.bgcolor = "#ABABAB"
        else:
            btnSeguir.content.value = "Seguir"
            btnSeguir.content.weight = "bold"
            btnSeguir.bgcolor = "#007BFF"
        page.update()

    page.fonts = {
        "Inter": "Exercícios\\Ex 005 - cartão de visita\\Inter.ttc"
    }

    foto = ft.Image("Exercícios\\Ex 005 - cartão de visita\\assets\\avatar.png")

    nome = ft.Text(
        value = "Nome Sobrenome",
        font_family = "Inter Bold",
        color = "#333333",
        weight = "bold",
        size = 18
    )

    descricao = ft.Text(
        value="breve descrição",
        font_family= "Inter",
        color = "#666666",
        italic = True,
        size = 14
    )
    btnSeguir = ft.Button(
        content = ft.Text(
            value="Seguir",
            font_family="Inter",
            weight="bold"
        ),
        width = 187,
        height = 40,
        bgcolor = "#007BFF",
        color = "#FFFFFF",
        style = ft.ButtonStyle(
            shape = ft.RoundedRectangleBorder(radius=5)
        ),
        on_click=seguir
    )

    colunaPrincipal = ft.Column(
        [foto,
         nome,
         descricao,
         btnSeguir],
         spacing = 30,
         horizontal_alignment = ft.CrossAxisAlignment.CENTER
    )

    page.add(
        ft.Container(
            colunaPrincipal,
            bgcolor = "#F0F0F0",
            width = 300,
            height = 345,
            border_radius = 10,
            alignment = ft.alignment.center,
            padding = 48
        )
    )



ft.app(target=main)