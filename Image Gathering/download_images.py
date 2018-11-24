import re
import requests
from bs4 import BeautifulSoup
import os

site = 'https://www.bing.com/images/search?q=bed&qs=n&form=QBILPG&sp=-1&pq=bed&sc=8-3&sk=&cvid=E821383C4C7C488090F27F212D81CC83'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.findAll('img')

urls = [img['src'] for img in img_tags]

save_path = os.getcwd() + '\Training Images\Bed Images'


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if filename == None:
        print('Didn\'t work')
        pass
    else:
        print('getting image')
        complete_path = os.path.join(save_path, filename.group(1))
        with open(complete_path, 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
