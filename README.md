# mrt_dumps_downloader

Downloads MRT dumps from: 

Ripe (https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris/ris-raw-data), 

Routeviews (http://archive.routeviews.org/), 

Isolario (https://www.isolario.it/Isolario_MRT_data/) and 

PCH (https://www.pch.net/resources/).

Requirements:
 - Linux
 - Python 3.6+
 - 'Progress' module (pip install progress)
 
 Usage
 
 Command line args:
 
 -p list of projects to fetch dump files (optional). If none, it will fetch from all projects (Ripe, RouteViews, Isolario and PCH)
 
 -d list of dates to get dumps from (format: yyyymmdd)
 
 -dr date range. It accepts 2 dates and will return dumps from this range. (At least one must be used: -d or -dr)
 
 -n number of dumps to get from each collector (optional). If none, it will return all dumps from a given date.
 
 --ribs get only rib dumps.
 
 --updates get only update dumps. (At least one must be used: --ribs or --updates)
 
 --download download files into a certain folder hierarchy (/dumps/project/rib or update/collector/dump_file). You can change this in the config.py file.
 
 If --download is not used, it will just print the list of urls it would use to download dump files.
 
 Example:
 python get_mrt_dumps.py -p ripe routeviews -d 20170101 20180101 -dr 20190101 20190103 -n 2 --updates --ribs --download
 
 Would download 4 dump files (2 ribs and 2 updates) from each one of ripe's and routeview's collectors, with dates 2017/01/01, 2018/01/01, 2019/01/01, 2019/01/02 and 2019/01/03.
 
 The folder structure can be changed in config.py.
