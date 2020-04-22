from urllib.request import urlopen as get_file
import urllib.error
import subprocess
from datetime import datetime as dt
import sys
import os
import time
from config import *


class DownloadDumps:

    def __init__(self, links_dict):
        self.links = links_dict
        self.log_file = open(log_file, 'a+')

    def download_files(self):
        try:
            for project in self.links:
                print('{}: started {}'.format(dt.now(), project))
                if not self.links[project]:
                    continue

                project_path = self.get_project_path(project)

                for url in self.links[project]:
                    file = self.get_file_path(project, project_path, url)
                    if os.path.isfile(file):
                        continue

                    try:
                        args = ['wget', '-O', file, url]
                        proc = subprocess.run(args)
                        self.log_event(url)

                    except subprocess.SubprocessError:
                        self.log_event(url, error=True)
                        continue

        except KeyboardInterrupt:
            print('\nAborting...')
            sys.exit()

    def get_file_path(self, project, project_path, url):
        base_dir = self.get_type_path(project_path, url)

        if project == 'ripe':
            return self.get_full_path(base_dir, url, 3)

        elif project == 'routeviews':
            return self.get_full_path(base_dir, url, 3)

        elif project == 'isolario':
            return self.get_full_path(base_dir, url, 4)

        elif project == 'pch':
            if self.get_dump_type(url) == 'updates':
                return self.get_full_path(base_dir, url, 5)

            else:
                return self.get_full_path(base_dir, url, 8)

        else:
            raise NameError

    def get_full_path(self, base_dir, url, collector_index):
        fields = url.split('/')
        collector = fields[collector_index]
        file = fields[-1]

        return self.get_collector_file_path(base_dir, collector, file)

    @staticmethod
    def get_collector_file_path(base_dir, collector, filename):
        col_dir = create_and_set_folder(base_dir, collector)

        return file_path(col_dir, filename)

    @staticmethod
    def get_project_path(project):
        return create_and_set_folder(dumps_dir, project)

    def get_type_path(self, project_path, url):
        dump_type = self.get_dump_type(url)
        dump_type_dir = create_and_set_folder(project_path, dump_type)

        return dump_type_dir

    @staticmethod
    def get_dump_type(link):
        if 'updates' in link:
            return 'updates'
        else:
            return 'ribs'

    def log_event(self, file, error=False):
        text = 'ERROR: ' if error else ''
        text += dt.now().strftime('%Y-%m-%d %H:%M:%S') + '-'
        text += file + '\n'
        self.log_file.write(text)
