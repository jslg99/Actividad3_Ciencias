import flet as ft

def crear_panel_info():
    return ft.Container(
        content = ft.Text("Calculador de memoria RAM", size=30, color="#FFFFFF", text_align=ft.TextAlign.CENTER),
    )

def crear_panel_detalles():
    return ft.Container(
        content = ft.Column(
            [
            ft.Text("Memoria RAM en uso:" , size=20, color="#FFFFFF", text_align=ft.TextAlign.CENTER),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
        ),
        bgcolor = "#508C65",
        padding = 15,
        border_radius = 10,
        width = 250,
    )        