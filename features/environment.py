from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, browser='chrome'):
    """
    :param context: Behave context
    :param browser: Browser name ('chrome' or 'firefox')
    """
    if browser == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    context.driver.implicitly_wait(4)
    context.driver.maximize_window()
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    if 'browser_firefox' in scenario.effective_tags:
        browser_init(context, browser='firefox')
    else:
        browser_init(context, browser='chrome')


def before_step(context, step):
    print('\nStarted step:', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step)


def after_scenario(context, feature):
    context.driver.quit()
