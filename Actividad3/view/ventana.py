import flet as ft
from paneles import crear_panel_info, crear_panel_detalles

def configurar_ventana(page: ft.Page):
    page.title = "Calculadora de Memoria RAM"
    page.window_width = 400
    page.window_height = 350
    page.bgcolor = "#854747"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    panel_superior = crear_panel_info()
    panel_inferior = crear_panel_detalles()

    recuadro_principal = ft.Container(
        content=ft.Column(
            [
                panel_superior,    
                panel_inferior
            ],
            spacing=25,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#1E1E2E",         
        padding=30,                
        border_radius=20,   
        width=400,
        height=300,

        border=ft.Border(
            top=ft.BorderSide(1, "#508C65"),
            bottom=ft.BorderSide(1, "#508C65"),
            left=ft.BorderSide(1, "#508C65"),
            right=ft.BorderSide(1, "#508C65")
        ),
        shadow=ft.BoxShadow(       
            blur_radius=20,
            color="#000000",
            offset=ft.Offset(0, 10)
        )
    )

    page.add(recuadro_principal)