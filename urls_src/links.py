
class Links:

    def __init__(self,
                 args,
                 params):
        try:
            self.download = args[0]
            self.ribs = args[1]
            self.updates = args[2]
            self.project = args[3]
            self.dates = args[4]
            self.number_of_dump_files = args[5]
            self.domain = params['domain']
            self.collectors = params['collectors']
            self.file_extension = params['file_extension']
            self.filename_format = params['filename_format']
            self.rib_prefix = ''
            self.update_prefix = ''
            self.url_format = params['url_format']

            self.rib_instances = self.set_dumps_list(params['rib_instances'])
            self.update_instances = self.set_dumps_list(params['update_instances'])

            self.url_list = []

            self.set_prefix(params)

        except IndexError:
            print('Missing argument for link class')

    def set_dumps_list(self, dump_instances):
        dumps = self.number_of_dump_files

        if not dump_instances:
            raise IndexError

        elif dumps \
                and dumps < len(dump_instances):
            return dump_instances[:dumps]

        else:
            return dump_instances

    def set_links(self):
        if self.ribs:
            self.make_links(self.rib_instances, self.rib_prefix)

        if self.updates:
            self.make_links(self.update_instances, self.update_prefix)

    def make_links(self, instances, type_prefix):
        domain = self.domain
        url_format = self.url_format
        file_extension = self.file_extension
        filename_format = self.filename_format
        prefix = type_prefix

        for collector in self.collectors:

            for date in self.dates:
                year = date[:4]
                month = date[4:6]
                day = date[6:]

                for instance in instances:

                    if isinstance(prefix, str):
                        filename = eval(filename_format)
                        url = eval(url_format)
                        self.url_list.append(url)

                    elif isinstance(prefix, list):
                        for form in prefix:
                            url = eval(form)
                            self.url_list.append(url)

                    else:
                        raise IndexError
        return

    def get_url_list(self):
        return self.url_list

    def set_prefix(self, params):
        rib_prefix = params['rib_prefix']
        update_prefix = params['update_prefix']
        ribs_path = params['ribs_path']
        updates_path = params['updates_path']

        if not (rib_prefix and update_prefix):
            self.rib_prefix = ribs_path
            self.update_prefix = updates_path
        else:
            self.rib_prefix = rib_prefix
            self.update_prefix = update_prefix

    def print_url_list(self):
        urls = '\n'.join(self.url_list)
        print(urls)
