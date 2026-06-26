import flet as ft
from view.ventana import VentanaView
from controller.proceso_controller import ProcesoController


def main(page: ft.Page):
    controller = None

    def on_proceso_change(e):
        controller.on_proceso_change(e)

    def on_intervalo_change(e):
        controller.on_intervalo_change(e)

    def on_iniciar(e):
        controller.iniciar_analisis(e)

    def on_detener(e):
        controller.detener_analisis()

    view = VentanaView(
        page,
        on_proceso_change=on_proceso_change,
        on_intervalo_change=on_intervalo_change,
        on_iniciar=on_iniciar,
        on_detener=on_detener,
    )
    controller = ProcesoController(page, view)
    controller.cargar_procesos()


ft.run(main)