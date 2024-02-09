import requests
from bs4 import BeautifulSoup

url = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'

def articleContents(url):
    response = requests.get(url)

    if response.status_code == 200:
        soap = BeautifulSoup(response.text, 'html.parser')

        titles = soap.find('h1').get_text()

        paragraphs = soap.find_all('p')

        content = '/n'.join([paragraph.get_text() for paragraph in paragraphs])
        return titles, content
    else:
        print("Failed to fetch the request")
        return None,None
    
    # Get the article title and content
title, content = articleContents(url)

# Display the results
if title and content:
    print(f"Title: {title}\nContent:\n{content}")
else:
    print("Failed to retrieve article information.")