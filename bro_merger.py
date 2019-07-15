import pandas
import logging
import bro_reader as br
import glob



class bro_merger:
    def __init__(self, file_path):
        f_list = ['conn.log', 'dhcp.log', 'dns.log', 'http.log']
        self.log_list = [file_path+"/" + lst for lst in f_list]

        #self.log_list = glob.glob(file_path+"/*.log")
        self.df_list = []
        self.bro_log = pandas.DataFrame()

        self.set_df_list()
        self.get_bro_logs()



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
            self.df_list.append(self.read_logs(log))

    def get_bro_logs(self):
        #get bro_logs with feature list what user wants
         
        pd = pandas.merge(self.df_list[0], self.df_list[1], how='outer')
        pd.to_csv("bro.csv", mode='w')
        '''
        for df in self.df_list:
            self.bro_log.merge(df,on='uid')
            #print(df)
        '''

bm = bro_merger('/home/jinho/MergeCICBro/mergeCICBro/bro')