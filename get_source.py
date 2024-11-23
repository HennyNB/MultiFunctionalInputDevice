import os
import sys
import shutil
import zipfile
import requests

sys.path.append('.\\')
import config


class GetSource(object):

    def __init__(self):
        self.config = config.Config()

        self.root_path = '.\\'
        self.zip_file_path = self.root_path + 'file.zip'
        self.source_path = self.root_path + '__source__'

        self.url = 'https://codeload.github.com/HennyNB/MultiFunctionalInputDevice/zip/refs/heads/main'

        self.response = requests.get(self.url)

        self.splot = self.url.split('/')
        self.path = f'{self.source_path}\\{self.splot[4]}-{self.splot[8]}\\'

    def get_source(self):
        with open(file=self.zip_file_path, mode='wb') as file:
            file.write(self.response.content)

        with zipfile.ZipFile(self.zip_file_path, mode='r') as zip_source:
            zip_source.extractall(self.source_path)

        os.remove(self.zip_file_path)

    def file_operate(self):
        [shutil.copy(self.path + file, self.source_path) for file in os.listdir(self.path)]

        shutil.rmtree(self.path)

    def source_operator(self):
        os.system('cls')

        if self.response.status_code == 200:
            self.config.be_getting()
            self.config.editor_title()
            self.config.choices_title()

            self.get_source()
            self.file_operate()

            os.system('cls')
            self.config.have_gotten()

        else:
            self.config.download_error()
