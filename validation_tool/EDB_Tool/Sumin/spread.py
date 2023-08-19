from Sumin.process import *
class Spread:
    def __init__(self, process):
        self.time = process.time
        self.obj = process.obj
        self.index = process.index
        self.match = process.match
        self.issue = process.issue
        self.s_obj = None
        self.s_match = None
        self.s_issue = None

        self.spread_obj()
        self.spread_match()
        self.spread_issue()
        pass

    def spread_obj(self):
        self.s_obj = [[] for _ in range(len(self.time))]
        for t in range(len(self.time)):
            self.s_obj[t].append(self.time[t])
            for i in range(len(self.obj[t])):
                for j in range(len(self.obj[t][i])):
                    self.s_obj[t].append(self.obj[t][i][j])
                pass
            pass
        pass

    def spread_issue(self):
        self.s_issue = [[] for _ in range(len(self.time))]
        for t in range(len(self.time)):
            self.s_issue[t].append(self.time[t])
            for i in range(len(self.issue[t])):
                for j in range(len(self.issue[t][i])):
                    self.s_issue[t].append(self.issue[t][i][j])
                pass
            pass
        pass

    def spread_match(self):
        self.s_match = [[] for _ in range(len(self.time))]
        for t in range(len(self.time)):
            self.s_match[t].append(self.time[t])
            for i in range(len(self.match[t])):
                self.s_match[t].append(self.match[t][i])
                pass
        pass

    pass