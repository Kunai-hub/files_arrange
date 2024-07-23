# -*- coding: utf-8 -*-

import os, time, shutil


class FileSorter:
    """
    Программа для сортировки файлов из каталога источника(src) в каталог назначения(dst).
    Сортировка происходит по дате модификации файла в виде "/dst/year/month"
    Сортировка происходит с учетом подкаталогов.
    """

    def __init__(self, src, dst):
        """
        :param src: каталог-источник
        :param dst: каталог-назначения
        """
        if src:
            self.src = os.path.normpath(src)
        else:
            print('Не указан каталог источник.')
        if dst:
            self.dst = os.path.normpath(dst)
        else:
            print('Не указан каталог назначения.')

    def get_dirs(self, mod_time=None):
        """
        Получение имени директории.

        :param mod_time: время последней модификации файла
        :return: имя директории
        """
        file_mdate = time.gmtime(mod_time)
        year, mon = str(file_mdate.tm_year), str(file_mdate.tm_mon)
        file_dest = os.path.join(self.dst, *(year, mon if len(mon) != 1 else '0' + mon))
        return file_dest

    def make_dirs(self, dir=None):
        """
        Проверка наличия директории.

        :param dir: название директории
        :return: None
        """
        if not os.path.exists(dir):
            os.makedirs(dir)

    def copy_file(self, src=None, dst=None):
        """
        Копирование исходного файла.

        :param src: директория исходного файла
        :param dst: директория конечного файла
        :return: None
        """
        if not os.path.exists(dst):
            shutil.copy2(src=src, dst=dst)

    def arrange(self):
        """
        Запуск сортировки.

        :return: None
        """
        for dir_path, dir_names, file_names in os.walk(self.src):
            for file in file_names:
                file_mod_time = os.path.getmtime(os.path.join(dir_path, file))
                file_dst = self.get_dirs(file_mod_time)
                self.make_dirs(file_dst)

                file_dst = os.path.join(file_dst, file)
                file_src = os.path.join(dir_path, file)
                self.copy_file(src=file_src, dst=file_dst)

        if os.path.exists(self.dst):
            print('Сортировка завершена успешно.', self.dst)
        else:
            print('Ошибка! Проверьте пути к каталогам.', self.src, self.dst)


if __name__ == '__main__':
    src_dir = r''
    dst_dir = r''
    files = FileSorter(src=src_dir, dst=dst_dir)
    files.arrange()
