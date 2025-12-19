#Библиотека requests используется для отправки HTTP-запросов
import requests

#Отправляем GET-запрос на публичный API
response = requests.get("https://api.github.com")

#Выводим статус ответа и часть данных
print("Статус код:", response.status_code)
print("Ответ от сервера:")
print(response.text[:200])  # выводим первые 200 символов
