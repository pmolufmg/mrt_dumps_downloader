from urls_src.links import Links

class RouteViewsLinks(Links):

    def __init__(self, args):
        params = {}
        params['domain'] = "http://archive.routeviews.org"
        params['collectors'] = ['bgpdata',
                                'route-views3/bgpdata',
                                'route-views4/bgpdata',
                                'route-views6/bgpdata',
                                'route-views.chicago/bgpdata',
                                'route-views.chile/bgpdata',
                                'route-views.eqix/bgpdata',
                                'route-views.flix/bgpdata',
                                'route-views.isc/bgpdata',
                                'route-views.kixp/bgpdata',
                                'route-views.jinx/bgpdata',
                                'route-views.linx/bgpdata',
                                'route-views.napafrica/bgpdata',
                                'route-views.nwax/bgpdata',
                                'route-views.wide/bgpdata',
                                'route-views.sydney/bgpdata',
                                'route-views.saopaulo/bgpdata',
                                'route-views2.saopaulo/bgpdata',
                                'route-views.sg/bgpdata',
                                'route-views.perth/bgpdata',
                                'route-views.sfmix/bgpdata',
                                'route-views.soxrs/bgpdata']

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
