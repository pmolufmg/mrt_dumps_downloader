from bs4 import BeautifulSoup, SoupStrainer
import requests
import re


def get_rv_collectors():
    url = "http://archive.routeviews.org"

    rv_collectors = []
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')

    collector_re = r"^\/route-views"
    collector_re_c = re.compile(collector_re)


    for link in soup.find_all('a'):
        try:
            if collector_re_c.search(link.get('href')):
                rv_collector_urls = link.get('href').split('/')[1:]
                rv_collectors.append(f"{rv_collector_urls[0]}/bgpdata")
        except TypeError:
            pass

    return rv_collectors
