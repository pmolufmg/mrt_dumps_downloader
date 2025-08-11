from urls_src.links import Links
from .get_all_collectors_ripe import get_ripe_collectors

class RipeLinks(Links):

    def __init__(self, args):
        params = {}
        params['domain'] = "https://data.ris.ripe.net"
        params['collectors'] = get_ripe_collectors()
        params['rib_prefix'] = 'bview'
        params['update_prefix'] = 'updates'

        params['rib_instances'] = ['0000',
                                   '0800',
                                   '1600']

        params['update_instances'] = [str(x).zfill(4)
                                      for x in range(0, 2360, 5)
                                      if x % 100 < 60]

        params['file_extension'] = 'gz'
        params['filename_format'] = 'f"{date}.{instance}.{file_extension}"'

        params['ipv4_path'] = None
        params['ipv6_path'] = None
        params['ribs_path'] = None
        params['updates_path'] = None

        params['url_format'] = 'f"{domain}/{collector}/{year}.{month}/{prefix}.{filename}"'

        Links.__init__(self,
                       args,
                       params)
