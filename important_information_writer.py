import sys

sys.path.append('.\\')
import config
import manager
import get_imports


class ImportantInformationWriter(object):
    config = config.Config()
    manager = manager.Manager()
    get_imports = get_imports.GetImports()

    project_name = '项目名称：多功能输入装置' + config.next
    creation_editor = '创建作者：༺ཌༀ Henny✵發龘 ༀད༻' + config.next
    creation_time = '创建时间：2023-9-21 13:25:34' + config.next
    contact_information = '联系方式：2669753313@qq.com' + config.next
    technical_support = '技术支持：PyCharm' + config.next

    used_programme = manager.space + 'Used programme '

    editor_total = str(project_name + creation_editor + creation_time +
                       contact_information + technical_support)

    modules_total = config.next.join(get_imports.get_imports(path='.\\')) + config.next

    used_programme_total = str(used_programme + config.now() + config.next + config.next)

    total = [[config.information_path, editor_total],
             [config.requirements_path, modules_total]]

    def writer(self):
        for item in self.total:
            with open(file=item[0], mode='r', encoding='UTF-8') as file:
                old = file.read()

            if not old == item[1]:
                with open(file=item[0], mode='w', encoding='UTF-8') as file:
                    file.write(item[1])

        with open(file=self.config.logs_path, mode='a', encoding='UTF-8') as file:
            file.write(self.used_programme_total)
