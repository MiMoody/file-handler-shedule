import os


class FileReader:
    """ Класс работает с файлами """
    
    @staticmethod
    def last_line(path_file:str) -> str:
        """ Читает последнюю строку файла """
        
        with open(path_file, 'rb') as f:
            try:  
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_line = f.readline().decode()
        return last_line