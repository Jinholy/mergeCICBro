import pandas
import logging
import bro_reader as br
import glob
import os.path


class bro_merger:
    def __init__(self, file_path):
        f_list = ['conn.log', 'dhcp.log', 'dns.log', 'http.log']
        self.log_list = [file_path+"/" + lst for lst in f_list]

        #self.log_list = glob.glob(file_path+"/*.log")
        self.df_list = []
        self.bro_logs = pandas.DataFrame()
        
        self.set_df_list()
        self.set_bro_logs()



    def read_logs(self,file_path):
        try:
            log = open(file_path, 'r')
            lines = log.readlines()
            attr = lines[6]
            col = attr.split('\t')[1:]
            col[-1] = col[-1].split('\n')[0]
            log.close()
            df = pandas.read_csv(file_path, sep='\t', skiprows=7)
            df = df.drop(df.columns[len(col)],axis=1) #set df columns
            df.columns = col
            df = df.drop(df.index[len(df)-1])
            return df
        except Exception as e:
            logging.error(e)
            
    def set_df_list(self):
        for log in self.log_list:
            if os.path.isfile(log):
                self.df_list.append(self.read_logs(log))

    def set_bro_logs(self):
        for i in range(1,len(self.df_list)):
            self.bro_logs = pandas.merge(self.df_list[i-1], self.df_list[i], how='outer')
      
    def get_bro_logs(self, f_list):
        df = self.bro_logs[f_list]
        return df

    def save_as_csv(self, data_frame, file_name):
        data_frame.to_csv(file_name+".csv", mode='w')




bm = bro_merger('/home/hott/honeypot/mergeCICBro/bro')

feature_list = ['uid', 'ts', 'Z', 'answers']


df = bm.get_bro_logs(feature_list)
print(df)
bm.save_as_csv(df, 'answers')