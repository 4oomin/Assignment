class Config:
    def __init__(self,RAD):
        self.obj_cnt = None
        self.mos_cnt = None
        self.dft_uid = None
        self.RAD = RAD
        self.set_config()
        pass
    def set_config(self):
        if self.RAD == "RAD6":
            self.obj_cnt = 100
            self.mos_cnt = 50
            self.dft_uid = -1

        elif self.RAD == "RAD5":
            self.obj_cnt = 100
            self.mos_cnt = 32
            self.dft_uid = 255
        pass
    pass