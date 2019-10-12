from urls_src.links import Links


class RipeLinks(Links):

    def __init__(self, args):
        params = {}
        params['domain'] = "http://data.ris.ripe.net"
        params['collectors'] = ['rrc00',
                                'rrc01',
                                'rrc03',
                                'rrc04',
                                'rrc05',
                                'rrc06',
                                'rrc07',
                                'rrc10',
                                'rrc11',
                                'rrc12',
                                'rrc13',
                                'rrc14',
                                'rrc15',
                                'rrc16',
                                'rrc18',
                                'rrc19',
                                'rrc20',
                                'rrc21',
                                'rrc22',
                                'rrc23']

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
