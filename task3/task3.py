import sys
import json
import shutil

src_values = sys.argv[1]
src_tests = sys.argv[2]
out_report = sys.argv[3]

# Скопировать файл tests.json

shutil.copy(src_tests, out_report)

# Получить содержимое файлов

load_values = json.loads(open(src_values).read())
load_report = json.loads(open(out_report).read())

# Извлечь dict, содержащий только успешные тесты

filtered_dict = [obj for obj in load_values['values'] if obj['value'] == 'passed']

ids = [key for key in filtered_dict.keys()]
print(ids)

print(passed_objects)

# Преобразовать полученные объекты в json строку

json_string = json.dumps(passed_objects, indent=2)

# Записать строку
with open(out_report, 'w') as outfile:
    outfile.write(json_string)

"""
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return o

json_str = json.dumps({1, 2, 3}, cls=MyEncoder)
print(json_str)

open(src_values, 'r') as file

data = {'name': 'Eric', 'age': 38 }
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

title = alert_json['rule']['description'] if 'description' in alert_json['rule'] else ''
description = alert_json['full_log'] if 'full_log' in alert_json else ''
# print(title, description)
# group_suricata = ['suricata']
# if any(group in groups for group in BLACK_GROUPS):
# suricata_alert_json =
# alert_json.replace("\\n", "\n")
full_log_json = json.loads(alert_json['full_log'])

src_ip = full_log_json['src_ip']
print('\n-----\n', src_ip)
# print(src_ip)
"""