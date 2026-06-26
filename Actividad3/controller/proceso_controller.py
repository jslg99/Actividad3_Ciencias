import threading
import time
from model import proceso_model


class ProcesoController:
    def __init__(self, page, view):
        self.page = page
        self.view = view
        self._pid_seleccionado = None
        self._intervalo_ms = 1000
        self._running = False
        self._hilo = None

    def cargar_procesos(self):
        procesos = proceso_model.obtener_procesos_python()
        self.view.actualizar_dropdown(procesos)

    def on_proceso_change(self, e):
        if e.control.value and e.control.value != "No hay procesos Python":
            self._pid_seleccionado = int(e.control.value)
            self.view.habilitar_iniciar(True)

    def on_intervalo_change(self, e):
        try:
            val = int(e.control.value) if e.control.value.strip() else 1000
            if val < 100:
                val = 100
            val = round(val / 100) * 100
            e.control.value = str(val)
            self._intervalo_ms = val
            e.control.update()
        except ValueError:
            pass

    def iniciar_analisis(self, e):
        if self._pid_seleccionado is None:
            return
        self._running = True
        self.view.habilitar_iniciar(False)
        self.view.habilitar_detener(True)
        self.view.bloquear_controles(True)
        self._hilo = threading.Thread(target=self._loop_lectura, daemon=True)
        self._hilo.start()

    def detener_analisis(self, desde_hilo=False):
        self._running = False
        if self._hilo and not desde_hilo:
            self._hilo.join(timeout=2)
        self._hilo = None
        self.view.habilitar_iniciar(True)
        self.view.habilitar_detener(False)
        self.view.bloquear_controles(False)

    def _loop_lectura(self):
        while self._running:
            rss = proceso_model.leer_memoria_rss(self._pid_seleccionado)
            if rss is not None:
                texto = proceso_model.formatear_bytes(rss)
                self.view.actualizar_resultado(texto)
            else:
                self.view.actualizar_resultado("Proceso finalizado")
                self.detener_analisis(desde_hilo=True)
                break
            time.sleep(self._intervalo_ms / 1000)
