from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração para diferentes navegadores
def test_portability(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()

    driver.get("http://seu-site-ecommerce.com")
    try:
        # Verificar exibição do produto
        driver.find_element(By.CLASS_NAME, "product-list").is_displayed()
        print(f"Exibição correta em {browser_name}")
    except:
        print(f"Erro de exibição em {browser_name}")
    driver.quit()

# Executando em diferentes navegadores
for browser in ["chrome", "firefox", "safari"]:
    test_portability(browser)
