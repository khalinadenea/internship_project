import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def browser_init(context):
    """
    Initialize WebDriver for BrowserStack or local Chrome.
    """

    # Your BrowserStack credentials (hardcoded for now — remember to regenerate after!)
    bs_username = "khalinaboyce_n8dEj5"
    bs_access_key = "53JK7y5vHQiYM6WEJkxV"

    if bs_username and bs_access_key:
        print("✅ Running on BrowserStack...")

        options = webdriver.ChromeOptions()

        # BrowserStack capabilities
        options.set_capability('bstack:options', {
            "os": "Windows",                 # Change to "OS X" to test on Mac
            "osVersion": "11",
            "sessionName": "Cross-platform test",
            "buildName": "QA Automation Build",
            "userName": bs_username,
            "accessKey": bs_access_key
        })
        options.set_capability("browserName", "Chrome")
        options.set_capability("browserVersion", "latest")

        url = "https://hub-cloud.browserstack.com/wd/hub"
        context.driver = webdriver.Remote(command_executor=url, options=options)

    else:
        print("⚠️ Running locally in headless Chrome...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.implicitly_wait(4)
    context.driver.maximize_window()
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print(f"\n🚀 Starting scenario: {scenario.name}")
    browser_init(context)


def before_step(context, step):
    print(f"\n➡️  Starting step: {step.name}")


def after_step(context, step):
    if step.status == 'failed':
        print(f"\n❌ Step failed: {step.name}")


def after_scenario(context, scenario):
    print(f"\n✅ Finished scenario: {scenario.name}")
    if hasattr(context, 'driver'):
        context.driver.quit()
