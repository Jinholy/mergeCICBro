import sys
import logging
import pandas
import 

class Merger:
    def __init__(self):
        self.path_list = sys.argv[1:]
        
        if len(sys.argv) != 4:
            logging.info("usage: python merge.py cic_filename bro_file_path save_path")
            exit()

        try:
            f = open()
        except:
            logging.info("cannot open file{}".format(path_list[1]))

    def merge(self):
        print("merge")


merger = Merger()

merger.merge()