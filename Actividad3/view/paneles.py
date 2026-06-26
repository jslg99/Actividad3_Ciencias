import flet as ft


def crear_panel_titulo():
    return ft.Text(
        spans=[
            ft.TextSpan("Analizador de Memoria ", ft.TextStyle(size=26, color="#1E1E2E")),
            ft.TextSpan("RAM", ft.TextStyle(size=26, color="#508C65", weight=ft.FontWeight.BOLD)),
        ],
        text_align=ft.TextAlign.CENTER,
    )


def crear_selector(on_select):
    return ft.Dropdown(
        label="Proceso Python:",
        on_select=on_select,
        options=[ft.dropdown.Option(text="No hay procesos")],
        label_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD, color="#1E1E2E"),
        color="#1E1E2E",
        text_size=14,
        width=250
    )


def crear_campo_intervalo(on_change):
    return ft.TextField(
        label="Intervalo (ms):",
        value="1000",
        input_filter=ft.NumbersOnlyInputFilter(),
        on_change=on_change,
        text_align=ft.TextAlign.CENTER,
        hint_text="Mín. 100 ms",
        label_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD, color="#1E1E2E"),
        color="#1E1E2E",
        text_size=14,
        width=250
    )


def crear_botones(on_iniciar, on_detener):
    btn_iniciar = ft.ElevatedButton(
        "Iniciar Análisis",
        on_click=on_iniciar,
        disabled=True,
        icon=ft.icons.Icons.PLAY_ARROW,
        color="#FFFFFF",
        bgcolor="#508C65",
        width=120,
        height=60
    )
    btn_detener = ft.ElevatedButton(
        "Detener Análisis",
        on_click=on_detener,
        disabled=True,
        icon=ft.icons.Icons.STOP,
        color="#FFFFFF",
        bgcolor="#854747",
        width=120,
        height=60
    )
    return btn_iniciar, btn_detener


def crear_texto_resultado():
    return ft.Text("0 MB", size=40, weight=ft.FontWeight.BOLD, color="#FFFFFF")
    