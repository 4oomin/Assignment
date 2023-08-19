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
    cfg = Config("RAD6")
    files = os.listdir(".\\Input")
    data = None
    for file in files:
        exp = file.split(".")[-1]
        if exp not in ["csv", "bsig"]:
            continue
        path = ".\\Input\\"+file
        #파일 읽기
        if exp == "csv":
            data = pd.read_csv(path)
            pass
        elif exp == "bsig":
            data = Prep(path).signal()
            pass

        #추출
        old_extract = Extract("old", cfg, data)
        new_extract = Extract("new", cfg, data)

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
        write_excel = Write(old_spread,new_spread,file)


        ######참고####
        #사용 class
        #spread
        #write
        #process
        #extract
        #config
        







