import json
from typing import Dict, List


def dict_diff(dict_1: Dict, dict_2: Dict, diff: List) -> Dict:
    """
    Функция поиска изменения в JSON файлах
    """

    for key, value in dict_1.items():
        if key in diff and dict_1[key] != dict_2[key]:
            result[key] = dict_2[key]
        if isinstance(value, dict):
            dict_diff(dict_1[key], dict_2[key], diff)
        if isinstance(value, list):
            for index, val in enumerate(value):
                if isinstance(val, dict):
                    dict_diff(dict_1[key][index], dict_2[key][index], diff)
    return result


result = {} 
diff_list = ["cost_per_unit", "staff", "datetime"]
with open('json_old.json', 'r', encoding='utf-8') as f: 
    old_data = json.load(f) 
with open('json_new.json', 'r', encoding='utf-8') as f: 
    new_data = json.load(f) 
result = dict_diff(old_data, new_data, diff_list)
print(result) 
with open('result.json', 'w') as file: 
    json.dump(result, file, indent=4)
