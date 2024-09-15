import os, time
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Укажите путь к вашему ChromeDriver
chrome_driver_path = "/opt/google/chrome/chromedriver"

# Укажите путь к папке для сохранения загруженных файлов
download_folder_path = os.path.dirname(os.path.realpath(__file__))
"/root/bots/vasgen_bot"


# Убедитесь, что папка существует, если нет, создайте её
if not os.path.exists(download_folder_path):
    os.makedirs(download_folder_path)

# Настраиваем параметры Chrome
chrome_options = Options()
chrome_prefs = {
    "download.default_directory": download_folder_path,  # Папка для загрузок
    "download.prompt_for_download": False,  # Отключаем запрос на подтверждение загрузки
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_experimental_option("prefs", chrome_prefs)

# Настраиваем Selenium для работы с Chrome
service = Service(ChromeDriverManager().install())
# Глобальный объект браузера
driver = None


def init_browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://fastflux.ai/")
        time.sleep(5)  # Ожидание загрузки сайта


def generate_image(prompt: str):
    global driver

    try:
        # Инициализируем браузер, если это еще не сделано
        if driver is None:
            init_browser()

        # Находим поле для ввода текста для промта
        prompt_input = driver.find_element(By.CSS_SELECTOR, '#root textarea')

        # Очищаем поле ввода
        prompt_input.clear()

        # Вводим промт
        prompt_input.send_keys(prompt)

        # Находим кнопку для генерации изображения и кликаем на неё
        generate_button = driver.find_element(By.CSS_SELECTOR, '#submit-btn-5dt')
        generate_button.click()

        # Ждем генерацию изображения
        time.sleep(3)  # Увеличиваем время ожидания, если это необходимо

        # Находим кнопку для скачивания изображения
        download_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.hidden.md\:block.max-w-\[1050px\].w-full.relative > button')
        download_button.click()

        # Ждем, пока изображение будет загружено
        time.sleep(3)  # Увеличиваем время ожидания

        # Путь к загруженному файлу
        files = os.listdir(download_folder_path)
        for file in files:
            if file.endswith(".webp"):  # Предполагаем, что исходный файл имеет расширение .webp
                old_file_path = os.path.join(download_folder_path, file)
                print(old_file_path)
                return old_file_path
                
                new_file_path = os.path.join(download_folder_path, "generated_image.jpeg")

                # Открываем изображение и сохраняем его в формате JPEG
                with Image.open(old_file_path) as img:
                    img.convert("RGB").save(new_file_path, "JPEG")

                # Удаляем исходный файл (если нужно)
                os.remove(old_file_path)
                return new_file_path

    except Exception as e:
        print(f"Ошибка при создании изображения: {e}")
        return e