from Sumin.extract import *
import math
class Process:
    def __init__(self, extract):
        self.match = None
        self.issue = None
        self.time = extract.time
        self.obj = extract.obj
        self.index = extract.index
        pass

    def make_match(self, other, cfg: Config):
        self.match = [[cfg.dft_uid for _ in range(cfg.obj_cnt)] for _ in range(len(self.time))]
        for t in range(len(self.time)):
            for i in range(len(self.obj[t])):
                obj_uid = self.obj[t][i][-1]
                obj_dist_x = self.obj[t][i][0]
                obj_dist_y = self.obj[t][i][1]

                min_dist = max(cfg.r_gate_x, cfg.r_gate_y) * 2 + 1
                min_uid = cfg.dft_uid + 0.1
                for j in range(len(other.obj[t])):
                    opp_uid = other.obj[t][j][-1]
                    opp_dist_x = other.obj[t][j][0]
                    opp_dist_y = other.obj[t][j][1]
                    diff_dist_x = abs(obj_dist_x - opp_dist_x)
                    diff_dist_y = abs(obj_dist_y - opp_dist_y)
                    # 1차 필터 : range 게이트
                    if diff_dist_x > cfg.r_gate_x or diff_dist_y > cfg.r_gate_y:
                        continue
                    # 2차 필터: 최솟값과 비교
                    diff_dist_r = math.sqrt(diff_dist_x ** 2 + diff_dist_y ** 2)
                    if diff_dist_r < min_dist:
                        min_dist = diff_dist_r
                        min_uid = opp_uid
                        pass
                    pass
                self.match[t][obj_uid] = min_uid
                pass
            pass
        pass

    def update_match(self, other, cfg: Config):
        for t in range(len(self.time)):
            for i in range(len(self.match[t])):
                if self.index[t][i] == cfg.mos_cnt or self.match[t][i] == cfg.dft_uid or self.match[t][i] == cfg.dft_uid + 0.1:
                    continue
                if self.match[t][i] != cfg.dft_uid and other.match[t][self.match[t][i]] == i:
                    continue
                obj_uid = i
                obj_idx = self.index[t][obj_uid]
                obj_dist_x = self.obj[t][obj_idx][0]
                obj_dist_y = self.obj[t][obj_idx][1]

                min_dist = max(cfg.r_gate_x, cfg.r_gate_y) * 2 + 1
                min_uid = cfg.dft_uid + 0.1
                for j in range(len(other.match[t])):
                    if other.match[t][j] != obj_uid:
                        continue
                    opp_uid = j
                    opp_idx = other.index[t][opp_uid]
                    opp_dist_x = other.obj[t][opp_idx][0]
                    opp_dist_y = other.obj[t][opp_idx][1]

                    diff_dist_x = abs(obj_dist_x - opp_dist_x)
                    diff_dist_y = abs(obj_dist_y - opp_dist_y)
                    diff_dist_r = math.sqrt(diff_dist_x ** 2 + diff_dist_y ** 2)

                    if diff_dist_r > min_dist:
                        other.match[t][opp_uid] = cfg.dft_uid + 0.1
                        pass
                    else:
                        if min_uid != cfg.dft_uid + 0.1:
                            other.match[t][min_uid] = cfg.dft_uid + 0.1
                            pass
                        min_dist = diff_dist_r
                        min_uid = opp_uid
                        pass
                    pass
                self.match[t][obj_uid] = min_uid
                pass
            pass
        for t in range(len(other.time)):
            for i in range(len(other.match[t])):
                if other.index[t][i] == cfg.mos_cnt or other.match[t][i] == cfg.dft_uid or other.match[t][i] == cfg.dft_uid + 0.1:
                    continue
                if other.match[t][i] != cfg.obj_cnt and self.match[t][other.match[t][i]] == i:
                    continue
                other.match[t][i] = cfg.dft_uid + 0.1
                pass
            pass
        pass

    def make_issue(self, cfg: Config):
        self.issue = [[] for _ in range(len(self.time))]
        for t in range(len(self.time)):
            for i in range(len(self.match[t])):
                if self.match[t][i] == cfg.dft_uid:
                    continue
                if self.match[t][i] == cfg.dft_uid + 0.1:
                    self.issue[t].append(self.obj[t][self.index[t][i]])
                    pass
                pass
            pass
        pass
    pass