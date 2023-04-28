from bs4 import BeautifulSoup

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
        #if parents:
        #   print("Padre: " + " > ".join(str(parent) for parent in parents))
