import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from config import (
    OPINION_SECTION,
    NUM_ARTICLES,
    USE_BROWSERSTACK,
    BROWSERSTACK_USERNAME,
    BROWSERSTACK_ACCESS_KEY
)

# ==============================
# DRIVER CREATION
# ==============================

from selenium.webdriver.remote.client_config import ClientConfig

def create_driver(browser_config=None):

    if not USE_BROWSERSTACK:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        return driver

    print("Running on BrowserStack Cloud...")
    print("Browser Config Received:", browser_config)

    options = webdriver.ChromeOptions()

    options.set_capability("browserName", browser_config["browserName"])
    options.set_capability("browserVersion", browser_config["browserVersion"])
    options.set_capability("bstack:options", {
        "os": browser_config["os"],
        "osVersion": browser_config["osVersion"],
        "sessionName": browser_config["sessionName"],
        "buildName": "CE Assignment Build"
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESSKEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    print("Session ID:", driver.session_id)
    return driver


# ==============================
# SCRAPE ARTICLES
# ==============================

def scrape_articles(browser_config=None):

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import StaleElementReferenceException
    import time

    articles_data = []

    # Create ONE driver per browser
    driver = create_driver(browser_config)

    try:
        # Open main page
        driver.get(OPINION_SECTION)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )

        headlines = driver.find_elements(By.CSS_SELECTOR, "h2 a")

        article_links = []
        for element in headlines:
            try:
                link = element.get_attribute("href")
                if link and "/opinion/" in link:
                    article_links.append(link)
            except StaleElementReferenceException:
                continue

        # Remove duplicates and limit number of articles
        article_links = list(dict.fromkeys(article_links))[:NUM_ARTICLES]

        # Visit each article using SAME DRIVER
        for link in article_links:

            driver.get(link)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )

            try:
                title = driver.find_element(By.TAG_NAME, "h1").text.strip()
            except StaleElementReferenceException:
                continue

            clean_paragraphs = []

            paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")

            for i in range(len(paragraphs)):
                try:
                    # Re-fetch element to avoid stale reference
                    p = driver.find_elements(By.CSS_SELECTOR, "article p")[i]
                    text = p.text.strip()

                    if text and "cookie" not in text.lower():
                        clean_paragraphs.append(text)

                except StaleElementReferenceException:
                    continue

            content = " ".join(clean_paragraphs[:5])

            if len(content) < 50:
                continue

            articles_data.append({
                "title": title,
                "content": content
            })

            time.sleep(2)  # small delay for stability

        # Keep session visible briefly
        time.sleep(5)

    finally:
        driver.quit()

    return articles_data
