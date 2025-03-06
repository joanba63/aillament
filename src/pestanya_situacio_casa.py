import tkinter as tk
from tkinter import messagebox
from api_client import obtenir_dades_geogràfiques, obtenir_dades_meteorològiques

class PestanyaSituacioCasa(tk.Frame):
    def __init__(self, parent):
        print("5.5.3.3.3.1. Inicialitzant PestanyaSituacioCasa...")
        super().__init__(parent)
        self.parent = parent
        print("5.5.3.3.3.2. PestanyaSituacioCasa inicialitzada.")

        # Crear el formulari
        print("5.5.3.3.3.3. Creant formulari per a 'Situació casa'...")
        self.crear_formulari()
        print("5.5.3.3.3.4. Formulari per a 'Situació casa' creat.")

    def crear_formulari(self):
        """Crea el formulari per introduir les dades de la situació de la casa."""
        # Carrer
        print("5.5.3.3.3.3.1. Afegint camp de carrer...")
        tk.Label(self, text="Carrer:").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_carrer = tk.Entry(self, width=30)
        self.entrada_carrer.grid(row=0, column=1, padx=10, pady=10)
        print("5.5.3.3.3.3.2. Camp de carrer afegit.")

        # Número
        print("5.5.3.3.3.3.3. Afegint camp de número...")
        tk.Label(self, text="Número:").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_numero = tk.Entry(self, width=10)
        self.entrada_numero.grid(row=1, column=1, padx=10, pady=10)
        print("5.5.3.3.3.3.4. Camp de número afegit.")

        # Població
        print("5.5.3.3.3.3.5. Afegint camp de població...")
        tk.Label(self, text="Població:").grid(row=2, column=0, padx=10, pady=10)
        self.entrada_poblacio = tk.Entry(self, width=30)
        self.entrada_poblacio.grid(row=2, column=1, padx=10, pady=10)
        print("5.5.3.3.3.3.6. Camp de població afegit.")

        # Província
        print("5.5.3.3.3.3.7. Afegint camp de província...")
        tk.Label(self, text="Província:").grid(row=3, column=0, padx=10, pady=10)
        self.entrada_provincia = tk.Entry(self, width=30)
        self.entrada_provincia.grid(row=3, column=1, padx=10, pady=10)
        print("5.5.3.3.3.3.8. Camp de província afegit.")

        # Botó per obtenir dades GPS i meteorològiques
        print("5.5.3.3.3.3.9. Afegint botó 'Obtenir dades'...")
        boto_obtenir_dades = tk.Button(self, text="Obtenir dades", command=self.obtenir_dades)
        boto_obtenir_dades.grid(row=4, column=0, columnspan=2, pady=10)
        print("5.5.3.3.3.3.10. Botó 'Obtenir dades' afegit.")

        # Camp per mostrar les dades GPS
        print("5.5.3.3.3.3.11. Afegint camp per mostrar dades GPS...")
        self.etiqueta_gps = tk.Label(self, text="GPS: No disponible", fg="blue")
        self.etiqueta_gps.grid(row=5, column=0, columnspan=2, pady=10)
        print("5.5.3.3.3.3.12. Camp per mostrar dades GPS afegit.")

        # Camp per mostrar les dades meteorològiques
        print("5.5.3.3.3.3.13. Afegint camp per mostrar dades meteorològiques...")
        self.etiqueta_meteo = tk.Label(self, text="Dades meteorològiques: No disponibles", fg="green")
        self.etiqueta_meteo.grid(row=6, column=0, columnspan=2, pady=10)
        print("5.5.3.3.3.3.14. Camp per mostrar dades meteorològiques afegit.")

    def obtenir_dades(self):
        """Obté les dades GPS i meteorològiques."""
        print("5.5.3.3.3.3.10.1. Executant funció 'obtenir_dades'...")

        # Obtenir l'adreça completa
        carrer = self.entrada_carrer.get()
        numero = self.entrada_numero.get()
        poblacio = self.entrada_poblacio.get()
        provincia = self.entrada_provincia.get()

        if not carrer or not numero or not poblacio or not provincia:
            messagebox.showerror("Error", "Si us plau, omple tots els camps de l'adreça.")
            return

        adreca_completa = f"{carrer} {numero}, {poblacio}, {provincia}"
        print(f"5.5.3.3.3.3.10.2. Adreça completa: {adreca_completa}")

        try:
            # Obtenir dades geogràfiques
            print("5.5.3.3.3.3.10.3. Obtenint dades geogràfiques...")
            latitud, longitud = obtenir_dades_geogràfiques(adreca_completa)

            # Mostrar les dades GPS
            self.etiqueta_gps.config(text=f"GPS: Latitud={latitud}, Longitud={longitud}", fg="blue")
            print("5.5.3.3.3.3.10.4. Dades GPS mostrades.")

            # Obtenir dades meteorològiques
            print("5.5.3.3.3.3.10.5. Obtenint dades meteorològiques...")
            temperatura, humitat, clima = obtenir_dades_meteorològiques(latitud, longitud)

            # Mostrar les dades meteorològiques
            self.etiqueta_meteo.config(
                text=f"Dades meteorològiques:\nTemperatura: {temperatura}°C\nHumitat: {humitat}%\nClima: {clima}",
                fg="green"
            )
            print("5.5.3.3.3.3.10.6. Dades meteorològiques mostrades.")
        except Exception as e:
            print(f"5.5.3.3.3.3.10.7. Error en obtenir dades: {str(e)}")
            messagebox.showerror("Error", f"No s'han pogut obtenir les dades: {str(e)}")