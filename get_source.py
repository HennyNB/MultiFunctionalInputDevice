import os
import sys
import shutil
import zipfile
import requests

sys.path.append('.\\')
import config


class GetSource(object):
    config = config.Config()

    url = 'https://codeload.github.com/HennyNB/MultiFunctionalInputDevice/zip/refs/heads/main'
    response = requests.get(url)

    splot = url.split('/')
    path = config.source_path + '\\' + splot[4] + '-' + splot[8] + '\\'

    def get_source(self):
        with open(file=self.config.zip_file_path, mode='wb') as file:
            file.write(self.response.content)

        with zipfile.ZipFile(self.config.zip_file_path, mode='r') as zip_source:
            zip_source.extractall(self.config.source_path)

        os.remove(self.config.zip_file_path)

    def file_operate(self):
        [shutil.copy(self.path + file, self.config.source_path) for file in os.listdir(self.path)]
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
