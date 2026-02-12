import flet as ft
from flet import Text

def main(page: ft.Page):
    page.title = "Hot Reload Example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"

    text : Text = Text(value = "Hola mundo",
                       text_align = ft.TextAlign.CENTER,
                       width = 200,
                       size = 30,
                       color = "red")

    page.add(text)


if __name__ == "__main__":
    ft.app(target=main)