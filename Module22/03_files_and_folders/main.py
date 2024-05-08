import os


def get_folder_info(path):
    size = 0
    folder_count = 0
    files_count = 0
    for i_path, folders, files in os.walk(path):
        for file in files:
            file_place = os.path.join(i_path, file)
            size += os.path.getsize(file_place)
        folder_count += len(folders)
        files_count += len(files)
    size = round(size / 1024, 2)
    return size, folder_count, files_count


path = os.path.abspath(os.path.join('../../../', input('')))
print(path)
size_files, folder_count, files_count = get_folder_info(path)
print('Размер каталога (в Кб): {}'.format(size_files))
print('Количество подкаталогов: {}'.format(folder_count))
print('Количество файлов: {}'.format(files_count))
