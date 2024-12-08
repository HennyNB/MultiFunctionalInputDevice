import os
import ast


class GetImports(object):

    @staticmethod
    def get_imports(path: str):
        path_list = os.listdir(path)

        imports = set()
        for each_file in path_list:
            if '.py' in each_file:
                with open(file=each_file, mode='r', encoding='UTF-8') as file:
                    tree = ast.parse(file.read(), filename=each_file)

                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            requirements = alias.name.split('.')
                            imports.add(requirements[0])

        filename = []
        for file in path_list:
            filename.append(file.split('.')[0])

        file_list = []
        for requirement in imports:
            if requirement not in filename:
                file_list.append(requirement)

        file_list.sort()
        return file_list
