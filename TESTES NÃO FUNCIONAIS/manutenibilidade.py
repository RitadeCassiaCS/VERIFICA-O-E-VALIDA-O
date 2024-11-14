from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_updated_module():
    driver.get("http://seu-site-ecommerce.com/updated-feature")
    try:
        # Verifica o novo módulo
        driver.find_element(By.ID, "updated-feature").is_displayed()
        print("Novo módulo funcionando corretamente.")
    except:
        print("Erro no módulo atualizado.")
    
    # Verifica funcionalidades existentes
    driver.get("http://seu-site-ecommerce.com/other-feature")
    try:
        driver.find_element(By.ID, "other-feature").is_displayed()
        print("Funcionalidade existente intacta.")
    except:
        print("Erro em funcionalidade existente.")
    
test_updated_module()
driver.quit()
