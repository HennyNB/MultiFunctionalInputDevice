import sys
import decimal

sys.path.append('.\\')
import config


class ProgressBar(object):
    config = config.Config()

    filled_text = '='
    unfilled_text = '-'

    progress_title = '当前进度：'

    len_title = config.text_length(text=progress_title)
    len_config = 10

    decimal_places = 2
    bar_end_space_quantity = 1

    bar_length = config.split_quantity - len_title - len_config - decimal_places - bar_end_space_quantity

    @staticmethod
    def rounder(number: float or int or eval, n: int):
        num = decimal.Decimal(number)
        side = '0.' + '0' * n
        round_config = decimal.Decimal(side)
        rounded = num.quantize(round_config)

        return rounded

    def progress_bar(self, total: int, item: int):
        percents_list = []

        completed_length = int(self.bar_length * item / total)
        uncompleted_length = self.bar_length - completed_length

        percents = self.rounder(100 * item / total, self.decimal_places)
        [percents_list.append(quantity) for quantity in str(percents)]

        bar = self.filled_text * completed_length + self.unfilled_text * uncompleted_length

        def output_config(filled: str, percent_bar: str):
            out_put = (self.progress_title + '[' + filled + '] ' +
                       percent_bar + ' %' + ' ' * self.bar_end_space_quantity)

            print('\r' + out_put, end='')

        def output(percent_bar: str, flag: str):
            if flag == 'programme':
                output_config(filled=bar, percent_bar=percent_bar)

            elif flag == 'end':
                output_config(filled=self.filled_text * self.bar_length, percent_bar=percent_bar)

        def programme(percent: str):
            if item + 1 == total:
                output(percent_bar='100.' + '0' * self.decimal_places, flag='end')

            elif item + 1 < total:
                output(percent_bar=percent, flag='programme')

        percent_list = ['0' * (4 + self.decimal_places - len(percents_list))] + percents_list
        programme(percent=str(''.join(percent_list)))
