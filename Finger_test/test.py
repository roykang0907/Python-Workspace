import requests

TOKEN = "8742370545:AAEXenn6jmiZXU5IPdrZEh4I1-92b4UyZ7A"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
response = requests.get(url)

print(response.json())