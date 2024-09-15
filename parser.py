from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Указываем путь к драйверу вашего браузера (например, для Chrome)
chrome_options = Options()
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)
# Открываем страницу
driver.get('https://fastflux.ai/')  # Замените на нужный URL

# Получение всех куки на странице
cookies = driver.get_cookies()
print("Текущие куки:", cookies)

# Закрываем браузер
driver.quit()
