from GoogleForm import GoogleForm
from ZilloScraper import ZilloScraper

import os


ZILLOW_URL = '?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.55461173490573%2C%22north%22%3A37.995314418058285%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A712639%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'
DRIVER_PATH = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdImEVrF1ItqwTMHLVGYLb0dZB3iJEFXljySqA5YMTDcvcApQ/viewform?usp=sf_link'
aa = ''
# gf = GoogleForm(DRIVER_PATH, FORM_URL)
zs = ZilloScraper(ZILLOW_URL)

zs.scrape_apartments()
# zs.fill_form(gf)
zs.test()
