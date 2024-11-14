from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Configuração do Selenium WebDriver
driver = webdriver.Chrome()

# Iniciar teste de usabilidade
def monitor_user_interaction():
    driver.get("http://site-do-ecommerce.com")
    
    # Simulação de navegação
    driver.find_element(By.ID, "search-bar").send_keys("Product Name")
    driver.find_element(By.ID, "search-button").click()
    
    # Adicionar ao carrinho
    driver.find_element(By.CLASS_NAME, "product-item").click()
    driver.find_element(By.ID, "add-to-cart").click()
    
    # Finalizar compra
    driver.find_element(By.ID, "cart").click()
    driver.find_element(By.ID, "checkout").click()
    
    print("Interação monitorada com sucesso")

# Rodar o script individualmente para cada usuário
monitor_user_interaction()
driver.quit()

