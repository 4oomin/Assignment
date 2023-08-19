import pandas as pd
import openpyxl

class Data:
    def __init__(self,cfg,file):
        self.cfg = cfg
        self.old_obj = None
        self.old_index= None
        self.old_match = None
        self.old_issue = None
        self.old_time = None

        self.new_obj = None
        self.new_index = None
        self.new_match = None
        self.new_issue = None
        self.new_time = None

        self.load(file)
        pass
    def load(self,file):
        path = ".\\Input\\"+file

        df_old_obj = pd.read_excel(path,sheet_name='old_obj', engine='openpyxl',index_col=None)
        df_old_match = pd.read_excel(path,sheet_name='old_match', engine='openpyxl',index_col=None)
        df_old_issue = pd.read_excel(path,sheet_name='old_issue', engine='openpyxl',index_col=None)
        df_new_obj = pd.read_excel(path, sheet_name='new_obj', engine='openpyxl',index_col=None)
        df_new_match = pd.read_excel(path, sheet_name='new_match', engine='openpyxl',index_col=None)
        df_new_issue = pd.read_excel(path, sheet_name='new_issue', engine='openpyxl',index_col=None)

        old_obj = df_old_obj.values.tolist()
        old_match = df_old_match.values.tolist()
        old_issue = df_old_issue.values.tolist()
        new_obj = df_new_obj.values.tolist()
        new_match = df_new_match.values.tolist()
        new_issue = df_new_issue.values.tolist()
        self.rerrange(old_obj,old_match,old_issue,new_obj,new_match,new_issue)
        pass

    def rerrange(self, old_obj, old_match, old_issue, new_obj, new_match, new_issue):

        self.old_obj = [[] for _ in range(len(old_obj))]
        self.old_index = [[self.cfg.mos_cnt for _ in range(self.cfg.obj_cnt)] for _ in range(len(old_obj))]
        self.old_time = []
        for t in range(len(old_obj)):
            self.old_time.append(old_obj[t][0])
            obj = ()
            for i in range(1,len(old_obj[t])):
                if pd.isna(old_obj[t][i]):
                    break
                obj += (old_obj[t][i],)
                if i % 3 == 0:
                    self.old_obj[t].append(obj)
                    self.old_index[t][int(old_obj[t][i])] = i//3 - 1
                    obj = ()
            pass

        self.old_issue = [[] for _ in range(len(old_issue))]
        for t in range(len(old_issue)):
            obj = ()
            for i in range(1,len(old_issue[t])):
                if pd.isna(old_issue[t][i]):
                    break
                obj += (old_issue[t][i],)
                if i % 3 == 0:
                    self.old_issue[t].append(obj)
                    obj = ()
            pass

        self.old_match = [[self.cfg.dft_uid for _ in range(self.cfg.obj_cnt)] for _ in range(len(old_match))]
        for t in range(len(old_match)):
            for i in range(1,len(old_match[t])):
                self.old_match[t][i-1] = old_match[t][i]
                pass
            pass

        self.new_obj = [[] for _ in range(len(new_obj))]
        self.new_index = [[self.cfg.mos_cnt for _ in range(self.cfg.obj_cnt)] for _ in range(len(new_obj))]
        self.new_time = []
        for t in range(len(new_obj)):
            self.new_time.append(new_obj[t][0])
            obj = ()
            for i in range(1, len(new_obj[t])):
                if pd.isna(new_obj[t][i]):
                    break
                obj += (new_obj[t][i],)
                if i % 3 == 0:
                    self.new_obj[t].append(obj)
                    self.new_index[t][int(new_obj[t][i])] = i // 3 - 1
                    obj = ()
            pass

        self.new_issue = [[] for _ in range(len(new_issue))]
        for t in range(len(new_issue)):
            obj = ()
            for i in range(1, len(new_issue[t])):
                if pd.isna(new_issue[t][i]):
                    break
                obj += (new_issue[t][i],)
                if i % 3 == 0:
                    self.new_issue[t].append(obj)
                    obj = ()
            pass

        self.new_match = [[self.cfg.dft_uid for _ in range(self.cfg.obj_cnt)] for _ in range(len(new_match))]
        for t in range(len(new_match)):
            for i in range(1, len(new_match[t])):
                self.new_match[t][i - 1] = new_match[t][i]
                pass
            pass

        pass

    pass