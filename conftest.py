from selenium import webdriver # Importar Selenium
from webdriver_manager.chrome import ChromeDriverManager # Importar Webdriver Manager
from selenium.webdriver.chrome.service import Service as ChromeService # Importar ChromeService
import pytest # Import Pytest





# @ 
@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # Config Chrome como default browser para Test.
    driver.maximize_window() # Maximiza ventana
    yield driver 
    driver.quit()


