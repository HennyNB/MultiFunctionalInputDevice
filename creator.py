import os
import sys

sys.path.append('.\\')
import config


class Creator(object):
    config = config.Config()

    def path_creator(self):
        [os.mkdir(i) for i in self.config.path_list if not os.path.exists(i)]

    def file_creator(self):
        for file in self.config.file_list:
            if not os.path.exists(file):
                with open(file=file, mode='w', encoding='UTF-8') as each_file:
                    each_file.write('')

    @staticmethod
    def file_filler_config(file, content: str):
        with open(file=file, mode='r', encoding='UTF-8') as each_file:
            old = each_file.read()

        if old == '' or old.isspace():
            with open(file=file, mode='w', encoding='UTF-8') as each_file:
                each_file.write(content)

    def file_filler(self):
        data_list = [[self.config.interval_path, '0.01'], [self.config.times_path, '0']]
        [self.file_filler_config(file=item[0], content=item[1]) for item in data_list]

    def total_creator(self):
        self.path_creator()
        self.file_creator()
        self.file_filler()
