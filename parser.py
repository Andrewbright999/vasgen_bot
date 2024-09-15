import requests
from bs4 import BeautifulSoup

# URL страницы, которую нужно загрузить
url = 'https://example.com'

# Отправляем GET-запрос на URL
response = requests.get(url)

# Проверяем статус-код ответа (200 означает успешное получение страницы)
if response.status_code == 200:
    # Получаем полный HTML-код
    html_content = response.text
    
    # Создаем объект BeautifulSoup для более удобной работы с HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Выводим весь HTML-код
    print(soup.prettify())
else:
    print(f"Ошибка: не удалось загрузить страницу. Статус-код: {response.status_code}")
