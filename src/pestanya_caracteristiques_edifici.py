import tkinter as tk
from tkinter import ttk

class PestanyaCaracteristiquesEdifici(tk.Frame):
    def __init__(self, parent):
        print("5.5.3.3.5.1. Inicialitzant PestanyaCaracteristiquesEdifici...")
        super().__init__(parent)
        self.parent = parent
        print("5.5.3.3.5.2. PestanyaCaracteristiquesEdifici inicialitzada.")

        # Crear el formulari
        print("5.5.3.3.5.3. Creant formulari per a 'Característiques de l'edifici'...")
        self.crear_formulari()
        print("5.5.3.3.5.4. Formulari per a 'Característiques de l'edifici' creat.")

    def crear_formulari(self):
        """Crea el formulari per introduir les característiques de l'edifici."""
        # Metres quadrats i alçada
        print("5.5.3.3.5.3.1. Afegint camps de metres quadrats i alçada...")
        tk.Label(self, text="Metres quadrats:").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_metres_quadrats = tk.Entry(self)
        self.entrada_metres_quadrats.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Alçada (m):").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_alcada = tk.Entry(self)
        self.entrada_alcada.grid(row=1, column=1, padx=10, pady=10)

        # Botó per calcular metres cúbics
        self.boto_calcular_metres_cubics = tk.Button(self, text="Calcular metres cúbics", command=self.calcular_metres_cubics)
        self.boto_calcular_metres_cubics.grid(row=2, column=0, columnspan=2, pady=10)

        # Resultat de metres cúbics
        self.etiqueta_metres_cubics = tk.Label(self, text="Metres cúbics: No calculat", fg="blue")
        self.etiqueta_metres_cubics.grid(row=3, column=0, columnspan=2, pady=10)

        # Parets
        print("5.5.3.3.5.3.2. Afegint camps per a parets...")
        tk.Label(self, text="Gruix de la paret (cm):").grid(row=4, column=0, padx=10, pady=10)
        self.entrada_gruix_paret = tk.Entry(self)
        self.entrada_gruix_paret.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self, text="Material de la paret:").grid(row=5, column=0, padx=10, pady=10)
        self.material_paret = ttk.Combobox(self, values=["Maó", "Formigó", "Pedra", "Fusta"])
        self.material_paret.grid(row=5, column=1, padx=10, pady=10)

        # Paret doble
        self.es_paret_doble = tk.BooleanVar()
        self.check_paret_doble = tk.Checkbutton(self, text="Paret doble", variable=self.es_paret_doble, command=self.actualitzar_paret_doble)
        self.check_paret_doble.grid(row=6, column=0, columnspan=2, pady=10)

        # Camps per a paret doble (inicialment ocults)
        self.frame_paret_doble = tk.Frame(self)
        self.frame_paret_doble.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.frame_paret_doble, text="Càmera d'aire o aïllant:").grid(row=0, column=0, padx=10, pady=10)
        self.tipus_camara = ttk.Combobox(self.frame_paret_doble, values=["Càmera d'aire", "Aïllant"])
        self.tipus_camara.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.frame_paret_doble, text="Gruix (cm):").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_gruix_camara = tk.Entry(self.frame_paret_doble)
        self.entrada_gruix_camara.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.frame_paret_doble, text="Tipus d'aïllant:").grid(row=2, column=0, padx=10, pady=10)
        self.tipus_aillant_camara = ttk.Combobox(self.frame_paret_doble, values=["Poliestirè", "Lana de roca", "Fibra de vidre"])
        self.tipus_aillant_camara.grid(row=2, column=1, padx=10, pady=10)

        self.frame_paret_doble.grid_remove()  # Ocultar inicialment

        # Terra
        print("5.5.3.3.5.3.3. Afegint camps per al terra...")
        tk.Label(self, text="Material del terra:").grid(row=8, column=0, padx=10, pady=10)
        self.material_terra = ttk.Combobox(self, values=["Ceràmica", "Parquet", "Màrmol", "Formigó"])
        self.material_terra.grid(row=8, column=1, padx=10, pady=10)

        tk.Label(self, text="Gruix del terra (cm):").grid(row=9, column=0, padx=10, pady=10)
        self.entrada_gruix_terra = tk.Entry(self)
        self.entrada_gruix_terra.grid(row=9, column=1, padx=10, pady=10)

        tk.Label(self, text="Aïllant del terra:").grid(row=10, column=0, padx=10, pady=10)
        self.tipus_aillant_terra = ttk.Combobox(self, values=["Poliestirè", "Lana de roca", "Fibra de vidre"])
        self.tipus_aillant_terra.grid(row=10, column=1, padx=10, pady=10)

        self.es_planta_baixa = tk.BooleanVar()
        self.check_planta_baixa = tk.Checkbutton(self, text="Planta baixa", variable=self.es_planta_baixa)
        self.check_planta_baixa.grid(row=11, column=0, columnspan=2, pady=10)

        # Sostre
        print("5.5.3.3.5.3.4. Afegint camps per al sostre...")
        tk.Label(self, text="Material del sostre:").grid(row=12, column=0, padx=10, pady=10)
        self.material_sostre = ttk.Combobox(self, values=["Pladur", "Formigó", "Fusta"])
        self.material_sostre.grid(row=12, column=1, padx=10, pady=10)

        tk.Label(self, text="Aïllant del sostre:").grid(row=13, column=0, padx=10, pady=10)
        self.tipus_aillant_sostre = ttk.Combobox(self, values=["Poliestirè", "Lana de roca", "Fibra de vidre"])
        self.tipus_aillant_sostre.grid(row=13, column=1, padx=10, pady=10)

        self.es_sostre_sol = tk.BooleanVar()
        self.check_sostre_sol = tk.Checkbutton(self, text="Sostre sol (no teulada)", variable=self.es_sostre_sol)
        self.check_sostre_sol.grid(row=14, column=0, columnspan=2, pady=10)

        # Teulada
        print("5.5.3.3.5.3.5. Afegint camps per a la teulada...")
        tk.Label(self, text="Mida entre sostre i teulada (m):").grid(row=15, column=0, padx=10, pady=10)
        self.entrada_mida_teulada = tk.Entry(self)
        self.entrada_mida_teulada.grid(row=15, column=1, padx=10, pady=10)

        tk.Label(self, text="Material de la teulada:").grid(row=16, column=0, padx=10, pady=10)
        self.material_teulada = ttk.Combobox(self, values=["Teula", "Fibrociment", "Zinc"])
        self.material_teulada.grid(row=16, column=1, padx=10, pady=10)

        tk.Label(self, text="Aïllant de la teulada:").grid(row=17, column=0, padx=10, pady=10)
        self.tipus_aillant_teulada = ttk.Combobox(self, values=["Poliestirè", "Lana de roca", "Fibra de vidre"])
        self.tipus_aillant_teulada.grid(row=17, column=1, padx=10, pady=10)

        tk.Label(self, text="Gruix de l'aïllant (cm):").grid(row=18, column=0, padx=10, pady=10)
        self.entrada_gruix_aillant_teulada = tk.Entry(self)
        self.entrada_gruix_aillant_teulada.grid(row=18, column=1, padx=10, pady=10)

    def calcular_metres_cubics(self):
        """Calcula els metres cúbics de l'edifici."""
        try:
            metres_quadrats = float(self.entrada_metres_quadrats.get())
            alcada = float(self.entrada_alcada.get())
            metres_cubics = metres_quadrats * alcada
            self.etiqueta_metres_cubics.config(text=f"Metres cúbics: {metres_cubics:.2f}", fg="green")
        except ValueError:
            self.etiqueta_metres_cubics.config(text="Error: Introdueix valors vàlids", fg="red")

    def actualitzar_paret_doble(self):
        """Mostra o amaga els camps per a paret doble."""
        if self.es_paret_doble.get():
            self.frame_paret_doble.grid()
        else:
            self.frame_paret_doble.grid_remove()