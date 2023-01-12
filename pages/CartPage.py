from pages.Base import Base
from selenium.webdriver.common.by import By

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        

    # Clickea el boton Place Order  
    def place_order(self):
        self.click((By.XPATH,"//button[text()='Place Order']")) # 
        
        
    # Se llena el formulario Place Order.   inputs es un diccionario, su informacion a la hora de su uso tiene origen en data.json
    def set_place_order(self, **inputs):
        for item in inputs:
            self.find_element((By.XPATH, f"//input[@id='{item}']")).send_keys(inputs.get(item))
        
        self.click((By.XPATH,"//button[text()='Purchase']"))
        
    # Retorna el contenido de texto (str) que esta en La Alerta de ordern invalida.
    def return_invalid_order_alert(self) -> str:
        
        return self.return_alert_text()
        
        
    # Retorna el contenido de texto que surge al confirmar la compra
    def get_purchase_confirmation_text(self):
        return self.get_text((By.XPATH, "//div[contains(@class, 'sweet-alert')]/h2"))