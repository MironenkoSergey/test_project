from os import listdir, path, chdir


def find_file(file_name):
    if path.isfile(file_name):
        return path.basename(file_name)
    for dir in listdir():
        if path.isdir(dir):
            chdir(dir)
            current_path = find_file(file_name)
            chdir('..')
            if current_path is not None:
                return current_path


if __name__ == '__main__':
    fname = 'recurs.py'
    chdir('..')
    print(find_file(fname))
