from pages.Base import Base
from selenium.webdriver.common.by import By



class LaptopPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        
    # Localiza el boton de Add to cart
    # luego le da click.
    
    def add_to_cart(self):
        self.click((By.XPATH,"//a[text()='Add to cart']")) # 
        
        
