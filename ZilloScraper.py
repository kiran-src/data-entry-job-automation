import requests
from bs4 import BeautifulSoup
import pprint


class ZilloScraper:
    def __init__(self, url):
        self.apartment_entries = []
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie": "PHPSESSID=8mepqprupj2qqvjtmnohhhf3v2; _ga=GA1.2.443508061.1643832570; _gid=GA1.2.1131766731.1643832570",
            "Authority": "zillow.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
        }
        self.site = requests.get(url, headers=self.headers)
        print(f"Code status: {self.site}")
        self.soup = BeautifulSoup(self.site.text, 'html.parser')

    def scrape_apartments(self):
        # Scrape through page to obtain each element containing an ad for an apartment on the website.
        more_pages = True
        count = 0
        while more_pages:
            page_ads = self.soup.select(selector='ul.photo-cards li')
            print(f"{count}, Page Ads {page_ads}")
            [self.register_entry(i) for i in page_ads]

            more_pages = self.turn_page()
            count +=1
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
        print(f"\tNew Entry: {apartment_entry}")
        self.apartment_entries.append(apartment_entry)

    def fill_form(self, form):
        for i in self.apartment_entries:
            form.form_entry(i)

    def turn_page(self):
        page = 0
        page_numbers = self.soup.select(selector="ul.PaginationList-c11n-8-62-4__sc-14rlw6v-0 li.gDZTHc")
        print(f"\tPage Numbers: {page_numbers}")
        for count, i in enumerate(page_numbers):
            print(f"\tTest i.get: {i.get('class')}")
            if i.get('class')[0] == "PaginationNumberItem-c11n-8-62-4__sc-bnmlxt-0":
                page == count + 1
                print(f"\t\tPage Number: {count} of {len(page_numbers)}")
                break
        if page == len(page_numbers):
            print(f"\tEnd of Pages")
            return False
        else:
            print(f"\t\tURL: {page_numbers[page].find(name='a').get('href')}")
            self.soup = BeautifulSoup(requests.get("https://www.zillow.com" + page_numbers[page].find(name='a').get('href')).text,
                                      'html.parser')
            print(f"\tNext Page")
            return True

    def test(self):
        for i in self.apartment_entries:
            pprint(i, indent=4)
