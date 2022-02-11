from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DRIVER_PATH = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdImEVrF1ItqwTMHLVGYLb0dZB3iJEFXljySqA5YMTDcvcApQ/viewform?usp=sf_link'


class GoogleForm:
    def __init__(self):
        self.s = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.s)

    def form_entry(self):
        pass