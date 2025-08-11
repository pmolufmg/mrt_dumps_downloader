from urls_src.links import Links
from .get_all_collectors_rv import get_rv_collectors

class RouteViewsLinks(Links):

    def __init__(self, args):
        params = {}
        params['domain'] = "http://archive.routeviews.org"
        params['collectors'] = get_rv_collectors()
        params['rib_prefix'] = 'RIBS/rib'
        params['update_prefix'] = 'UPDATES/updates'

        params['rib_instances'] = [str(t).zfill(4)
                                   for t in range(0, 2400, 200)]

        params['update_instances'] = [str(x).zfill(4)
                                      for x in range(0, 2360, 15)
                                      if x % 100 < 60]

        params['file_extension'] = 'bz2'
        params['filename_format'] = 'f"{date}.{instance}.{file_extension}"'

        params['ipv4_path'] = None
        params['ipv6_path'] = None
        params['ribs_path'] = None
        params['updates_path'] = None

        params['url_format'] = 'f"{domain}/{collector}/{year}.{month}/{prefix}.{filename}"'

        Links.__init__(self,
                       args,
                       params)
