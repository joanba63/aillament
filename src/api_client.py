import requests

# Claus d'API (substitueix amb les teves claus)
OPENWEATHERMAP_KEY = "clau"  # Clau d'OpenWeatherMap
OPENCAGEDATA_KEY = "la_teva_clau_opencagedata"  # Clau d'OpenCageData

def obtenir_dades_geogràfiques(ciutat):
    """Obté la latitud i la longitud d'una ciutat mitjançant OpenCageData."""
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={ciutat}&key={OPENCAGEDATA_KEY}"
        resposta = requests.get(url).json()
        if resposta.get("results"):
            latitud = resposta["results"][0]["geometry"]["lat"]
            longitud = resposta["results"][0]["geometry"]["lng"]
            return latitud, longitud
        else:
            raise ValueError(f"No s'ha pogut trobar la ciutat: {ciutat}. Resposta: {resposta}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error de connexió: {str(e)}")

def obtenir_dades_meteorològiques(latitud, longitud):
    """Obté les dades meteorològiques mitjançant OpenWeatherMap."""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={OPENWEATHERMAP_KEY}&units=metric"
        resposta = requests.get(url).json()
        if resposta.get("main"):
            temperatura = resposta["main"]["temp"]
            humitat = resposta["main"]["humidity"]
            clima = resposta["weather"][0]["description"]
            return temperatura, humitat, clima
        else:
            raise ValueError(f"No s'han pogut obtenir les dades meteorològiques. Resposta: {resposta}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error de connexió: {str(e)}")