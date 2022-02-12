from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class GoogleForm:
    def __init__(self, path, url):
        self.s = Service(path)
        self.driver = webdriver.Chrome(service=self.s)
        self.url = url
        self.driver.get(self.url)

    def form_entry(self):
        pass