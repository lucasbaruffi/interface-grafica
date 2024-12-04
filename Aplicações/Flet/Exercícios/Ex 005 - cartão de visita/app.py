import flet as ft

def main(page: ft.Page):

    foto = ft.Image("Exercícios\\Ex 005 - cartão de visita\\avatar.png")

    nome = ft.Text(
        value="Nome Sobrenome"
    )

    descricao = ft.Text(
        value="Descrição sobre o contato"
    )

    btnSeguir = ft.Button(
        text="Seguir"
    )

    colunaPrincipal = ft.Column(
        [foto,
         nome,
         descricao,
         btnSeguir]
    )

    page.add(
        ft.Container(
            colunaPrincipal,
            bgcolor="#F0F0F0",
            width=300,
            height=375,
            border_radius=10

        )
    )





ft.app(target=main)