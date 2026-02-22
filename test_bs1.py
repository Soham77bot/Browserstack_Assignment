from selenium import webdriver

driver = webdriver.Remote(
    command_executor="https://sohamshivpuje_mMOpY2:eswHZxTxQxDSKSyx4uhB@hub-cloud.browserstack.com/wd/hub",
    options=webdriver.ChromeOptions()
)

print("Session:", driver.session_id)
driver.quit()