import pandas
import logging

class Bro:
    def __init__(self, file_path):
        self.file_path = file_path
        self.result = file_path + "bro"
        self.sep = ""
        self.empty_filed = ""
        self.unset_field = ""
        self.path = ""      #log type
        self.open = ""
        self.fields = []
        self.types = []
        self.bro_file_init(file_path)
        self.logs = []

    def get_bro_log(self):
        log = open(self.file_path, 'r')
        lines = log.readlines()
        self.logs = lines[8:]
        log.close()
        return self.logs

    def bro_file_init(self, file_path):
        try:
            log = open(file_path, 'r')
            lines = log.readlines()
            attr = lines[0:8]
            #self.sep = attr[0].split(' ')[1]
            self.sep = '\t'
            self.empty_filed = attr[2].split(self.sep)[1]
            self.unset_field = attr[3].split(self.sep)[1]
            self.path = attr[4].split(self.sep)[1]
            self.open = attr[5].split(self.sep)[1]
            self.fields = attr[6].split(self.sep)[1:]
            self.fields[-1] = self.fields[-1].split('\n')[0]
            self.types = attr[7].split(self.sep)[1:]
            self.types[-1] = self.types[-1].split('\n')[0]
            log.close()
        except Exception as e:
            logging.error(e)

