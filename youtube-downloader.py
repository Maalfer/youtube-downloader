import subprocess

def limpiar_cache():
    """Limpia el caché de yt-dlp."""
    try:
        print("Limpiando el caché de yt-dlp...")
        subprocess.run(["yt-dlp", "--rm-cache-dir"], check=True)
        print("Caché limpiado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al limpiar el caché: {e}")
    except Exception as e:
        print(f"Ocurrió un error al limpiar el caché: {e}")

def descargar_video(url, output_path="."):
    """Descarga un video de YouTube con la mejor calidad disponible."""
    try:
        print("Iniciando la descarga del video...")
        
        comando = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            url
        ]
        
        subprocess.run(comando, check=True)
        print("Descarga completada.")
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar el video: {e}")
    except Exception as e:
        print(f"Ocurrió un error al descargar el video: {e}")

if __name__ == "__main__":
    limpiar_cache()  # Ejecutamos esto para que permita descargar el mismo vídeo más de una vez.
    
    url = input("Introduce la URL del video de YouTube: ")
    output_path = input("Introduce la ruta de salida (deja en blanco para usar la carpeta actual): ") or "."
    descargar_video(url, output_path)
