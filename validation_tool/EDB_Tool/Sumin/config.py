class Config:
    def __init__(self, RAD):
        self.RAD = RAD
        self.old_signal = None
        self.new_signal = None
        self.obj_dict = None
        self.dft_uid = None
        self.obj_cnt = None
        self.mos_cnt = None
        self.r_gate_y = None
        self.r_gate_x = None
        self.config()
        pass

    def config(self):
        if self.RAD == "RAD5":
            self.old_signal = "ARS5xx"
            self.new_signal = "SIM VFB ALL"
            self.obj_dict = {"fDistX": 0, "fDistY": 1,"uiID": 2}
            self.dft_uid = 255
            self.obj_cnt = 100
            self.mos_cnt = 32

        elif self.RAD == "RAD6":
            self.old_signal = "ARS620"
            self.new_signal = "SIM VFB ALL_FM-L"
            self.obj_dict = {"distX": 0, "distY": 1, "internalObjectID": 2}
            self.dft_uid = -1
            self.obj_cnt = 100
            self.mos_cnt = 50

        self.r_gate_x = 2
        self.r_gate_y = 1.5
        pass

    pass