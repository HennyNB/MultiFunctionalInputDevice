import os
import pathlib


class GetModules(object):

    @staticmethod
    def get_modules(path: str = '.\\'):
        file = 'importer.py'

        file_list = []
        modules_list = []
        module_lists = []
        imports_list = []

        key = 'i' + 'm' + 'p' + 'o' + 'r' + 't' + ' '

        path_list = os.listdir(path)

        for each_file in path_list:
            if not each_file == file:
                if pathlib.Path(each_file).is_file():
                    filename = each_file.split('.')[0]
                    file_list.append(filename)

                    with open(file=each_file, mode='r', encoding='UTF-8') as file:
                        content_lines = file.readlines()

                    for content in content_lines:
                        if key in content:
                            imports_config = content.split(key)[1]
                            imports = imports_config.split('\n')[0]

                            imports_list.append(imports)

        for module in set(imports_list):
            if module not in file_list:
                if '.' in module:
                    classes = module.split('.')[0]
                    module_lists.append(classes)

                else:
                    module_lists.append(module)

        [modules_list.append(module) for module in set(module_lists)]
        modules_list.sort()
        return modules_list
