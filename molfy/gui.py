import cv2 as cv
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import tensorflow as tf
import numpy as np
import serial,time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = tf.keras.models.load_model('3_facial_recongnition_model.h5',compile=False)
        self.ser = serial.Serial('COM3', 9600)

    def initUI(self):

        # 툴바
        hbox_tool = QHBoxLayout()
        label_timer = QLabel('Timer : ', self)
        self.label_sec = QLabel('0 sec', self)
        button_on = QPushButton('start car', self)
        button_on.clicked.connect(self.start)
        hbox_tool.addWidget(label_timer)
        hbox_tool.addSpacing(20)
        hbox_tool.addWidget(self.label_sec)
        hbox_tool.addSpacing(20)
        hbox_tool.addWidget(button_on)
        hbox_tool.addSpacing(100)

        # 주황 박스 (이미지 프레임)
        vbox_cam = QVBoxLayout()
        self.label = QLabel()
        vbox_cam.addWidget(self.label)

        # 초록 박스 (state)
        vbox_state = QVBoxLayout()
        label_title = QLabel('Facial expression', self)
        label_title.setAlignment(Qt.AlignCenter)
        font_title = label_title.font()
        font_title.setPointSize(20)
        label_title.setFont(font_title)

        self.label_priority = QLabel('None', self)
        self.label_priority.setAlignment(Qt.AlignCenter)
        font_priority = self.label_priority.font()
        font_priority.setPointSize(50)
        font_priority.setBold(True)
        self.label_priority.setFont(font_priority)

        label_type1 = QLabel('happy', self)
        font_type1 = label_type1.font()
        font_type1.setPointSize(15)
        label_type1.setFont(font_type1)

        label_type2 = QLabel('neutral', self)
        font_type2 = label_type2.font()
        font_type2.setPointSize(15)
        label_type2.setFont(font_type2)

        label_type3 = QLabel('sad', self)
        font_type3 = label_type3.font()
        font_type3.setPointSize(15)
        label_type3.setFont(font_type3)

        self.label_happy = QLabel('0%', self)
        font_happy = self.label_happy.font()
        font_happy.setPointSize(15)
        self.label_happy.setFont(font_happy)

        self.label_neutral = QLabel('0%', self)
        font_neutral = self.label_neutral.font()
        font_neutral.setPointSize(15)
        self.label_neutral.setFont(font_neutral)

        self.label_sad = QLabel('0%', self)
        font_sad = self.label_sad.font()
        font_sad.setPointSize(15)
        self.label_sad.setFont(font_sad)

        label_tmp1 = QLabel('', self)
        font_tmp1 = label_tmp1.font()
        font_tmp1.setPointSize(5)
        label_tmp1.setFont(font_tmp1)

        label_tmp2 = QLabel('', self)
        font_tmp2 = label_tmp2.font()
        font_tmp2.setPointSize(5)
        label_tmp2.setFont(font_tmp2)

        h1 = QHBoxLayout()
        h1.addWidget(label_type1)
        h1.addWidget(self.label_happy)
        h2 = QHBoxLayout()
        h2.addWidget(label_type2)
        h2.addWidget(self.label_neutral)
        h3 = QHBoxLayout()
        h3.addWidget(label_type3)
        h3.addWidget(self.label_sad)

        vbox_state.addWidget(label_title)
        vbox_state.addWidget(self.label_priority)
        vbox_state.addWidget(label_tmp1)
        vbox_state.addLayout(h1)
        vbox_state.addLayout(h2)
        vbox_state.addLayout(h3)
        vbox_state.addWidget(label_tmp2)

        # 투명박스
        vbox_tmp = QVBoxLayout()
        label_tmp = QLabel(" ", self)
        vbox_tmp.addWidget(label_tmp)

        # 파랑 박스 (전체)
        hbox_total = QHBoxLayout()
        hbox_total.addLayout(vbox_cam)
        hbox_total.addLayout(vbox_tmp)
        hbox_total.addLayout(vbox_state)

        vbox_total = QVBoxLayout()
        vbox_total.addLayout(hbox_tool)
        vbox_total.addLayout(hbox_total)

        self.setLayout(vbox_total)
        self.resize(750, 300)
        self.center()
        self.show()
        pass

    def start(self):
        pixmap = QPixmap('current.jpg')
        self.label.setPixmap(pixmap)
        cropped = cv.imread('cropped.jpg')
        resized = cv.resize(cropped,dsize=(96,96),interpolation=cv.INTER_LINEAR)
        graied = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
        nped = np.array(graied)
        img = nped.reshape((1,nped.shape[0],nped.shape[1],1))
        predict = self.model.predict(img)
        label = predict[0].argmax()
        print(label)
        #for i in [3, 2, 1, 0]:
            #self.label_sec.setText(str(i) + " sec")
            #QtTest.QTest.qWait(1000)

        happy_prob = 0
        neutral_prob = 0
        sad_prob = 0
        time.sleep(2)
        if label == 0:
            happy_prob = predict[0][0]*100
            neutral_prob = predict[0][1]*100
            sad_prob = predict[0][2]*100
            self.label_priority.setText("Positive")
            self.ser.write(b'H')
            pass
        elif label == 1:
            happy_prob = predict[0][0]*100
            neutral_prob = predict[0][1]*100
            sad_prob = predict[0][2]*100
            self.label_priority.setText("Neutral")
            self.ser.write(b'N')
            pass
        elif label == 2:
            happy_prob = predict[0][0]*100
            neutral_prob = predict[0][1]*100
            sad_prob = predict[0][2]*100
            self.label_priority.setText("Negative")
            self.ser.write(b'S')
            pass
        self.label_happy.setText(str(happy_prob) + " %")
        self.label_neutral.setText(str(neutral_prob) + " %")
        self.label_sad.setText(str(sad_prob) + " %")

        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
