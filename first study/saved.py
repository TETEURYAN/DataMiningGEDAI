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
            link = line.strip()  # Remove espaços em branco e quebras de linha
            try:
                response = requests.get(link)
                response.raise_for_status()  # Verificar se a resposta foi bem-sucedida

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
                # Salvar o HTML em um arquivo
                
                print(f"HTML da página {index} ({link}) salvo")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao fazer a solicitação para {link}: {e}")
            except Exception as e:
                print(f"Ocorreu um erro ao processar {link}: {e}")
    filename = 'general.json'
    filepath = os.path.join(output_directory, filename)
    with open(filepath, 'w', encoding='utf-8') as json_file:
        json_object = json.dumps(arr, indent= 4)
        json_file.write(json_object)

if __name__ == "__main__":
    input_file = "general.txt"  # Substitua pelo caminho do arquivo de texto com os links
    output_directory = "saved_html"  # Diretório para salvar o HTML das páginas

    fetch_and_save_html_from_file(input_file, output_directory)
