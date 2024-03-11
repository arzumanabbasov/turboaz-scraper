import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
BASE_DIR = 'C://Users/Admin/Desktop/Projects/TurboAzScraper/'


def get_links():
    base_url = 'https://turbo.az/autos?page='
    links_file_path = BASE_DIR + 'data/raw/links.txt'
    with open(links_file_path, 'w') as links_file:
        current_page = 1
        driver.get(base_url)
        last_page = int(driver.find_element(By.CSS_SELECTOR, 'span.last > a').get_attribute('href').split('=')[-1])

        while current_page <= last_page:
            driver.get(base_url + str(current_page))
            time.sleep(3)
            ad_links = driver.find_elements(By.CSS_SELECTOR, 'a.products-i__link')
            if not ad_links:
                print("No advertisements found, reached the last page.")
                break

            urls = [link.get_attribute('href') + '\n' for link in ad_links]
            links_file.writelines(urls)

            current_page += 1


if __name__ == "__main__":
    get_links()
