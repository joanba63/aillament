import tkinter as tk
from tkinter import ttk
from pestanya_situacio_casa import PestanyaSituacioCasa
from pestanya_caracteristiques_edifici import PestanyaCaracteristiquesEdifici
from pestanya_obertures import PestanyaObertures

class PestanyaDadesEdifici(tk.Frame):
    def __init__(self, parent):
        print("5.5.3.1. Inicialitzant PestanyaDadesEdifici...")
        super().__init__(parent)
        self.parent = parent
        print("5.5.3.2. PestanyaDadesEdifici inicialitzada.")

        # Crear pestanyes secundàries
        print("5.5.3.3. Creant pestanyes secundàries...")
        self.crear_pestanyes()
        print("5.5.3.4. Pestanyes secundàries creades.")

    def crear_pestanyes(self):
        """Crea les pestanyes secundàries."""
        print("5.5.3.3.1. Creant notebook per a pestanyes secundàries...")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        print("5.5.3.3.2. Notebook per a pestanyes secundàries creat.")

        # Pestanya "Situació casa"
        print("5.5.3.3.3. Afegint pestanya 'Situació casa'...")
        self.pestanya_situacio = PestanyaSituacioCasa(self.notebook)
        self.notebook.add(self.pestanya_situacio, text="Situació casa")
        print("5.5.3.3.4. Pestanya 'Situació casa' afegida.")

        # Pestanya "Característiques de l'edifici"
        print("5.5.3.3.5. Afegint pestanya 'Característiques de l'edifici'...")
        self.pestanya_caracteristiques = PestanyaCaracteristiquesEdifici(self.notebook)
        self.notebook.add(self.pestanya_caracteristiques, text="Característiques de l'edifici")
        print("5.5.3.3.6. Pestanya 'Característiques de l'edifici' afegida.")

        # Pestanya "Obertures (Portes i Finestres)"
        print("5.5.3.3.7. Afegint pestanya 'Obertures (Portes i Finestres)'...")
        self.pestanya_obertures = PestanyaObertures(self.notebook)
        self.notebook.add(self.pestanya_obertures, text="Obertures (Portes i Finestres)")
        print("5.5.3.3.8. Pestanya 'Obertures (Portes i Finestres)' afegida.")