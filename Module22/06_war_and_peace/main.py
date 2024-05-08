import collections
import zipfile


def get_text(archive_name):
    text = ''
    with zipfile.ZipFile(archive_name, "r") as archive:
        for i_file_name in archive.namelist():
            if i_file_name:
                with archive.open(i_file_name, "r") as file:
                    text = file.read().decode('utf8')
    return text


def collect_stats(text):
    result = {}
    for letter in text:
        if letter.isalpha():
            result[letter] = result.get(letter, 0) + 1
    return result


def sort_by_frequency(stats):
    sorted_value = sorted(stats.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for value in sorted_value:
        for key in stats.keys():
            if stats[key] == value:
                sorted_dict[key] = stats[key]
    return sorted_dict


def print_stats(stats):
    for letter, count in stats.items():
        print('{} : {}'.format(letter, count))


archive_name = 'voyna-i-mir.zip'
text = get_text(archive_name)
stats = collect_stats(text)
stats = sort_by_frequency(stats)
print_stats(stats)
