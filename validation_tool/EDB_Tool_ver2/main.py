from Sumin.save import *
from Sumin.write import *
from Sumin.align import *
from Sumin.spread import *
from Sumin.process import *
from Sumin.extract import *
from Sumin.config import *
from BsigReader.prep import Prep
import os
import pandas as pd

# *** MAIN  ************************************************************************************************************
if __name__ == "__main__":
    # Input 폴더에서 file 탐색
    cfg = Config("RAD6(2)")
    files_ref = os.listdir(".\\Input_ref")
    files_sim = os.listdir(".\\Input_sim")
    path_ref = None
    path_sim = None
    old_data = None
    new_data = None
    target = None
    for file_ref in files_ref:
        exp_ref = file_ref.split(".")[-1]
        if exp_ref != "bsig":
            continue
        path_ref = ".\\Input_ref\\"+file_ref
        target = '_'.join(file_ref.split("_")[:-1])
        for file_sim in files_sim:
            exp_sim = file_sim.split(".")[-1]
            if exp_sim != "bsig":
                continue
            if '.'.join(file_sim.split(".")[:-1]) == target:
                path_sim = ".\\Input_sim\\"+file_sim
                break
        #파일 읽기
        old_data = Prep(path_ref).signal()
        new_data = Prep(path_sim).signal()

        #추출
        old_extract = Extract("old", cfg, old_data)
        new_extract = Extract("new", cfg, new_data)

        #처리
        old_process = Process(old_extract)
        new_process = Process(new_extract)
        old_process.make_match(new_process, cfg)
        new_process.make_match(old_process, cfg)
        old_process.update_match(new_process, cfg)
        old_process.make_issue(cfg)
        new_process.make_issue(cfg)

        #저장
        #old_align = Align(old_process)
        #new_align = Align(new_process)
        #save_excel = Save(old_align,new_align,file)
        old_spread = Spread(old_process)
        new_spread = Spread(new_process)
        write_excel = Write(old_spread,new_spread,target)

        ######참고####
        #사용 class
        #spread
        #write
        #process
        #extract
        #config
        







