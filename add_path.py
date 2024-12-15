import os
import sys


class AddPath(object):

    @staticmethod
    def get_path():
        exe_path = sys.executable
        splot = exe_path.split('\\')
        splot.remove(splot[-1])

        python_path = '\\'.join(splot)

        if splot[-1] == 'Scripts':
            scripts_path = python_path

        else:
            scripts_path = python_path + '\\Scripts\\'

        return [python_path, scripts_path]

    def add_path(self):
        python_path = self.get_path()[0]
        scripts_path = self.get_path()[1]

        environment = os.environ['path']

        if python_path == scripts_path:
            environment += os.pathsep + python_path

        else:
            environment += os.pathsep + python_path
            environment += os.pathsep + scripts_path
