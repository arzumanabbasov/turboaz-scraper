import time

import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
BASE_DIR = 'C://Users/Admin/Desktop/Projects/TurboAzScraper/'


def get_car_info(url: str):
    driver.get(url)
    car_info = {
        'Şəhər': None,
        'Market': None,
        'Marka': None,
        'Model': None,
        'Buraxılış ili': None,
        'Ban növü': None,
        'Rəng': None,
        'Fuel_type': None,
        'Mühərrik': None,
        'Yürüş': None,
        'Sürətlər qutusu': None,
        'Ötürücü': None,
        'New': None,
        'Seats': None,
        'Sahiblər': None,
        'Vəziyyəti': None,
        'Seller': None,
        'Seller comment': None,
        'Price': None,
        'ImageUrl': None
    }
    values = driver.find_elements(By.CSS_SELECTOR, "div.product-properties__i")
    for value in values:
        field_name = value.find_element(By.CSS_SELECTOR, 'label.product-properties__i-name').text.strip()
        field_value = value.find_element(By.CSS_SELECTOR, 'span.product-properties__i-value').text.strip()
        if field_name in car_info:
            car_info[field_name] = field_value
    try:
        car_info['Market'] = driver.find_element(By.CSS_SELECTOR, 'div.product-shop__owner-name').text.strip()
    except:
        pass
    try:
        car_info['Seller'] = driver.find_element(By.CSS_SELECTOR, 'div.product-owner__info-name').text.strip()
    except:
        pass
    try:
        car_info['Seller comment'] = driver.find_element(By.CSS_SELECTOR,
                                                         'div.product-description__content').text.strip()
    except:
        pass

    car_info['Price'] = driver.find_element(By.CSS_SELECTOR, 'div.product-price__i').text.strip()

    image = driver.find_element(By.CSS_SELECTOR, ".fotorama__img")
    image_url = image.get_attribute("src")
    car_info['ImageUrl'] = image_url

    return car_info


def main():
    links_file_path = BASE_DIR + 'data/raw/links.txt'
    with open(links_file_path, 'r') as links_file:
        urls = links_file.readlines()[1000:]
        car_infos = []
        for url in urls:
            car_infos.append(get_car_info(url))
            time.sleep(0.5)

            if len(car_infos) % 100 == 0:
                df = pd.DataFrame(car_infos)
                df.to_csv(BASE_DIR + 'data/raw/car_info.csv', index=False)

        df = pd.DataFrame(car_infos)
        df.to_csv(BASE_DIR + 'data/raw/car_info2.csv', index=False)


if __name__ == "__main__":
    main()
