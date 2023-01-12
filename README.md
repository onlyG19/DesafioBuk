# DesafioBuk
Repositorio que almacena proecto de Testing para solucionar Jr Desafío Técnico QA Engineer Buk.



 Simple Folder PATH  // Se detalla de forma general la utilidad y funcion de los archivos más importantes del projecto

\---
|
|   conftest.py       -> Archivo que presenta la configuracion inicial del driver
|   test_demoblaze.py   -> Archivo principal que almacena los Test a ejecutar.
|   utils.py          -> Archivo que contiene función para la carga correcta del archivo "data.json"
|   
|
|               
+---data                                -> Carpeta que almacena el contenido 'data.json'
|       data.json  -> Archivo que contiene almacenada información relevante para el Testing, por ejemplo: Informacion para rellenar el formulario de compra Place Order
|       
+---pages                                -> Carpeta que almacena las diversas clases Pages, referentes a las diversas paginas empleadas en el Test
|   |   Base.py        -> Clase Base. Contiene Metodos Reutilizables, principalmente de Selenium WebDriver
|   |   CartPage.py     -> Clase CartPage, contiene contenido referente a la página Cart o Carrito de Compras
|   |   IndexPage.py     -> Clase IndexPage, contiene contenido referente a la página Index, Inicio o Home.
|   |   LaptopPage.py   -> Clase LaptopPage, contiene contenido referente a la página de las Laptops. En donde se visualiza un unico producto de este tipo.
|     
|
|           
+---venv                                  -> Carpeta que almacena el Virtual Enviroment del proyecto.
    |
|   \---Scripts
|           activate        -> Archivo que se debe inicializar desde la CMD para activar el modo virtual enviroment (venv)
|           activate.bat
|           
|           
\---

