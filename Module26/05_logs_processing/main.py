from collections.abc import Iterable
import os


def error_log_generator(file_name: str) -> Iterable[str]:
    """
    функция-генератор чтения ошибок из файла
    
    :param file_name: название файла
    :type dir: str
    :yield: line
    :rtype: str
    """

    with open(file_name, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


input_file_path = os.path.join('data', 'work_logs.txt')
output_file_path = os.path.join('data', 'output.txt')
with open(output_file_path, 'w') as output:
    if not os.path.exists(input_file_path):
        print("Файл не найден.")
    else:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
print("Файл успешно обработан.")
