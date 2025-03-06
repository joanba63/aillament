import tkinter as tk
from tkinter import ttk, messagebox

class PestanyaObertures(tk.Frame):
    def __init__(self, parent):
        print("5.5.3.3.7.1. Inicialitzant PestanyaObertures...")
        super().__init__(parent)
        self.parent = parent
        print("5.5.3.3.7.2. PestanyaObertures inicialitzada.")

        # Llista per emmagatzemar les obertures
        self.llista_obertures = []

        # Crear el formulari
        print("5.5.3.3.7.3. Creant formulari per a 'Obertures (Portes i Finestres)'...")
        self.crear_formulari()
        print("5.5.3.3.7.4. Formulari per a 'Obertures (Portes i Finestres)' creat.")

    def crear_formulari(self):
        """Crea el formulari per afegir obertures."""
        # Orientació
        print("5.5.3.3.7.3.1. Afegint camp d'orientació...")
        tk.Label(self, text="Orientació:").grid(row=0, column=0, padx=10, pady=10)
        self.orientacio = ttk.Combobox(self, values=["Nord", "Sud", "Est", "Oest"])
        self.orientacio.grid(row=0, column=1, padx=10, pady=10)

        # Mida (alçada i amplada)
        print("5.5.3.3.7.3.2. Afegint camps de mida...")
        tk.Label(self, text="Alçada (m):").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_alcada = tk.Entry(self)
        self.entrada_alcada.grid(row=1, column=1, padx=10, pady=10)
        self.entrada_alcada.bind("<KeyRelease>", self.calcular_metres_quadrats)  # Calcula automàticament

        tk.Label(self, text="Amplada (m):").grid(row=2, column=0, padx=10, pady=10)
        self.entrada_amplada = tk.Entry(self)
        self.entrada_amplada.grid(row=2, column=1, padx=10, pady=10)
        self.entrada_amplada.bind("<KeyRelease>", self.calcular_metres_quadrats)  # Calcula automàticament

        # Metres quadrats (calculat automàticament)
        self.etiqueta_metres_quadrats = tk.Label(self, text="Metres quadrats: 0.00", fg="blue")
        self.etiqueta_metres_quadrats.grid(row=3, column=0, columnspan=2, pady=10)

        # Material de l'obertura
        print("5.5.3.3.7.3.3. Afegint camp de material...")
        tk.Label(self, text="Material:").grid(row=4, column=0, padx=10, pady=10)
        self.material = ttk.Combobox(self, values=["Fusta", "Alumini", "PVC", "Ferro"])
        self.material.grid(row=4, column=1, padx=10, pady=10)

        # Vidres
        print("5.5.3.3.7.3.4. Afegint camps de vidres...")
        self.te_vidres = tk.BooleanVar(value=True)
        self.check_vidres = tk.Checkbutton(self, text="Té vidres", variable=self.te_vidres, command=self.actualitzar_vidres)
        self.check_vidres.grid(row=5, column=0, columnspan=2, pady=10)

        self.frame_vidres = tk.Frame(self)
        self.frame_vidres.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.frame_vidres, text="Tipus de vidre:").grid(row=0, column=0, padx=10, pady=10)
        self.tipus_vidre = ttk.Combobox(self.frame_vidres, values=["Simple", "Doble", "Triple"])
        self.tipus_vidre.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.frame_vidres, text="Gruix del vidre (mm):").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_gruix_vidre = tk.Entry(self.frame_vidres)
        self.entrada_gruix_vidre.grid(row=1, column=1, padx=10, pady=10)

        # Botó per afegir obertura
        print("5.5.3.3.7.3.5. Afegint botó per afegir obertura...")
        self.boto_afegir = tk.Button(self, text="Afegir obertura", command=self.afegir_obertura)
        self.boto_afegir.grid(row=7, column=0, columnspan=2, pady=10)

        # Llista d'obertures afegides
        print("5.5.3.3.7.3.6. Afegint llista d'obertures...")
        self.llista_obertures_afegides = tk.Listbox(self, width=50)
        self.llista_obertures_afegides.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def actualitzar_vidres(self):
        """Mostra o amaga els camps de vidres."""
        if self.te_vidres.get():
            self.frame_vidres.grid()
        else:
            self.frame_vidres.grid_remove()

    def calcular_metres_quadrats(self, event=None):
        """Calcula els metres quadrats de l'obertura."""
        try:
            alcada = float(self.entrada_alcada.get())
            amplada = float(self.entrada_amplada.get())
            metres_quadrats = alcada * amplada
            self.etiqueta_metres_quadrats.config(text=f"Metres quadrats: {metres_quadrats:.2f}", fg="blue")
        except ValueError:
            self.etiqueta_metres_quadrats.config(text="Metres quadrats: 0.00", fg="blue")

    def afegir_obertura(self):
        """Afegeix una obertura a la llista."""
        try:
            orientacio = self.orientacio.get()
            alcada = float(self.entrada_alcada.get())
            amplada = float(self.entrada_amplada.get())
            material = self.material.get()
            te_vidres = self.te_vidres.get()
            tipus_vidre = self.tipus_vidre.get() if te_vidres else "Sense vidres"
            gruix_vidre = self.entrada_gruix_vidre.get() if te_vidres else "N/A"

            obertura = {
                "orientacio": orientacio,
                "alcada": alcada,
                "amplada": amplada,
                "material": material,
                "te_vidres": te_vidres,
                "tipus_vidre": tipus_vidre,
                "gruix_vidre": gruix_vidre
            }

            self.llista_obertures.append(obertura)
            self.actualitzar_llista_obertures()
            messagebox.showinfo("Èxit", "Obertura afegida correctament.")
        except ValueError:
            messagebox.showerror("Error", "Si us plau, omple tots els camps correctament.")

    def actualitzar_llista_obertures(self):
        """Actualitza la llista d'obertures afegides."""
        self.llista_obertures_afegides.delete(0, tk.END)
        for obertura in self.llista_obertures:
            text = (f"Orientació: {obertura['orientacio']}, "
                    f"Mida: {obertura['alcada']}m x {obertura['amplada']}m, "
                    f"Material: {obertura['material']}, "
                    f"Vidres: {obertura['tipus_vidre']} ({obertura['gruix_vidre']})")
            self.llista_obertures_afegides.insert(tk.END, text)