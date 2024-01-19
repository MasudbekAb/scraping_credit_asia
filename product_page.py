import requests
from bs4 import BeautifulSoup

class Additional:
    def get_product_data(self, link=''):
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        section = soup.find("div", class_='configuration')
        items = section.find_all('div', class_='configuration-item')
        characteristics = {}
        for item in items:
            details = item.find('div', class_='configuration-item-row-detail')
            title = details.find('span', class_='title').get_text()
            info = details.find('span', class_='info').get_text(strip=True)
            characteristics.update({title: info})
        info_product = soup.find('div', class_='info-producct')
        description = info_product.find('div', class_='detail__info-card').get_text()
        return characteristics, description


q = Additional()
q.get_product_data(link='https://www.creditasia.uz/product/smartfon-apple-iphone-15-pro-max-512gb-black-titanium-mu7c3rx-a/')