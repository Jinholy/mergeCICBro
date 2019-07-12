import sys
import logging
import pandas
import cic_reader as cr
import bro_reader as br

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





rc = cr.cic_reader("/home/hott/honeypot/mergeCICBro/cic/2015-03-19_winnormal.pcap_Flow.csv")

frame = rc.read_cic_pandas()
print(frame[6]) #6: Time Stamp

br = br.bro_reader("/home/hott/honeypot/mergeCICBro/bro/conn.log")
br.bro_file_init