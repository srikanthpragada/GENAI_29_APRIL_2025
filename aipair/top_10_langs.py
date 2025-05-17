# list top 10 programming languages from tiobe.com
import requests
from bs4 import BeautifulSoup   

def get_top_10_languages():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the programming languages
    table = soup.find('table', {'class': 'table table-striped table-hover table-bordered'})

    # Extract the top 10 languages
    languages = []
    for row in table.find_all('tr')[1:11]:  # Skip the header row and get the next 10 rows
        cols = row.find_all('td')
        language = cols[1].text.strip()
        languages.append(language)

    return languages

if __name__ == "__main__":
    top_languages = get_top_10_languages()
    print("Top 10 Programming Languages from TIOBE Index:")
    for i, lang in enumerate(top_languages, start=1):
        print(f"{i}. {lang}")

        