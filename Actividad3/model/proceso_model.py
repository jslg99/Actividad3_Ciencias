import psutil
from typing import List, Dict, Optional


def obtener_procesos_python() -> List[Dict]:
    procesos = []
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if proc.info["name"] and "python" in proc.info["name"].lower():
                cmdline = " ".join(proc.info["cmdline"]) if proc.info["cmdline"] else ""
                procesos.append({
                    "pid": proc.info["pid"],
                    "name": proc.info["name"],
                    "cmdline": cmdline,
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procesos


def leer_memoria_rss(pid: int) -> Optional[int]:
    try:
        proc = psutil.Process(pid)
        return proc.memory_info().rss
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None


def formatear_bytes(bytes_val: int) -> str:
    mb = bytes_val / (1024 * 1024)
    if mb >= 1024:
        gb = mb / 1024
        return f"{gb:.2f} GB"
    return f"{mb:.1f} MB"
