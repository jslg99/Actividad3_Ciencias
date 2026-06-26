import flet as ft
from view.paneles import (
    crear_panel_titulo,
    crear_selector,
    crear_campo_intervalo,
    crear_botones,
    crear_texto_resultado,
)


class VentanaView:
    def __init__(
        self,
        page: ft.Page,
        on_proceso_change,
        on_intervalo_change,
        on_iniciar,
        on_detener,
    ):
        self.page = page
        self._on_proceso_change = on_proceso_change
        self._on_intervalo_change = on_intervalo_change
        self._on_iniciar = on_iniciar
        self._on_detener = on_detener

        self._dropdown = None
        self._campo_intervalo = None
        self._btn_iniciar = None
        self._btn_detener = None
        self._texto_resultado = None

        self._build()

    def _build(self):
        self.page.title = "Analizador de Memoria RAM"
        self.page.bgcolor = "#1E1E2E"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 20

        titulo = crear_panel_titulo()
        self._dropdown = crear_selector(self._on_proceso_change)
        self._campo_intervalo = crear_campo_intervalo(self._on_intervalo_change)
        self._btn_iniciar, self._btn_detener = crear_botones(
            self._on_iniciar, self._on_detener
        )
        self._texto_resultado = crear_texto_resultado()

        separador = ft.Container(height=3, bgcolor="#508C65", border_radius=2)

        panel_izquierdo = ft.Container(
            content=ft.Column(
                [
                    self._dropdown,
                    self._campo_intervalo,
                    ft.Divider(height=1, color="#E0E0E0"),
                    ft.Row(
                        [self._btn_iniciar, self._btn_detener],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ],
                spacing=12,
            ),
            border=ft.Border(
                top=ft.BorderSide(1, "#D0D0D0"),
                bottom=ft.BorderSide(1, "#D0D0D0"),
                left=ft.BorderSide(1, "#D0D0D0"),
                right=ft.BorderSide(1, "#D0D0D0"),
            ),
            border_radius=12,
            padding=18,
        )

        panel_resultado = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Memoria RSS:",
                        size=20,
                        color="#854747",
                        weight=ft.FontWeight.BOLD,
                    ),
                    self._texto_resultado,
                    ft.Text(
                        "en tiempo real",
                        size=12,
                        color="#FFFFFF",
                        italic=True,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="#508C65",
            padding=28,
            border_radius=16,
            width=230,
            shadow=ft.BoxShadow(
                blur_radius=8, color="#1E1E2E", offset=ft.Offset(0, 2)
            ),
        )

        fila_columnas = ft.Row(
            [panel_izquierdo, panel_resultado],
            spacing=25,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        contenedor = ft.Container(
            content=ft.Column(
                [
                    titulo,
                    separador,
                    fila_columnas,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
            ),
            bgcolor="#FFFFFF",
            padding=30,
            border_radius=20,
            width=600,
            shadow=ft.BoxShadow(
                blur_radius=20, color="#000000", offset=ft.Offset(0, 10)
            ),
        )

        self.page.add(contenedor)

    def actualizar_dropdown(self, procesos):
        if not procesos:
            self._dropdown.options = [ft.dropdown.Option("No hay procesos Python")]
            self._dropdown.value = None
        else:
            self._dropdown.options = [
                ft.dropdown.Option(
                    str(p["pid"]), f"{p['name']} (PID: {p['pid']})"
                )
                for p in procesos
            ]
        self._dropdown.update()

    def actualizar_resultado(self, texto):
        self._texto_resultado.value = texto
        self._texto_resultado.update()

    def habilitar_iniciar(self, habilitado):
        self._btn_iniciar.disabled = not habilitado
        self._btn_iniciar.update()

    def habilitar_detener(self, habilitado):
        self._btn_detener.disabled = not habilitado
        self._btn_detener.update()

    def bloquear_controles(self, bloquear):
        self._dropdown.disabled = bloquear
        self._campo_intervalo.disabled = bloquear
        self._dropdown.update()
        self._campo_intervalo.update()