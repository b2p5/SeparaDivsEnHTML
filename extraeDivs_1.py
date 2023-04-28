from bs4 import BeautifulSoup

# Abre el archivo HTML
with open("ejemplo.html", "r") as f:
    # Lee el contenido del archivo
    html = f.read()

# Crea un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, "html.parser")

# Encuentra todos los elementos div
divs = soup.find_all("div")

# Crea un diccionario para almacenar los niveles de cada div
niveles = {}

# Función recursiva para obtener el nivel de un elemento div
def obtener_nivel(div, nivel):
    # Agrega el nivel actual del div al diccionario
    niveles[str(div)] = nivel
    # Recorre todos los div hijos del div actual
    for hijo in div.find_all("div"):
        # Llama recursivamente a la función para obtener el nivel del hijo
        obtener_nivel(hijo, nivel + 1)

# Llama a la función para obtener los niveles de todos los divs
for div in divs:
    obtener_nivel(div, 0)

# Muestra los niveles de los divs ordenados por su jerarquía
for div, nivel in sorted(niveles.items(), key=lambda x: x[1]):
    print("  " * nivel + str(div))
