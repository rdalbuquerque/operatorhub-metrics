import time
import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode.
driver = webdriver.Chrome(
    executable_path="chromedriver.exe",
    options=chrome_options,
)

driver.get("https://operatorhub.io")
time.sleep(1)
elems = driver.find_elements(By.CSS_SELECTOR, "a.catalog-tile-pf")
operator_urls = []
for e in elems:
    operator_urls.append(e.get_attribute("href"))
for url in operator_urls:
    driver.get(url)
    time.sleep(2)
    try:
        github = driver.find_element(By.XPATH, '//h5[text()="Repository"]/..//a').get_attribute("href")
    except:
        print("error finding element")
    print(f"{url} -> {github}")

# Close the browser when we're done.
driver.quit()
