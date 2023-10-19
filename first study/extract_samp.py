import requests
import os
from bs4 import BeautifulSoup
import re

output_directory = 'samp'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

link = []
for page_number in range(2, 30):
    url = f"https://radiosampaio.com.br/editoria/policia/page/{page_number}/"
    
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        links = soup.find('a', {'id': 'link-64-109216'})

        code = links
        link.append(code)

    else:
        print(f"error in {page_number}: Status {response.status_code}")

    if html:
        filepath = os.path.join(output_directory, f"samp_{page_number}.html")
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(html)
        print("HTML extraído com sucesso e salvo no arquivo ", f'samp_{page_number}.html')


filepath = os.path.join(output_directory, 'samp.txt')

i = 0
with open(filepath, 'w', encoding='utf-8') as file:
    for ended in link:
        file.write(ended + '\n')  