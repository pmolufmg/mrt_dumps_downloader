import os


def create_and_set_folder(main, subdir):
    path = subdir + '/'
    sub = '/' + path
    os.makedirs(main + sub, exist_ok=True)
    dir_path = os.path.join(main, path)
    return dir_path


def file_path(folder, filename):
    return os.path.join(folder, filename)


main_dir = os.path.abspath(os.path.dirname(__file__))

dumps_dir = create_and_set_folder(main_dir, 'dumps')

log_dir = create_and_set_folder(main_dir, 'logs')
log_file = os.path.join(log_dir, 'log.log')
