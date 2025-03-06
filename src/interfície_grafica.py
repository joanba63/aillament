import tkinter as tk
from tkinter import ttk
from pestanya_dades_edifici import PestanyaDadesEdifici

class InterficieGrafica:
    def __init__(self, root):
        print("5.1. Inicialitzant InterficieGrafica...")
        self.root = root
        self.root.title("Càlcul d'Aïllament Tèrmic")
        self.root.geometry("800x600")
        print("5.2. Finestra principal configurada.")

        # Missatge de benvinguda
        self.missatge_benvinguda = tk.Label(self.root, text="Benvingut al programa de càlcul d'aïllament tèrmic!", font=("Arial", 16))
        self.missatge_benvinguda.pack(pady=50)

        # Crear el menú superior
        print("5.3. Creant el menú superior...")
        self.crear_menu()
        print("5.4. Menú superior creat.")

        # Inicialment, no es mostren les pestanyes
        self.notebook = None
        self.pestanya_dades = None

    def crear_menu(self):
        """Crea el menú superior."""
        print("5.3.1. Creant menú superior...")
        menubar = tk.Menu(self.root)

        # Menú Arxiu
        print("5.3.2. Creant menú 'Arxiu'...")
        menu_arxiu = tk.Menu(menubar, tearoff=0)
        menu_arxiu.add_command(label="Nou", command=self.nou_arxiu)
        menu_arxiu.add_command(label="Obrir", command=self.obrir_arxiu)
        menu_arxiu.add_separator()
        menu_arxiu.add_command(label="Sortir", command=self.root.quit)
        menubar.add_cascade(label="Arxiu", menu=menu_arxiu)

        # Menú Ajuda
        print("5.3.4. Creant menú 'Ajuda'...")
        menu_ajuda = tk.Menu(menubar, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

        # Configurar el menú a la finestra principal
        print("5.3.6. Configurant menú a la finestra principal...")
        self.root.config(menu=menubar)
        print("5.3.7. Menú configurat a la finestra principal.")

    def nou_arxiu(self):
        """Neteja tots els camps per començar un nou projecte."""
        print("Funció 'nou_arxiu' executada.")
        self.mostrar_pestanya_dades()

    def obrir_arxiu(self):
        """Obre un fitxer JSON amb dades guardades."""
        print("Funció 'obrir_arxiu' executada.")
        self.mostrar_pestanya_dades()

    def mostrar_pestanya_dades(self):
        """Mostra la pestanya 'Dades d'edifici'."""
        print("5.5. Creant pestanyes principals...")
        if self.notebook is None:
            # Crear el notebook si no existeix
            self.notebook = ttk.Notebook(self.root)
            self.notebook.pack(fill=tk.BOTH, expand=True)
            print("5.5.2. Notebook per a pestanyes principals creat.")

            # Afegir la pestanya "Dades d'edifici"
            print("5.5.3. Afegint pestanya 'Dades d'edifici'...")
            self.pestanya_dades = PestanyaDadesEdifici(self.notebook)
            self.notebook.add(self.pestanya_dades, text="Dades d'edifici")
            print("5.5.4. Pestanya 'Dades d'edifici' afegida.")

        # Amagar el missatge de benvinguda
        self.missatge_benvinguda.pack_forget()

    def guardar_dades(self):
        """Guarda les dades en un fitxer JSON."""
        print("Funció 'guardar_dades' executada.")

    def mostrar_sobre(self):
        """Mostra informació sobre el programa."""
        print("Funció 'mostrar_sobre' executada.")