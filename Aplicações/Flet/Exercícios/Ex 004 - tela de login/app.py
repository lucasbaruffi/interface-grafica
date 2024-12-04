import flet as ft

def main(page:ft.Page):

    def on_click(e):
        if userField.value == "Lucas" and senhaField.value == "admin":
            mensagem = f"Bem vindo {userField.value}!"
        else:
            mensagem = "Acesso incorreto!"
        
        txtResultado.value = mensagem
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txtLoginPage = ft.Text("Preencha os dados para o Login", width=300)
    userField = ft.TextField(label="Nome de Usuário", width=300)
    senhaField = ft.TextField(label="Senha", width=300, password=True)
    btnSend = ft.Button("Enviar", width=300, on_click=on_click)
    txtResultado = ft.Text("", width=300)

    page.add(
        ft.Column(
            [
                txtLoginPage,
                userField,
                senhaField,
                btnSend,
                txtResultado
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)