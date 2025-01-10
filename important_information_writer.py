import sys

sys.path.append('.\\')
import config
import manager


class ImportantInformationWriter(object):
    config = config.Config()
    manager = manager.Manager()

    modules_list = ['PyAutoGUI', 'pyperclip', 'pynput', 'pypi' + 'win32', 'PyGetWindow']

    project_list = ['项目名称：多功能输入装置',
                    '创建作者：༺ཌༀ Henny✵發龘 ༀད༻',
                    '创建时间：2023-9-21 13:25:34',
                    '联系方式：2669753313@qq.com',
                    '版本信息：Python-3.12.8',
                    '技术支持：PyCharm']

    author_total = config.next.join(project_list) + config.next
    modules_total = config.next.join(modules_list) + config.next

    used_programme = manager.space + 'Used programme '
    used_programme_total = used_programme + config.now() + config.next + config.next

    total = [[config.information_path, author_total], [config.requirements_path, modules_total]]

    def writer(self):
        for item in self.total:
            with open(file=item[0], mode='r', encoding='UTF-8') as file:
                content = file.read()

            if not content == item[1]:
                with open(file=item[0], mode='w', encoding='UTF-8') as file:
                    file.write(item[1])

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write(self.used_programme_total)
