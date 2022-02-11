import requests
from bs4 import BeautifulSoup

ZILLO_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.55461173490573%2C%22north%22%3A37.995314418058285%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A712639%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'


class ZilloScraper:
    def __init__(self):
        self.apartment_entries = []
        self.site = requests.get(ZILLO_URL)
        self.soup = BeautifulSoup(self.site.text, 'html.parser')

    def scrape_apartments(self):
        # Scrape through page to obtain each element containing an ad for an apartment on the website.
        more_pages = True
        while True:
            page_ads = self.soup.select('ul.photo-cards li')
            (self.register_entry(i) for i in page_ads)

            more_pages = self.turn_page()


        # Loop through all available pages and perform step 1 from each one
        # In each loop, call function to remove information from element to document
        pass

    def register_entry(self, element):
        # Remove information from BS element and enter it into the apartment entry list
        apartment_entry = {
            'address': "",
            'rent': "",
            'url': ""
        }
        self.apartment_entries.append(apartment_entry)

    def fill_form(self, form):
        for i in self.apartment_entries:
            form.form_entry(i)

    def turn_page(self):
        page = 0
        page_numbers = self.soup.select("ul.PaginationList-c11n-8-62-4__sc-14rlw6v-0 li.gDZTHc")
        for count, i in enumerate(page_numbers):
            if i.get('class') == "PaginationNumberItem-c11n-8-62-4__sc-bnmlxt-0":
                page == count + 1
                break
        if page == len(page_numbers):
            return False
        else:
            self.soup = BeautifulSoup(requests.get("https://www.zillow.com" + page_numbers[page].get('href')),
                                      'html.parser')
            return True
