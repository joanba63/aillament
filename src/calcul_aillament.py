def calcular_aillament_termic(dades):
    """
    Calcula l'aïllament tèrmic en funció de les dades rebudes.
    Aquest és un exemple simplificat. Pots ajustar els càlculs segons les teves necessitats.
    """
    try:
        temperatura = float(dades["temperatura_media"])
        humitat = float(dades["humitat_relativa"])
        # Exemple de càlcul: Índex d'aïllament basat en temperatura i humitat
        index_aillament = (temperatura * 0.5) + (humitat * 0.3)
        return index_aillament
    except (KeyError, ValueError) as e:
        raise ValueError(f"Dades invàlides per al càlcul: {str(e)}")