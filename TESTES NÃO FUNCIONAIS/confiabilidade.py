import requests
import time

def monitor_availability():
    url = "http://seu-site-ecommerce.com"
    start_time = time.time()
    downtime = 0

    while time.time() - start_time < 86400:  # 24 horas
        response = requests.get(url)
        
        if response.status_code != 200:
            downtime += 1
            print("Sistema fora do ar!")
        
        time.sleep(60)  # Checa a cada minuto

    uptime_percentage = ((86400 - downtime * 60) / 86400) * 100
    print(f"Disponibilidade: {uptime_percentage}%")

monitor_availability()

