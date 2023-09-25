# Selenium - Automatizando tarefas no navegador
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils import CHROME_DRIVER_PATH

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


def makeBrowser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser
