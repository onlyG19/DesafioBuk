from pages.Base import Base
from selenium.webdriver.common.by import By

# Index Page
# Página index ' home. 

class IndexPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demoblaze.com/index.html")
        
    
    # Localiza mediante método click la catégoria de Laptops y clickea.
    
    def select_laptops(self):
        self.click((By.XPATH,"//a[text()='Laptops']"))
        
        
    # Selecciona el producto, dando click a su nombre (laptopName)    
    def select_specific_laptop(self, laptopName):
        self.click((By.XPATH, f"//a[text()='{laptopName}']"))
        

    # Accede a la opcion de nombre navbarOptionName si esta es localizada.
    def click_navbar_option(self, navbarOptionName):
        self.click((By.XPATH, f"//a[text()='{navbarOptionName}']"))
        
    