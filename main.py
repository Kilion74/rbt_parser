import bs4
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

count = 1
while count <= 17:
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options) as driver:  # Открываем хром
        driver.get(f"https://www.rbt.ru/cat/cifrovye_ustroistva/smartfony/~/page/{count}/")  # Открываем страницу
        time.sleep(3)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

        heads = soup.find_all('div', class_='item-catalogue catalogue-list-item')
        print(len(heads))
        for head in heads:
            name = head.find('a',
                             class_='link link_theme_item-catalogue link_underline-color_orange link_size_b item-catalogue__item-name-link')
            print(name.text.strip())
            price = head.find('div',
                              class_='price__row price__row_current text_bold text')
            print(price.text.strip())
            params = head.find_next('div', class_='item-catalogue__attributes').find_all('div',
                                                                                         class_='item-catalogue__attribute text')
            print(' '.join(params[0].text.strip().split()))
            print(' '.join(params[1].text.strip().split()))
            cyaract = head.find_next('div', class_='item-catalogue__attributes').find_all('div',
                                                                                          class_='item-catalogue__attribute item-catalogue__attribute_hidden text')
            print(' '.join(cyaract[0].text.strip().split()))
            print(' '.join(cyaract[1].text.strip().split()))
            nalichiye = head.find_next('div', class_='item-availability__container')
            print(nalichiye.text.strip())
            pix = head.find_next('div', class_='item-catalogue__image').find('img').get('src')
            print('https:' + pix)
            url = head.find_next('div', class_='item-catalogue__image').find('a').get('href')
            print('https://www.rbt.ru'+url)
            print('\n')
    count = count + 1
    print(count)
