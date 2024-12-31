class GetModules(object):

    @staticmethod
    def get_modules():
        modules_list = ['PyAutoGUI', 'PyGetWindow', 'pynput', 'requests', 'pypiwin32', 'keyboard']
        modules = [module for module in set(modules_list)]

        modules.sort()
        return modules
