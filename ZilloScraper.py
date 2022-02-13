import requests
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)

page_max = 13

class ZilloScraper:
    def __init__(self, addon):
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
        self.url_head = "https://www.zillow.com"
        self.url_end = addon
        self.site = requests.get(self.url_head+"/homes/for_rent/1-_beds/1_p/"+self.url_end, headers=self.headers)
        print(f"Code status: {self.site}")
        self.soup = BeautifulSoup(self.site.text, 'html.parser')

    def scrape_apartments(self):
        # Scrape through page to obtain each element containing an ad for an apartment on the website.
        more_pages = True
        count = 0
        while more_pages:
            page_ads = self.soup.select(selector='ul.photo-cards > li')
            for i in page_ads:
                if i.find(name='address', class_='list-card-addr') is not None\
                        and i.find(name='div', class_='list-card-price') is not None\
                        and i.find(name='a', class_='list-card-link') is not None:
                    self.register_entry(i)

            more_pages = self.turn_page()
            count +=1
        # Loop through all available pages and perform step 1 from each one
        # In each loop, call function to remove information from element to document
        pass

    def register_entry(self, element):
        # Remove information from BS element and enter it into the apartment entry list
        url = element.find(name='a', class_='list-card-link').get('href')
        if url[0] == '/':
            url = "https://www.zillow.com" + url
        apartment_entry = {
            'address': element.find(name='address', class_='list-card-addr').get_text(),
            'rent': element.find(name='div', class_='list-card-price').get_text(),
            'url': url
        }
        self.apartment_entries.append(apartment_entry)

    def fill_form(self, form):
        for i in self.apartment_entries:
            form.form_entry(i)

    def turn_page(self):
        page = 0
        page_numbers = self.soup.select(selector="ul.PaginationList-c11n-8-62-4__sc-14rlw6v-0 li.gDZTHc")
        print(f"\tPage Numbers: {page_numbers}")
        for count, i in enumerate(page_numbers):
            print(f"\t{count}. Test i.get: {i.get('class')} {i.find(name='a').get('href')}")
            # if i.get('class')[0] == "PaginationNumberItem-c11n-8-62-4__sc-bnmlxt-0":
            if i.get('aria-current') == 'page':
                page = count + 1
                print(f"\t\tPage Number: {page} of {len(page_numbers)}")
                break
        url_tail = page_numbers[page].find(name='a').get('href')
        if page == len(page_numbers) or url_tail == f'/homes/for_rent/1-_beds/{page_max}_p/':
            print(f"\tEnd of Pages")
            return False
        else:
            updated_url = self.url_head + url_tail
            print(f"\t\tURL{page}: {updated_url}")
            self.site = requests.get(updated_url, headers=self.headers)
            self.soup = BeautifulSoup(self.site.text, 'html.parser')
            print(f"\tNext Page {self.site}")
            return True

    def test(self):
        for i in self.apartment_entries:
            pp.pprint(i)
#
# https://www.zillow.com/homes/for_rent/1-_beds/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.55461173490573%2C%22north%22%3A37.995314418058285%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A712639%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%7D%2C%22isListVisible%22%3Atrue%7D
# https://www.zillow.com/homes/for_rent/1-_beds/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.85218275976563%2C%22east%22%3A-122.01447524023438%2C%22south%22%3A37.50342490969512%2C%22north%22%3A38.0461619281346%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A712639%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D
