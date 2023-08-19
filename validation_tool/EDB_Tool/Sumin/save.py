from Sumin.align import *
import openpyxl
import pandas as pd

class Save:
    def __init__(self,old_align,new_align,file:str):
        self.old_time = old_align.a_time
        self.old_obj = old_align.a_obj
        self.old_match = old_align.a_match
        self.old_issue = old_align.a_issue
        self.new_time = new_align.a_time
        self.new_obj = new_align.a_obj
        self.new_match = new_align.a_match
        self.new_issue = new_align.a_issue
        self.file = file
        self.excel_save()
        pass

    def excel_save(self):
        df_old_time = pd.DataFrame(self.old_time,columns=["TimeIndex","TimeStamp"])
        df_old_obj = pd.DataFrame(self.old_obj,columns=["TimeIndex","distX","distY","uiID"])
        df_old_match = pd.DataFrame(self.old_match,columns=["TimeIndex","SuiID","OuiID"])
        df_old_issue = pd.DataFrame(self.old_issue,columns=["TimeIndex","distX","distY","uiID"])
        df_new_time = pd.DataFrame(self.new_time,columns=["TimeIndex","TimeStamp"])
        df_new_obj = pd.DataFrame(self.new_obj,columns=["TimeIndex","distX","distY","uiID"])
        df_new_match = pd.DataFrame(self.new_match,columns=["TimeIndex","SuiID","OuiID"])
        df_new_issue = pd.DataFrame(self.new_obj,columns=["TimeIndex","distX","distY","uiID"])

        writer = pd.ExcelWriter(".\\Output\\" + ''.join(self.file.split(".")[:-1]) + ".xlsx",engine='openpyxl')
        df_old_time.to_excel(writer,sheet_name="old_time",startrow=0, startcol=0, index=False)
        df_old_obj.to_excel(writer,sheet_name="old_obj",startrow=0, startcol=0, index=False)
        df_old_match.to_excel(writer,sheet_name="old_match",startrow=0, startcol=0, index=False)
        df_old_issue.to_excel(writer,sheet_name="old_issue",startrow=0, startcol=0, index=False)
        df_new_time.to_excel(writer, sheet_name="new_time", startrow=0, startcol=0, index=False)
        df_new_obj.to_excel(writer,sheet_name="new_obj",startrow=0, startcol=0, index=False)
        df_new_match.to_excel(writer,sheet_name="new_match",startrow=0, startcol=0, index=False)
        df_new_issue.to_excel(writer,sheet_name="new_issue",startrow=0, startcol=0, index=False)
        writer.save()

        pass
    pass