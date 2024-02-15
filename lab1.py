from bs4 import BeautifulSoup
import requests as r

BASE_URL = "https://lnu.edu.ua/"
URL = f"{BASE_URL}/about/faculties/"


req = r.get(URL)


soup = BeautifulSoup(req.text, 'lxml')


ul_structural_units = soup.find('ul', class_='structural-units')

print(ul_structural_units.text)

ul_text = ul_structural_units.text.strip()

with open('lnu.txt', 'w', encoding='utf-8') as f:
    f.write(ul_text)


