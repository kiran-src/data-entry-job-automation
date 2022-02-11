import requests
from bs4 import BeautifulSoup


class ZilloScraper:
    def __init__(self, url):
        self.apartment_entries = []
        self.site = requests.get(url)
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
            'address': element.find(name='address', class_='list-card-addr').get_text(),
            'rent': element.find(name='div', class_='list-card-price').get_text(),
            'url': element.find(name='a', class_='list-card-link').get('href')
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
