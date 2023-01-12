from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


# Clase Base.    
# Principalmente, conjunto de Metodos que reunen diversas utilidades de Selenium, por ejemplo: find_element, click, accept alert
class Base:

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver


    # Clickea el elemento,si este es localizado mediante Metodo find_element
    def click(self, by_locator, timeout=10, any_available=False):

        element = self.find_element(by_locator, timeout, any_available)
        element.click()

    # Metodo que retorna el elemento localizado, dado un metodo de localizacion. 
    #            Ejemplo de llamado al metodo/funcion:      find_element((By.XPATH, f"//input[@id='{item}']"))
    def find_element(self, by_locator, timeout=10, any_available=False, any_present=False, message=None):

        if any_available:
            element = WebDriverWait(self.driver, int(timeout)).until(EC.visibility_of_any_elements_located(by_locator),
                message='No elements available by address {}'.format(by_locator))
            return element[0]
        elif any_present:
            element = WebDriverWait(self.driver, int(timeout)).until(EC.presence_of_element_located(by_locator),
                message='No elements available by address {}'.format(by_locator))
            return element
        else:
            element = WebDriverWait(self.driver, int(timeout)).until(EC.visibility_of_element_located(by_locator),
                    message='Element has not been found' if not message else message)
            return element

    
    def get_text(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, int(timeout)).until(EC.visibility_of_element_located(by_locator),
            message='Element has not been found').text
    # Metodo para aceptar la alerta en browser.
    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    # Metodo que retorna el texto de una eventual alerta en browser
    def return_alert_text(self) -> str:
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return self.driver.switch_to.alert.text