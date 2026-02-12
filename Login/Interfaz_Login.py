import flet as ft
from flet import Text

def main (page:ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(container)
    pass

container = ft.Container (
    ft.Column(
    [
        ft.Container(
            ft.Text(
                "Iniciar Sesion",
                width=320,
                height=50,
                text_align= "Center",
                weight="w900"
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width= 280,
                height= 50,
                hint_text = "Correo Electronico",   
                border= "Underline",
                prefix_icon= ft.Icons.EMAIL
            ),
            padding = ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width= 280,
                height= 50,
                hint_text = "Contraseña",   
                border= "Underline",
                prefix_icon= ft.Icons.LOCK,
                password = True
            ),
            padding = ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Checkbox(
                label= "Recordar Contraseña",
                check_color= ft.Colors.BLACK
            ),
            padding = ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                 content = "Iniciar Sesion",
                 width= 400,
            ),
            padding = ft.padding.only(1,20)
            ),
        ft.Container(
            ft.Row(
                [
                    ft.IconButton(
                        icon = ft.Icons.MAIL,
                        tooltip= "Google",
                        icon_color= ft.Colors.BLUE_900
                    ),

                ],
            ),
        ),
    ],  
    alignment = ft.MainAxisAlignment.SPACE_EVENLY  
    ),
    border_radius = 10,
    width= 320,
    height= 500,
    gradient= ft.LinearGradient( [        
        ft.Colors.PURPLE_200,
        ft.Colors.RED_100,
        ft.Colors.PINK_200]
    )
)

ft.app(target = main)

