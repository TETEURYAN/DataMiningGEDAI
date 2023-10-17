import os
import requests
from bs4 import BeautifulSoup


def extract_https_links(html):
    https_links = []

    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a', href=True):
        url = link['href']
        if url.startswith('https://www.chicosabetudo.com.br/policia'):
            https_links.append(url)

    return https_links

def write_links_to_file(links, output_file):
    filepath = os.path.join(output_directory, output_file)
    with open(filepath, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

def fetch_and_extract_links_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html = file.read()

        https_links = extract_https_links(html)

        return https_links
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    file_path = "page.html" 
    output_file = "cst.txt"
    output_directory = 'saved_html'

    https_links = fetch_and_extract_links_from_file(file_path)

    if https_links:
        print("Links HTTPS encontrados:")
        for link in https_links:
            print(link)

        write_links_to_file(https_links, output_file)
        print(f"Links escritos em '{output_file}'")
