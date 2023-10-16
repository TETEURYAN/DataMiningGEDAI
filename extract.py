import requests

def extract_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida (status 2xx)

        html = response.text
        return html
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer a solicitação:", e)
        return None

# URL da página que você deseja extrair o HTML
url = "https://www.chicosabetudo.com.br/?s=seguran%C3%A7a+homic%C3%ADdio"

html = extract_html(url)

if html:
    # Agora, você tem o HTML da página na variável 'html'
    # Você pode fazer o que quiser com ele, como analisá-lo ou salvá-lo em um arquivo
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(html)
    print("HTML extraído com sucesso e salvo no arquivo 'page.html'")