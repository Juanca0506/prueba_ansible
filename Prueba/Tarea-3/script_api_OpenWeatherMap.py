import requests
import json

# Define la clave de la API y la ciudad para la consulta
API_KEY = '5bdad9ff366db4dac7d46c9d00d686f9'  # Reemplaza con tu propia clave de API de OpenWeatherMap
CITY = 'Medellin'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Función para obtener datos del clima desde la API
def get_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta tiene un error HTTP
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Función para almacenar datos en un archivo JSON
def save_to_json(data, filename='weather_data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Función para generar un archivo HTML con los datos del clima
def generate_html(data, filename='weather_report.html'):
    html_content = f"""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte del Clima</title>
</head>
<body>
    <h1>Reporte del Clima</h1>
    <h2>Clima en Medellin</h2>
    <p><strong>Temperatura:</strong> 25°C</p>
    <p><strong>Clima:</strong> Nublado</p>
    <p><strong>Humedad:</strong> 80%</p>
    <p><strong>Viento:</strong> 3.5 m/s</p>
    <footer>
        <p>Datos proporcionados por OpenWeatherMap</p>
    </footer>
</body>
</html>
    """
    with open(filename, 'w') as html_file:
        html_file.write(html_content)

# Ejecutar funciones
if __name__ == "__main__":
    weather_data = get_weather_data(URL)
    if weather_data:
        save_to_json(weather_data)
        generate_html(weather_data)
        print("Datos guardados y archivo HTML generado con éxito.")
    else:
        print("No se pudieron obtener los datos del clima.")
