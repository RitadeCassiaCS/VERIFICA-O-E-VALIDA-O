import requests

def penetration_test():
    url = "http://seu-site-ecommerce.com/login"
    # Tentativa de login com dados inválidos
    response = requests.post(url, data={"username": "admin", "password": "wrongpass"})
    
    if response.status_code == 403:
        print("Acesso não autorizado bloqueado com sucesso.")
    else:
        print("Falha na segurança: acesso não autorizado permitido.")

penetration_test()

