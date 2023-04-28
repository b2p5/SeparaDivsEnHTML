##
##El programa es una función en Python que utiliza la biblioteca 
#   BeautifulSoup para analizar un archivo HTML y construir un diccionario 
#   que representa la jerarquía de todos los elementos "div" en el archivo.
##
##La función get_div_hierarchy toma como entrada el nombre de un 
#   archivo HTML y devuelve un diccionario que contiene cada elemento 
#   "div" en el archivo como clave y una lista de sus padres 
#   (elementos "div" que lo contienen) como valores.
##
##Para hacer esto, el programa utiliza la biblioteca BeautifulSoup 
#   para analizar el archivo HTML y encontrar todos los elementos 
#   "div" en el archivo. Luego, por cada "div" encontrado, busca todos 
#   sus padres "div" utilizando el método find_parent de BeautifulSoup. 
#   Cada padre "div" se agrega a una lista que se inserta en el diccionario 
#   de jerarquía, con la clave siendo el elemento "div" y el valor la 
#   lista de sus padres.
##
##La última parte del programa imprime la jerarquía para cada elemento 
#   "div" encontrado en el archivo HTML. Cada elemento "div" se imprime en 
#   una nueva línea y sus padres se imprimen debajo de él, separados por 
#   una flecha ">".
##

from bs4 import BeautifulSoup

## get_div_hierarchy
#   La entrada es el nombre de un archivo HTML y devuelve un diccionario que 
#   contiene cada elemento "div" en el archivo como clave 
#   y una lista de sus padres (elementos "div" que lo contienen) como valores.
def get_div_hierarchy(html_file):
    with open(html_file, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        divs = soup.find_all('div')
        hierarchy = {}

        for div in divs:
            hierarchy[div] = []
            parent = div.find_parent('div')
            while parent:
                hierarchy[div].insert(0, parent)
                parent = parent.find_parent('div')

    return hierarchy

if __name__ == '__main__':
    html_file = "ejemplo.html"
    hierarchy = get_div_hierarchy(html_file)

    for div, parents in hierarchy.items():
        print("\n" + str(div))
        #A continuación  imprime el padre del div actual
        #if parents:
        #   print("Padre: " + " > ".join(str(parent) for parent in parents))
