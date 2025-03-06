import tkinter as tk
from tkinter import simpledialog, messagebox

def obtenir_dades_entrada():
    """Recull les dades bàsiques de l'usuari a través d'una GUI."""
    root = tk.Tk()
    root.withdraw()  # Amaga la finestra principal

    try:
        latitud = simpledialog.askfloat("Dades", "Latitud (ex. 41.3851): ")
        longitud = simpledialog.askfloat("Dades", "Longitud (ex. 2.1734): ")
        altitud = simpledialog.askfloat("Dades", "Altitud sobre el nivell del mar (m): ")
        temperatura_media = simpledialog.askfloat("Dades", "Temperatura mitjana anual (°C): ")
        humitat_relativa = simpledialog.askfloat("Dades", "Humitat relativa mitjana (%): ")
        clima = simpledialog.askstring("Dades", "Tipus de clima (ex. Mediterrani, Continental, etc.): ")

        return {
            "latitud": latitud,
            "longitud": longitud,
            "altitud": altitud,
            "temperatura_media": temperatura_media,
            "humitat_relativa": humitat_relativa,
            "clima": clima
        }
    except ValueError:
        messagebox.showerror("Error", "Si us plau, introdueix valors numèrics vàlids.")
        return None