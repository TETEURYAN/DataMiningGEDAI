import os
import json
import requests
from bs4 import BeautifulSoup

def fetch_and_save_html_from_file(input_file, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    arr = []
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines, 1):
            link = line.strip() 
            try:
                response = requests.get(link)
                response.raise_for_status()  

                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                author = soup.find("span", class_ = "author-name").find("a").text
                title = soup.find("title").text
                date = soup.find("time")["datetime"]
                description = soup.find("meta", {"name": "description"})

                if description:
                    description = description.get("content")

                data = {
                    "title":title,
                    "author" : author,
                    "date": date,
                    "description": description,
                    "url" : link}
                
                arr.append(data)
                
                print(f"HTML da página {index} ({link}) salvo")
            except Exception as e:
                print(f"Ocorreu um erro ao processar {link}: {e}")

            general = os.path.join(output_directory, f'page_CST_{index}.html')
            with open(general, 'w', encoding='utf-8') as html_file:
                html_file.write(html)    

    filename = 'cst.json'
    filepath = os.path.join(output_directory, filename)
    with open(filepath, 'w', encoding='utf-8') as json_file:
        json_object = json.dumps(arr, indent= 4)
        json_file.write(json_object)

if __name__ == "__main__":
    input_file = "general.txt"  
    output_directory = "cst"  

    fetch_and_save_html_from_file(input_file, output_directory)
