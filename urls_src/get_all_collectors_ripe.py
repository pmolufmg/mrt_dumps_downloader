from bs4 import BeautifulSoup, SoupStrainer
import requests
import re


def get_ripe_collectors():
    url = "https://ris.ripe.net/docs/route-collectors/"

    ripe_collectors = []
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')

    collector_ripe = r"\/rrc[0-9]{2}"
    collector_ripe_c = re.compile(collector_ripe)


    for link in soup.find_all('a'):
        try:
            if collector_ripe_c.search(link.get('href')):
                ripe_collector_urls = link.get('href').split('/')[3]
                ripe_collectors.append(f"{ripe_collector_urls}")
        except TypeError:
            pass

    return ripe_collectors
