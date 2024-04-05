from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.google.com")
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("Python scraping with Selenium")
    elem.send_keys(Keys.RETURN)

    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    for result in search_results:
        try:
            title = result.find_element(By.CSS_SELECTOR, "h3").text
            url = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            print("Title:", title)
            print("URL:", url)
            print()
        except Exception as e:
            print(e)

    driver.close()


if __name__ == "__main__":
    main()
