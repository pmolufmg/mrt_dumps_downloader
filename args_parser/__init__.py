import sys
import argparse
import datetime


class ArgsParser:

    def __init__(self):
        self.projects = ['ripe', 'routeviews', 'isolario', 'pch']
        self.date_format = '%Y%m%d'

        self.parser = argparse.ArgumentParser()
        self.add_arguments()
        self.args = self.parser.parse_args()

        self.test_args()

        self.set_range_list()

    def add_arguments(self):
        self.parser.add_argument('--download',
                                 dest='download',
                                 action='store_true',
                                 help="download from sources")

        self.parser.add_argument('--ribs',
                                 dest='ribs',
                                 action='store_true',
                                 help="get RIB dumps")

        self.parser.add_argument('--updates',
                                 dest='updates',
                                 action='store_true',
                                 help="get UPDATE dumps")

        self.parser.add_argument('-p', '--project',
                                 dest='project',
                                 nargs='*',
                                 type=str,
                                 help="source project ('ripe, routeviews, isolario, pch)\
                                         - use -p 'project' for each one")

        self.parser.add_argument('-d', '--date',
                                 dest='date',
                                 nargs='*',
                                 type=str,
                                 help="dump dates\
                                         - use -d list of dates (yyyymmdd) or \
                                         -dr [initial date] [final date] for a date range")

        self.parser.add_argument('-dr', '--date-range',
                                 dest='date_range',
                                 nargs=2,
                                 type=str,
                                 help="date range - get dumps from all dates in range")

        self.parser.add_argument('-n', '--num-of-dumps',
                                 dest='number_of_dumps',
                                 type=int,
                                 help="number of dumps to download from each collector "
                                      "if none is given, fetch all of them")

        return

    def test_args(self):
        try:
            self.test_projects()
            self.test_dates_and_range()
            self.test_number_of_dumps()
            self.test_ribs_update_mode()

        except (ValueError, NameError):
            print('Aborting.')
            sys.exit(1)

        return

    def test_ribs_update_mode(self):
        if not (self.args.ribs or self.args.updates):
            print('definition of --ribs or --updates parameter is required')
            raise ValueError

    def test_projects(self):
        if not self.args.project:
            self.args.project = self.projects
            return

        else:
            error = ''
            self.set_names_to_lower()
            try:
                for project in self.args.project:
                    error = project
                    assert (project in self.projects)

            except AssertionError:
                print('Unknow project name: {}'.format(error))
                raise NameError

        return

    def test_dates_and_range(self):
        if not self.dates_or_range():
            print('At least one date value is required as argument.')
            raise ValueError

        if self.args.date:
            self.test_dates()
        else:
            self.args.date = []

        if self.args.date_range:
            self.test_range()

        return

    def dates_or_range(self):
        return self.args.date or self.args.date_range

    def test_dates(self, d_range=False):
        error = ''
        dates = self.args.date if not d_range else self.args.date_range

        if dates:
            try:
                for date in dates:
                    error = date
                    _ = self.get_date_object(date)
            except ValueError:
                print('Invalid date: {}'.format(error))
                raise ValueError

        return

    def test_range(self):
        if len(self.args.date_range) == 2:
            self.test_dates(d_range=True)

            try:
                initial_date = self.get_date_object(self.args.date_range[0])
                end_date = self.get_date_object(self.args.date_range[1])

                assert (initial_date <= end_date)

            except AssertionError:
                print('Initial date is greater than final date.')
                raise ValueError

        else:
            print('Range takes exactly 2 arguments (initial date and final date')
            raise ValueError

        return

    def test_number_of_dumps(self):
        if self.args.number_of_dumps \
                and self.args.number_of_dumps < 0:
            print('Number of dumps must be a positive integer.')
            raise ValueError

        return

    def get_date_object(self, date_string):
        date = datetime.datetime.strptime(date_string, self.date_format)
        return date

    def set_range_list(self):
        if not self.args.date_range:
            return

        initial_date = self.args.date_range[0]
        final_date = self.args.date_range[1]

        start = self.get_date_object(initial_date)
        end = self.get_date_object(final_date)
        step = datetime.timedelta(days=1)

        while start <= end:
            self.args.date.append(start.strftime('%Y%m%d'))
            start += step

        self.args.date = sorted(list(set(self.args.date)))

        return

    def set_names_to_lower(self):
        lower = []

        for project in self.args.project:
            lower.append(project.lower())

        self.args.project = lower

    def get_args(self):
        return self.args.download, \
               self.args.ribs, \
               self.args.updates, \
               self.args.project, \
               self.args.date, \
               self.args.number_of_dumps
