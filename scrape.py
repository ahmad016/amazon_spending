from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import time
from selenium.common.exceptions import NoSuchElementException


# Set up the Selenium WebDriver
debugging_port = "9222"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", f"localhost:{debugging_port}")
driver = webdriver.Chrome(options=chrome_options)

year = 2024
price_pattern = re.compile(r'\$\d+\.\d{2}')
continue_scraping = True

while year >= 2016:  # Assuming you want to stop at the year 2000
    driver.get(f"https://www.amazon.com/your-orders/orders?timeFilter=year-{year}")
    time.sleep(2)  # Wait for page to load
    print(f"Processing year: {year}")

    while continue_scraping:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        elements = soup.find_all('span', {'class': 'a-color-secondary value'})

        for element in elements:
            text = element.text.strip()
            if price_pattern.match(text):
                print(text)

        try:
            next_button = driver.find_element(By.CLASS_NAME, 'a-last').find_element(By.TAG_NAME, 'a')
            if next_button:
                next_button.click()
                time.sleep(2)
        except NoSuchElementException:
            break

    year -= 1
    continue_scraping = True

driver.quit()
