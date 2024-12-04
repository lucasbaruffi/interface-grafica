import flet as ft

def main(page: ft.Page):

    def alterarNome(e):
        txtResult.value = f"Olá {campoNome.value}"
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    campoNome = ft.TextField(label="Digite seu nome", width=300)
    btnSend = ft.Button("Enviar", on_click=alterarNome, width=300)
    txtResult = ft.Text("", width=300)
    
    page.add(
        ft.Column([campoNome, btnSend, txtResult], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)