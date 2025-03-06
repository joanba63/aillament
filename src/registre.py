import logging
import os

# Camí absolut al fitxer de log
log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "log.txt")

def configurar_log():
    """Configura el sistema de logs."""
    logging.basicConfig(
        filename=log_path,  # Camí absolut
        level=logging.DEBUG,  # Nivell de log més detallat
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def registrar_log(missatge, nivell="info"):
    """Registra un missatge en el fitxer de log."""
    if nivell.lower() == "info":
        logging.info(missatge)
    elif nivell.lower() == "error":
        logging.error(missatge)
    elif nivell.lower() == "warning":
        logging.warning(missatge)
    elif nivell.lower() == "debug":
        logging.debug(missatge)
    else:
        logging.info(missatge)  # Per defecte, registra com a info