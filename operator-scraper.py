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

github_urls = []
for url in operator_urls:
    driver.get(url)
    time.sleep(2)
    try:
        f = open("gh-urls.txt","a")
        github = driver.find_element(By.XPATH, '//h5[text()="Repository"]/..//a').get_attribute("href")
        github_urls.append(github)
        f.write(f"{github}\n")
        f.close()
    except Exception as err:
        print(f"error finding github address for operator {url}, error: {err}")
        continue
    print(f"{url} -> {github}")


for url in github_urls:
    driver.get(url)
    time.sleep(2)
    try: 
        f = open("languages.txt", "a")
        languages = driver.find_elements(By.XPATH, '//h2[text()="Languages"]/..//span/span')
        f.write(f"{url} languages:\n")
        print(f"{url} languages:")
        for l in languages:
            l_percentage = l.get_attribute("aria-label")
            f.write(f"- {l_percentage}\n")
            print(f"- {l_percentage}")
        f.close()
    except:
        print(f"error getting languages for github {url}")
        continue

# Close the browser when we're done.
driver.quit()
