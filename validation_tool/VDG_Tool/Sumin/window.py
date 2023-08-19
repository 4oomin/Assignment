from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QIcon
import sys
from Sumin.data import *

class Window(QWidget):
    def __init__(self,cfg,files):
        super().__init__()
        ########멤버 변수 #####
        self.cfg = cfg
        self.files = files
        self.timestamp = None
        self.timeindex = None

        self.old_time = None
        self.old_obj = None
        self.old_index = None
        self.old_match = None
        self.old_issue = None

        self.new_time = None
        self.new_obj = None
        self.new_index = None
        self.new_match = None
        self.new_issue = None

        ##### method 실행 ####
        self.initUI()
        self.setLayout(self.layout)
        self.resize(1200,800)
        self.center()
        pass

    def initUI(self):
        vbox_main = QVBoxLayout()
        vbox_toolbar = QVBoxLayout()
        hbox_graph = QHBoxLayout()
        vbox_main.addLayout(vbox_toolbar)
        vbox_main.addLayout(vbox_toolbar)
        vbox_main.addLayout(hbox_graph)
        self.layout = vbox_main

        tb1 = QToolBar()
        tb2 = QToolBar()
        vbox_toolbar.addWidget(tb1)
        vbox_toolbar.addWidget(tb2)

        gp1 = QVBoxLayout()
        gp2 = QVBoxLayout()
        self.fig1 = plt.Figure()
        self.fig2 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas2 = FigureCanvas(self.fig2)
        gp1.addWidget(self.canvas1)
        gp2.addWidget(self.canvas2)
        hbox_graph.addLayout(gp1)
        hbox_graph.addLayout(gp2)

        #########toolbar1########
        self.btn1 = QPushButton("Prev", self)
        font = self.btn1.font()
        font.setPointSize(10)
        self.btn1.setFont(font)
        tb1.addWidget(self.btn1)
        self.btn2 = QPushButton("Next", self)
        font = self.btn2.font()
        font.setPointSize(10)
        self.btn2.setFont(font)
        tb1.addWidget(self.btn2)

        lbl1 = QLabel("     TimeStamp : ")
        font = lbl1.font()
        font.setPointSize(10)
        lbl1.setFont(font)
        self.le1 = QLineEdit()
        font = self.le1.font()
        font.setPointSize(10)
        self.le1.setFont(font)
        tb1.addWidget(lbl1)
        tb1.addWidget(self.le1)
        self.btn3 = QPushButton("OK", self)
        font = self.btn3.font()
        font.setPointSize(10)
        self.btn3.setFont(font)
        tb1.addWidget(self.btn3)

        lbl2 = QLabel('     REF_uiID : ')
        font = lbl2.font()
        font.setPointSize(10)
        lbl2.setFont(font)
        self.le2 = QLineEdit()
        font = self.le2.font()
        font.setPointSize(10)
        self.le2.setFont(font)
        tb1.addWidget(lbl2)
        tb1.addWidget(self.le2)
        self.btn4 = QPushButton("OK", self)
        font = self.btn4.font()
        font.setPointSize(10)
        self.btn4.setFont(font)
        tb1.addWidget(self.btn4)

        lbl3 = QLabel('     SIM_uiID : ')
        font = lbl3.font()
        font.setPointSize(10)
        lbl3.setFont(font)
        self.le3 = QLineEdit()
        font = self.le3.font()
        font.setPointSize(10)
        self.le3.setFont(font)
        tb1.addWidget(lbl3)
        tb1.addWidget(self.le3)
        self.btn5 = QPushButton("OK", self)
        font = self.btn5.font()
        font.setPointSize(10)
        self.btn5.setFont(font)
        tb1.addWidget(self.btn5)

        #########toolbar2########
        self.cb = QComboBox(self)
        self.cb.addItems(self.files)
        font = self.cb.font()
        font.setPointSize(10)
        self.cb.setFont(font)
        tb2.addWidget(self.cb)
        self.btn6 = QPushButton("OK", self)
        font = self.btn6.font()
        font.setPointSize(10)
        self.btn6.setFont(font)
        tb2.addWidget(self.btn6)
        lbl5 = QLabel('         TimeStamp :  ')
        font = lbl5.font()
        font.setPointSize(10)
        lbl5.setFont(font)
        self.lbl5 = QLabel()
        font = self.lbl5.font()
        font.setPointSize(10)
        self.lbl5.setFont(font)
        tb2.addWidget(lbl5)
        tb2.addWidget(self.lbl5)
        lbl6 = QLabel('         REF_uiID :  ')
        font = lbl6.font()
        font.setPointSize(10)
        lbl6.setFont(font)
        self.lbl6 = QLabel()
        font = self.lbl6.font()
        font.setPointSize(10)
        self.lbl6.setFont(font)
        tb2.addWidget(lbl6)
        tb2.addWidget(self.lbl6)
        lbl7 = QLabel('         SIM_uiID :  ')
        font = lbl7.font()
        font.setPointSize(10)
        lbl7.setFont(font)
        self.lbl7 = QLabel()
        font = self.lbl7.font()
        font.setPointSize(10)
        self.lbl7.setFont(font)
        tb2.addWidget(lbl7)
        tb2.addWidget(self.lbl7)

        #########connect button########
        self.btn1.clicked.connect(self.prev_event)
        self.btn2.clicked.connect(self.next_event)
        self.btn3.clicked.connect(self.time_event)
        self.btn4.clicked.connect(self.old_event)
        self.btn5.clicked.connect(self.new_event)
        self.btn6.clicked.connect(self.file_event)


    def prev_event(self):
        self.timeindex = self.timeindex-1
        self.timestamp = self.old_time[self.timeindex]
        self.lbl5.setText(str(int(self.timestamp)) + ' [' + str(self.timeindex) + ']')
        old_distX = [obj[0] for obj in self.old_obj[self.timeindex]]
        old_distY = [obj[1] for obj in self.old_obj[self.timeindex]]
        new_distX = [obj[0] for obj in self.new_obj[self.timeindex]]
        new_distY = [obj[1] for obj in self.new_obj[self.timeindex]]

        del_distX = [obj[0] for obj in self.old_issue[self.timeindex]]
        del_distY = [obj[1] for obj in self.old_issue[self.timeindex]]
        eme_distX = [obj[0] for obj in self.new_issue[self.timeindex]]
        eme_distY = [obj[1] for obj in self.new_issue[self.timeindex]]

        self.fig1.clear()
        ax1 = self.fig1.add_subplot(1, 1, 1)
        ax1.set_xlim(-60, 60)
        ax1.set_ylim(0, 300)
        ax1.spines['left'].set_position('center')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['bottom'].set_position(('data', 0))
        ax1.set_aspect(0.5)
        ax1.scatter(old_distY, old_distX, s=10, c='gainsboro')
        ax1.scatter(new_distY, new_distX, s=10, c='gainsboro')
        ax1.scatter(del_distY, del_distX, s=10, c='red')
        ax1.scatter(eme_distY, eme_distX, s=10, c='green')
        ax1.legend(("","keep(REF_uiID)","delete(REF_uiID)","emerge(SIM_uiID)"))
        for i in range(len(old_distX)):
            ax1.text(old_distY[i], old_distX[i], int(self.old_obj[self.timeindex][i][-1]), fontsize=7)

        for i in range(len(eme_distX)):
            ax1.text(eme_distY[i], eme_distX[i], int(self.new_issue[self.timeindex][i][-1]), fontsize=7)

        self.canvas1.draw()
        pass
    def next_event(self):
        self.timeindex = self.timeindex + 1
        self.timestamp = self.old_time[self.timeindex]
        self.lbl5.setText(str(int(self.timestamp)) + ' [' + str(self.timeindex) + ']')
        old_distX = [obj[0] for obj in self.old_obj[self.timeindex]]
        old_distY = [obj[1] for obj in self.old_obj[self.timeindex]]
        new_distX = [obj[0] for obj in self.new_obj[self.timeindex]]
        new_distY = [obj[1] for obj in self.new_obj[self.timeindex]]

        del_distX = [obj[0] for obj in self.old_issue[self.timeindex]]
        del_distY = [obj[1] for obj in self.old_issue[self.timeindex]]
        eme_distX = [obj[0] for obj in self.new_issue[self.timeindex]]
        eme_distY = [obj[1] for obj in self.new_issue[self.timeindex]]

        self.fig1.clear()
        ax1 = self.fig1.add_subplot(1, 1, 1)
        ax1.set_xlim(-60, 60)
        ax1.set_ylim(0, 300)
        ax1.spines['left'].set_position('center')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['bottom'].set_position(('data', 0))
        ax1.set_aspect(0.5)
        ax1.scatter(old_distY, old_distX, s=10, c='gainsboro')
        ax1.scatter(new_distY, new_distX, s=10, c='gainsboro')
        ax1.scatter(del_distY, del_distX, s=10, c='red')
        ax1.scatter(eme_distY, eme_distX, s=10, c='green')
        ax1.legend(("","keep(REF_uiID)","delete(REF_uiID)","emerge(SIM_uiID)"))
        for i in range(len(old_distX)):
            ax1.text(old_distY[i], old_distX[i], int(self.old_obj[self.timeindex][i][-1]), fontsize=7)

        for i in range(len(eme_distX)):
            ax1.text(eme_distY[i], eme_distX[i], int(self.new_issue[self.timeindex][i][-1]), fontsize=7)

        self.canvas1.draw()
        pass
    def time_event(self):
        self.timestamp = int(self.le1.text())
        tmp = 10e10
        for t in range(len(self.old_time)):
            if tmp > abs(self.timestamp - self.old_time[t]):
                tmp = abs(self.timestamp - self.old_time[t])
                self.timeindex = t
        self.lbl5.setText(str(int(self.old_time[self.timeindex]))+' ['+str(self.timeindex)+']')

        old_distX = [obj[0] for obj in self.old_obj[self.timeindex]]
        old_distY = [obj[1] for obj in self.old_obj[self.timeindex]]
        new_distX = [obj[0] for obj in self.new_obj[self.timeindex]]
        new_distY = [obj[1] for obj in self.new_obj[self.timeindex]]

        del_distX = [obj[0] for obj in self.old_issue[self.timeindex]]
        del_distY = [obj[1] for obj in self.old_issue[self.timeindex]]
        eme_distX = [obj[0] for obj in self.new_issue[self.timeindex]]
        eme_distY = [obj[1] for obj in self.new_issue[self.timeindex]]

        self.fig1.clear()
        ax1 = self.fig1.add_subplot(1, 1, 1)
        ax1.set_xlim(-60, 60)
        ax1.set_ylim(0, 300)
        ax1.spines['left'].set_position('center')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['bottom'].set_position(('data', 0))
        ax1.set_aspect(0.5)
        ax1.scatter(old_distY, old_distX, s=10, c='gainsboro')
        ax1.scatter(new_distY, new_distX, s=10, c='gainsboro')
        ax1.scatter(del_distY, del_distX, s=10, c='red')
        ax1.scatter(eme_distY, eme_distX, s=10, c='green')
        ax1.legend(("","keep(REF_uiID)","delete(REF_uiID)","emerge(SIM_uiID)"))

        for i in range(len(old_distX)):
            ax1.text(old_distY[i], old_distX[i], int(self.old_obj[self.timeindex][i][-1]), fontsize=7)

        for i in range(len(eme_distX)):
            ax1.text(eme_distY[i], eme_distX[i], int(self.new_issue[self.timeindex][i][-1]), fontsize=7)
        self.canvas1.draw()
        pass
    def old_event(self):
        old_uid = int(self.le2.text())
        self.lbl6.setText(str(old_uid) + ' [' + str(self.timeindex) + ']')
        old_distX = []
        old_distY = []
        old_timeT = []
        for t in range(self.timeindex - 20, self.timeindex + 20):
            if self.old_index[t][old_uid] == self.cfg.mos_cnt:
                continue
            old_distX.append(self.old_obj[t][self.old_index[t][old_uid]][0])
            old_distY.append(self.old_obj[t][self.old_index[t][old_uid]][1])
            old_timeT.append(t-self.timeindex)
            pass

        new_uid = self.old_match[self.timeindex][old_uid] # -1 은 old가 없을때 -0.9는 old 대응이 없을 때 ,float형
        if new_uid == self.cfg.dft_uid+0.1:
            self.lbl7.setText(str(new_uid) + ' [' + str(self.timeindex) + ']')
        else:
            self.lbl7.setText(str(int(new_uid))+' [' + str(self.timeindex) + ']')

        new_distX = []
        new_distY = []
        new_timeT = []
        for t in range(self.timeindex - 20, self.timeindex + 20):
            if self.old_index[t][old_uid] == self.cfg.mos_cnt:
                continue
            new_uid = self.old_match[t][old_uid]
            if new_uid == self.cfg.dft_uid+0.1:
                continue
            new_uid = int(new_uid)
            new_distX.append(self.new_obj[t][self.new_index[t][new_uid]][0])
            new_distY.append(self.new_obj[t][self.new_index[t][new_uid]][1])
            new_timeT.append(t - self.timeindex)
            pass
        
        self.fig2.clear()
        ax3 = self.fig2.add_subplot(2, 1, 1)
        ax4 = self.fig2.add_subplot(2, 1, 2)
        ax3.set_xlim(-20,20)
        ax4.set_xlim(-20,20)
        ax3.grid()
        ax3.scatter(new_timeT, new_distX, c='green')
        ax3.scatter(old_timeT, old_distX, c='red', marker='x')
        ax3.set_title("distX")
        ax3.legend(("SIM","REF"))
        ax4.grid()
        ax4.scatter(new_timeT, new_distY, c='green')
        ax4.scatter(old_timeT, old_distY, c='red', marker='x')
        ax4.set_title("distY")
        ax4.legend(("SIM","REF"))
        self.canvas2.draw()
        pass
    def new_event(self):
        new_uid = int(self.le3.text())
        self.lbl7.setText(str(new_uid) + ' [' + str(self.timeindex) + ']')
        new_distX = []
        new_distY = []
        new_timeT = []
        for t in range(self.timeindex - 20, self.timeindex + 20):
            if self.new_index[t][new_uid] == self.cfg.mos_cnt:
                continue
            new_distX.append(self.new_obj[t][self.new_index[t][new_uid]][0])
            new_distY.append(self.new_obj[t][self.new_index[t][new_uid]][1])
            new_timeT.append(t - self.timeindex)
            pass

        old_uid = self.new_match[self.timeindex][new_uid]  # -1 은 old가 없을때 -0.9는 old 대응이 없을 때 ,float형
        if old_uid == self.cfg.dft_uid + 0.1:
            self.lbl6.setText(str(old_uid) + ' [' + str(self.timeindex) + ']')
        else:
            self.lbl6.setText(str(int(old_uid)) + ' [' + str(self.timeindex) + ']')

        old_distX = []
        old_distY = []
        old_timeT = []
        for t in range(self.timeindex - 20, self.timeindex + 20):
            if self.new_index[t][new_uid] == self.cfg.mos_cnt:
                continue
            old_uid = self.new_match[t][new_uid]
            if old_uid == self.cfg.dft_uid + 0.1:
                continue
            old_uid = int(old_uid)
            old_distX.append(self.old_obj[t][self.old_index[t][old_uid]][0])
            old_distY.append(self.old_obj[t][self.old_index[t][old_uid]][1])
            old_timeT.append(t - self.timeindex)
            pass

        self.fig2.clear()
        ax3 = self.fig2.add_subplot(2, 1, 1)
        ax4 = self.fig2.add_subplot(2, 1, 2)
        ax3.set_xlim(-20, 20)
        ax4.set_xlim(-20, 20)
        ax3.grid()
        ax3.scatter(new_timeT, new_distX, c='green')
        ax3.scatter(old_timeT, old_distX, c='red', marker='x')
        ax3.set_title("distX")
        ax3.legend(("SIM","REF"))
        ax4.grid()
        ax4.scatter(new_timeT, new_distY, c='green')
        ax4.scatter(old_timeT, old_distY, c='red', marker='x')
        ax4.set_title("distY")
        ax4.legend(("SIM","REF"))
        self.canvas2.draw()
        pass
    def file_event(self):
        file = self.cb.currentText()
        data = Data(self.cfg, file)
        self.old_time = data.old_time
        self.old_obj = data.old_obj
        self.old_index = data.old_index
        self.old_match = data.old_match
        self.old_issue = data.old_issue

        self.new_time = data.new_time
        self.new_obj = data.new_obj
        self.new_index = data.new_index
        self.new_match = data.new_match
        self.new_issue = data.new_issue

        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        pass

    pass