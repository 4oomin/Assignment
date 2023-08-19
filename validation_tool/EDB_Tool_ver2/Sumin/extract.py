from Sumin.config import *
import pandas as pd

class Extract:
    def __init__(self, ver: str, cfg: Config, data):
        self.ver = ver
        self.cfg = cfg
        self.data = data
        self.obj = None
        self.time = None
        self.index = None
        self.extract()
        self.make_index()
        pass
    def extract(self):
        self.obj = [[] for _ in range(len(self.data))]
        self.time = []
        if self.ver == "old":
            for t in range(len(self.data)):
                obj = ()
                for col in self.data.columns:
                    clss = col.split(".")[0]
                    lbl = col.split(".")[-1]
                    if clss == self.cfg.old_signal:
                        if lbl in list(self.cfg.obj_dict.keys()):
                            obj += (self.data.loc[t, col],)
                            if len(obj) == len(self.cfg.obj_dict):
                                if obj[-1] != self.cfg.dft_uid:
                                    self.obj[t].append(obj)
                                obj = ()
                                pass
                            pass
                        pass
                    if clss == "MTS" and lbl == "TimeStamp":
                        self.time.append(self.data.loc[t, col])
                    pass
                pass
            pass
        elif self.ver == "new":
            for t in range(len(self.data)):
                obj = ()
                for col in self.data.columns:
                    clss = col.split(".")[0]
                    lbl = col.split(".")[-1]
                    if clss == self.cfg.new_signal:
                        if lbl in list(self.cfg.obj_dict.keys()):
                            obj += (self.data.loc[t, col],)
                            if len(obj) == len(self.cfg.obj_dict):
                                if obj[-1] != self.cfg.dft_uid:
                                    self.obj[t].append(obj)
                                obj = ()
                                pass
                            pass
                        pass
                    if clss == "MTS" and lbl == "TimeStamp":
                        self.time.append(self.data.loc[t, col])
                        pass
                    pass
                pass
            pass
        pass

    def make_index(self):
        self.index = [[self.cfg.mos_cnt for _ in range(self.cfg.obj_cnt)] for _ in range(len(self.time))]
        # self.index[t][i]=mos_cnt : time t에서 uid=i 없음
        for t in range(len(self.time)):
            for i in range(len(self.obj[t])):
                uid = self.obj[t][i][-1]
                self.index[t][uid] = i
                pass
            pass
        pass
    pass