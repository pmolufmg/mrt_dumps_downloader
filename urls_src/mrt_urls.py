from urls_src.routeviews_links import RouteViewsLinks
from urls_src.ripe_links import RipeLinks


class MrtUrlDict:
    def __init__(self, args):
        self.args = args
        self.urls_dict = self.fetch_links()

    def fetch_links(self):
        links = {'ripe': [], 'routeviews': []}
        projects = self.args[3]

        if 'ripe' in projects:
            ripe = RipeLinks(self.args)
            ripe.set_links()
            links['ripe'] = ripe.get_url_list()

        if 'routeviews' in projects:
            routeviews = RouteViewsLinks(self.args)
            routeviews.set_links()
            links['routeviews'] = routeviews.get_url_list()

        return links

    def get_urls(self):
        return self.urls_dict

    def print_urls(self):
        for project in self.urls_dict:
            for link in self.urls_dict[project]:
                print(link)

