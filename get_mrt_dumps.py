from args_parser import ArgsParser
from urls_src.mrt_urls import MrtUrlDict
from download_dumps import DownloadDumps

if __name__ == "__main__":
    args = ArgsParser().get_args()
    get_files = args[0]

    links = MrtUrlDict(args)
    links_dict = links.get_urls()

    if get_files:
        downloader = DownloadDumps(links_dict)
        downloader.download_files()

    else:
        links.print_urls()
