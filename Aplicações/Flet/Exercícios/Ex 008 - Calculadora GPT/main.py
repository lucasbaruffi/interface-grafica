import flet
from flet import (
    Page, Text, ElevatedButton, Row, Column, TextField,
    ButtonStyle, RoundedRectangleBorder, TextStyle, colors, MainAxisAlignment
)


def main(page: Page):
    page.title = "Calculadora Flet"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = colors.BLUE_GREY_900
    page.padding = 20

    # Campo de exibição
    display = TextField(
        value="0",
        text_align="right",
        width=300,
        height=60,
        color=colors.WHITE,
        bgcolor=colors.BLACK45,
        border_radius=10,
        text_size=30,
        read_only=True
    )

    # Lógica da calculadora
    current_val = "0"
    operator = ""
    reset_next = False

    def update_display(val):
        display.value = val
        page.update()

    def button_click(e):
        nonlocal current_val, operator, reset_next
        btn_val = e.control.data
        
        if btn_val.isdigit() or btn_val == ".":
            if reset_next:
                current_val = "0"
                reset_next = False
            if current_val == "0" and btn_val != ".":
                current_val = btn_val
            else:
                if btn_val == "." and "." in current_val:
                    return
                current_val += btn_val
            update_display(current_val)
        elif btn_val in ["+", "-", "*", "/"]:
            operator = btn_val
            reset_next = True
            update_display(current_val)
        elif btn_val == "C":
            current_val = "0"
            operator = ""
            reset_next = False
            update_display(current_val)
        elif btn_val == "=":
            try:
                if operator:
                    expression = display.value
                    result = str(eval(expression))
                    current_val = result
                    operator = ""
                    reset_next = True
                    update_display(current_val)
            except Exception:
                current_val = "Error"
                operator = ""
                reset_next = True
                update_display(current_val)
        else:
            pass

    # Definição do estilo dos botões
    btn_style = ButtonStyle(
        color=colors.WHITE,
        bgcolor=colors.BLUE_GREY_700,
        shape=RoundedRectangleBorder(radius=10),
        text_style=TextStyle(size=20)
    )

    def make_button(text):
        return ElevatedButton(
            text,
            data=text,
            on_click=button_click,
            width=60,
            height=60,
            style=btn_style
        )

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "C", "+"],
        ["="]
    ]

    rows = []
    for row in buttons:
        row_controls = [make_button(i) for i in row]
        rows.append(Row(row_controls, alignment=MainAxisAlignment.CENTER, spacing=10))

    calc_container = Column(
        [display, *rows],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment="center",
        spacing=15
    )

    page.add(calc_container)


if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER, port=8080)
