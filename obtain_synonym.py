from bs4 import BeautifulSoup
import requests


def extract_synonyms(word, how_many):
    link = 'https://www.thesaurus.com/browse/' + word
    page = requests.get(link)
    print('Made request!')
    soup = BeautifulSoup(page.content, 'html.parser')
    # soup.find('div':'synonyms-container css-429zho e1991neq0')
    all_li = soup.find("ul", {"class": "css-1lc0dpe et6tpn80"})
    cnt = 0
    syn_list = []
    if all_li is None:
        return []
    for el in all_li:
        print(el.get_text())
        syn_list.append(el.get_text())
        cnt += 1
        if cnt >= how_many:
            break
    return syn_list
    # print(soup.contents)


# extract_synonyms('love', 4)
