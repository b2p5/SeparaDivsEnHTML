from bs4 import BeautifulSoup

# Ejemplo de código HTML para analizar
html = """
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <div id="primer_div_Nivel1">
            <div id="div_Nivel2">
                <div id="div_Nivel3">
                </div>
            </div>
        </div>
        <div id="segundo_div_Nivel1">
        </div>
    </body>
</html>
"""

# Carga el HTML en un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Busca todas las etiquetas div
divs = soup.find_all('div')

# Inicializa un diccionario para almacenar los div por niveles
divs_por_nivel = {}

# Itera a través de cada div y clasifícalos por nivel
for div in divs:
    # Encuentra el nivel actual del div contando cuántos padres tiene
    nivel = len(list(div.parents))
    
    # Agrega el div a la lista de divs para su nivel actual
    if nivel not in divs_por_nivel:
        divs_por_nivel[nivel] = []
    divs_por_nivel[nivel].append(div)

# Imprime los divs clasificados por niveles
for nivel, divs in divs_por_nivel.items():
    print(f"Divs de nivel {nivel}: {len(divs)}")
    for div in divs:
        print(div)
