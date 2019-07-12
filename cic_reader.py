import pandas



class cic_reader:
    def __init__(self,file_path):
            self.file_path = file_path


    def read_cic_pandas(self):
        #returns pandas frame
        csv = pandas.read_csv(self.file_path, header=None)
        frame = pandas.DataFrame(csv)
        return frame



