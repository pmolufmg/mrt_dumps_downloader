#!/usr/bin/env python3
from args_parser import ArgsParser
from mrt_urls import MrtUrlDict
from download_dumps import DownloadDumps

if __name__ == "__main__":
    args = ArgsParser().get_args()
    get_files = args[0]

    links = MrtUrlDict(args).get_urls()

    if get_files:
        downloader = DownloadDumps(links)
        downloader.download_files()

    else:
        links.print_urls()
