import subprocess
import random

# Lista de User-Agents comunes
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
]

def limpiar_cache():
    """Limpia el caché de yt-dlp."""
    try:
        subprocess.run(["yt-dlp", "--rm-cache-dir"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def descargar_video(url, output_path="."):
    """Descarga un video de YouTube con la mejor calidad disponible."""
    try:
        # Selecciona un User-Agent aleatorio
        user_agent = random.choice(USER_AGENTS)

        comando = [
            "yt-dlp",
            "-f", "best[ext=mp4]",
            "--user-agent", user_agent,
            "--quiet",  # Reduce la salida al mínimo
            "--no-warnings",  # Elimina las advertencias
            "-o", f"{output_path}/%(title)s.%(ext)s",
            url
        ]

        subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("Error: No se pudo descargar el video. Intenta con otro enlace o configura cookies.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    limpiar_cache()  # Ejecutamos esto para que permita descargar el mismo vídeo más de una vez.

    url = input("Introduce la URL del video de YouTube: ")
    output_path = input("Introduce la ruta de salida (deja en blanco para usar la carpeta actual): ") or "."
    descargar_video(url, output_path)
