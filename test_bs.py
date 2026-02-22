from selenium import webdriver

USERNAME = "sohamshivpuje_mMOpY2"
ACCESS_KEY = "eswHZxTxQxDSKSyx4uhB"

options = webdriver.ChromeOptions()
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "latest")
options.set_capability("bstack:options", {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Single Debug Test",
    "buildName": "Debug Build"
})

try:
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )
    print("Session Created:", driver.session_id)
    driver.quit()
except Exception as e:
    print("ERROR:", e)