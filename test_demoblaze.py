from pages.IndexPage import IndexPage
from pages.LaptopPage import LaptopPage
from pages.CartPage import CartPage
from utils import load_data
import pytest 

from time import sleep



# Se carga la información de data.json en variable 'data'
data = load_data("data/data.json")



# Test #1 y #2
# Test || Add to Cart 
# Descripcion: Se testea la funcionalidad de poder seleccionar un producto de la categoria Laptops y finalizar su compra en el Cart (Carrito-Carro de Compras)
@pytest.mark.parametrize("info_place_order", data['valid_data'])
def test_add_to_cart(init_driver, info_place_order):
    
    # Index Page
    index_page = IndexPage(init_driver) # 

    index_page.select_laptops() # Acceder categoria Laptops
    index_page.select_specific_laptop("MacBook Pro") # Seleccionar producto determinado mediante su nombre, en este caso se testea con el producto 'MacBook Pro'

    
    # Laptop Page
    laptop_page = LaptopPage(init_driver) 

    laptop_page.add_to_cart() # Se clickea el boton de Add to Cart (añadir al carro de compras)
    
    laptop_page.accept_alert() # Se acepta la alerta emergente
    
    
    # Click Opcion "Cart" 
    index_page.click_navbar_option("Cart")
    
    
    # Cart Page
    cart_page = CartPage(init_driver)

    cart_page.place_order()   # Accede al formulario de Place Order
    
    #                            Se llena el Formulario Place Order para la compra
    cart_page.set_place_order(name=info_place_order.get("name"), country=info_place_order.get("country"), city=info_place_order.get("city"),card=info_place_order.get("card"),month= info_place_order.get("month"), year=info_place_order.get("year") )
    
    # Para verificar 
    # sleep(3)   
    
    
    assert cart_page.get_purchase_confirmation_text() == info_place_order.get("expected_text"), "el mensaje mostrado no es el correcto"
    
    
    
#   Test #3
# En este Test se testea el caso Negativo en que la compra no se realiza ya que en el formulario de Place Order se llena con informacion invalida (data['invalid_data']  ->     data.json | file)
@pytest.mark.parametrize("info_place_order", data['invalid_data'])
def test_add_to_cart_invalid_data(init_driver, info_place_order):
    index_page = IndexPage(init_driver)

    index_page.select_laptops()
    index_page.select_specific_laptop("MacBook Pro")

    
    laptop_page = LaptopPage(init_driver)

    laptop_page.add_to_cart()
    
    laptop_page.accept_alert()
    
    index_page.click_navbar_option("Cart")
    
    
    cart_page = CartPage(init_driver)

    cart_page.place_order()
    cart_page.set_place_order(name=info_place_order.get("name"), country=info_place_order.get("country"), city=info_place_order.get("city"),card=info_place_order.get("card"),month= info_place_order.get("month"), year=info_place_order.get("year") )
    
    
    # Se verifica con assert que el contenido de texto de la orden invalida coincida con el mensaje esperado ("expected_test").
    # Si esto es True, entonces se testea el correcto funcionamiento del caso Negativo.
    assert cart_page.return_invalid_order_alert() == info_place_order.get("expected_text"), "el mensaje mostrado no es el correcto"
    
