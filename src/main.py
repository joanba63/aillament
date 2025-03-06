import tkinter as tk
from registre import configurar_log, registrar_log
from interfície_grafica import InterficieGrafica

def iniciar_aplicacio():
    """Inicia l'aplicació."""
    print("1. Iniciant l'aplicació...")
    
    # Configurar el sistema de logs
    print("2. Configurant el sistema de logs...")
    configurar_log()
    registrar_log("Inici de l'aplicació.")

    # Crear la finestra principal
    print("3. Creant la finestra principal...")
    root = tk.Tk()
    print("4. Finestra principal creada.")

    # Inicialitzar la interfície gràfica
    print("5. Inicialitzant la interfície gràfica...")
    app = InterficieGrafica(root)
    print("6. Interfície gràfica inicialitzada.")

    # Executar el bucle principal
    print("7. Executant el bucle principal de l'aplicació...")
    root.mainloop()
    print("8. Bucle principal finalitzat.")

if __name__ == "__main__":
    iniciar_aplicacio()