from Sumin.process import *
class Align():
    def __init__(self, process):
        self.time = process.time
        self.obj = process.obj
        self.index = process.index
        self.match = process.match
        self.issue = process.issue
        self.a_time = None
        self.a_obj = None
        self.a_match = None
        self.a_issue = None

        self.align_time()
        self.align_obj()
        self.align_match()
        self.align_issue()
        pass
    def align_time(self):
        self.a_time = []
        for t in range(len(self.time)):
            self.a_time.append((t, self.time[t]))
            pass
        pass
    def align_obj(self):
        self.a_obj = []
        for t in range(len(self.time)):
            for i in range(len(self.obj[t])):
                self.a_obj.append((t,)+self.obj[t][i])
                pass
            pass
        pass
    def align_match(self):
        self.a_match = []
        for t in range(len(self.time)):
            for i in range(len(self.match[t])):
                self.a_match.append((t, i, self.match[t][i]))
                pass
        pass
    def align_issue(self):
        self.a_issue = []
        for t in range(len(self.time)):
            for i in range(len(self.issue[t])):
                self.a_issue.append((t,)+self.issue[t][i])
        pass
    pass