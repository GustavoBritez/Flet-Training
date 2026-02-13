import flet as ft
from flet import Text
from Login.Be.UsuarioBE import UsuarioBE as UBE
from Login.BLL.UsuarioService import UsuarioService as UsuarioService

def main (page:ft.Page):
    page.title = "Login System"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    def btnClick(e):
        
        nuevo_usuario = UBE(email = txt_user.value , password = txt_pass.value)
        
        resultado = UsuarioService.registrar_usuario(nuevo_usuario)
        
        snack =  ft.SnackBar(
            content= ft.Text(f"Intentando iniciar sesion, usuario creado"),
            bgcolor= ft.Colors.BLUE_ACCENT
        )
        page.overlay.append(snack)
        snack.open = True
        page.update()
        
    btn_login = ft.ElevatedButton("Iniciar Sesion", on_click= btnClick )
    txt_user = ft.TextField(
            width= 280,
            height= 50,
            hint_text = "Correo Electronico",   
            border= "Underline",
            prefix_icon= ft.Icons.EMAIL)

    txt_pass = ft.TextField(
            width= 280,
            height= 50,
            hint_text = "Contrasenia",   
            border= "Underline",
            prefix_icon= ft.Icons.LOCK
    )
    
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
                txt_user, padding=20
                ),
            ft.Container(
                txt_pass , padding = 20
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
                    on_click = btnClick
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
    page.add(container)
    

ft.app(target = main)

