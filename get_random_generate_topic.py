

import requests

url = 'https://www.conversationstarters.com/generator.php'

url = 'https://www.conversationstarters.com/random.php'

from time import sleep
from bs4 import BeautifulSoup



fp = open('topic.list', 'a')

while True:
    r = requests.post(url)
    if not r.status_code == 200:
       continue

    soup = BeautifulSoup(r.text, 'html.parser')
    fp.write(soup.get_text() + '\n')
    print(soup.get_text())
