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

        self.missatge_benvinguda = tk.Label(self.root, text="Benvingut al programa de càlcul d'aïllament tèrmic!", font=("Arial", 16))
        self.missatge_benvinguda.pack(pady=50)

        print("5.3. Creant el menú superior...")
        self.crear_menu()
        print("5.4. Menú superior creat.")

        self.notebook = None
        self.pestanya_dades = None

    def crear_menu(self):
        print("5.3.1. Creant menú superior...")
        menubar = tk.Menu(self.root)

        print("5.3.2. Creant menú 'Arxiu'...")
        menu_arxiu = tk.Menu(menubar, tearoff=0)
        menu_arxiu.add_command(label="Nou", command=self.nou_arxiu)
        menu_arxiu.add_command(label="Obrir", command=self.obrir_arxiu)
        menu_arxiu.add_separator()
        menu_arxiu.add_command(label="Sortir", command=self.root.quit)
        menubar.add_cascade(label="Arxiu", menu=menu_arxiu)

        print("5.3.3. Creant menú 'Informes'...")
        menu_informes = tk.Menu(menubar, tearoff=0)
        menu_informes.add_command(label="Exportar a Calc", command=lambda: self.generar_informe("calc"))
        menu_informes.add_command(label="Exportar CSV", command=lambda: self.generar_informe("csv"))
        menubar.add_cascade(label="Informes", menu=menu_informes)

        print("5.3.4. Creant menú 'Ajuda'...")
        menu_ajuda = tk.Menu(menubar, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

        print("5.3.6. Configurant menú a la finestra principal...")
        self.root.config(menu=menubar)
        print("5.3.7. Menú configurat a la finestra principal.")

    def nou_arxiu(self):
        print("Funció 'nou_arxiu' executada.")
        self.mostrar_pestanya_dades()

    def obrir_arxiu(self):
        print("Funció 'obrir_arxiu' executada.")
        self.mostrar_pestanya_dades()

    def mostrar_pestanya_dades(self):
        print("5.5. Creant pestanyes principals...")
        if self.notebook is None:
            self.notebook = ttk.Notebook(self.root)
            self.notebook.pack(fill=tk.BOTH, expand=True)
            print("5.5.2. Notebook per a pestanyes principals creat.")

            print("5.5.3. Afegint pestanya 'Dades d'edifici'...")
            self.pestanya_dades = PestanyaDadesEdifici(self.notebook)
            self.notebook.add(self.pestanya_dades, text="Dades d'edifici")
            print("5.5.4. Pestanya 'Dades d'edifici' afegida.")

        self.missatge_benvinguda.pack_forget()

    def generar_informe(self, tipus):
        if tipus == "calc":
            print("Generant informe per LibreOffice Calc...")
        elif tipus == "csv":
            print("Generant informe CSV...")

    def mostrar_sobre(self):
        print("Funció 'mostrar_sobre' executada.")
