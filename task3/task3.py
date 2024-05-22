import sys
import json

path_values = sys.argv[1]
path_tests = sys.argv[2]
path_report = sys.argv[3]

# Загрузить файлы в память

with open(path_values, 'r') as file:
    src_values = json.load(file)

with open(path_tests, 'r') as file:
    src_tests = json.load(file)

# Получить список успешно выполненных тестов

ids_passed = [obj['id'] for obj in src_values['values'] if obj['value'] == 'passed']

# Модифицировать файлы

for test in src_tests['tests']:
    if test['id'] in ids_passed:
        test['value'] = 'passed'

# Записать итоговый фалй на диск

with open(path_report, 'w') as file:
    json.dump(src_tests, file, indent=4)

