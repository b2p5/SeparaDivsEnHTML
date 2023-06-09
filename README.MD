# Programa que extrae divs de un archivo HTML

Este programa está hecho en **Python** y utiliza la librería **BeautifulSoup** para analizar un archivo HTML y obtener todos los elementos div presentes en él.

## Uso

Para utilizar el programa, sigue los siguientes pasos:

1. Guarda el archivo HTML que quieres analizar en la misma carpeta que el archivo `extraeDivs.py`.
2. Abre una terminal y navega hasta la carpeta donde se encuentran los archivos.
3. Ejecuta el programa con el siguiente comando: 

`python extraeDivs.py ejemplo.html`

Donde `ejemplo.html` es el nombre del archivo que quieres analizar.

4. El programa te mostrará una jerarquía de niveles de div en función de su anidación en el documento HTML.

## Ejemplo

Supongamos que queremos analizar el siguiente archivo HTML:

```
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <div id="primer_div_Nivel1">
            <div id="div_Nivel2">
                <div id="div_Nivel3">
                    <p>Esto es un párrafo</p>
                </div>
            </div>
        </div>
        <div id="segundo_div_Nivel1">
            <p>Esto es otro párrafo</p>
        </div>
    </body>
</html>
```


### El resultado del programa sería el siguiente:

```
<div id="primer_div_Nivel1">
    <div id="div_Nivel2">
        <div id="div_Nivel3">
            <p>Esto es un párrafo</p>
        </div>
    </div>
</div>

<div id="div_Nivel2">
    <div id="div_Nivel3">
        <p>Esto es un párrafo</p>
    </div>
</div>

<div id="div_Nivel3">
    <p>Esto es un párrafo</p>
</div>

<div id="segundo_div_Nivel1">
    <p>Esto es otro párrafo</p>
</div>

```

Como podemos ver ha separado todos los DIVs con sus contenidos.









