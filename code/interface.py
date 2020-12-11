# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:19:46 2020

@author: elena
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel
import sys
import qtawesome
import pymysql

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #define main window
        self.setFixedSize(1000, 800)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        #define left part
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        #define right part
        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)
        
        self.main_layout.addWidget(self.left_widget,0,0,6,2)
        self.main_layout.addWidget(self.right_widget,0,2,6,10)
        self.setCentralWidget(self.main_widget)
        #--------------------------------------------------------------
        #define left buttons
        self.left_mini = QtWidgets.QPushButton("")
        self.left_return = QtWidgets.QPushButton("")
        self.left_close = QtWidgets.QPushButton("")
        
        self.left_label_1 = QtWidgets.QPushButton("Daily Recommendation")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("My Profile")
        self.left_label_2.setObjectName('left_label')
        
        
        self.left_button_1 = QtWidgets.QPushButton("Item")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.addNum)
        self.left_button_2 = QtWidgets.QPushButton("Browse History")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton("Purchase History")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton("My Favorite")
        self.left_button_4.setObjectName('left_button')
        
        self.left_layout.addWidget(self.left_mini,0,0,1,1)
        self.left_layout.addWidget(self.left_return,0,1,1,1)
        self.left_layout.addWidget(self.left_close,0,2,1,1)
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1,2,0,1,3)
        self.left_layout.addWidget(self.left_label_2,3,0,1,3)
        self.left_layout.addWidget(self.left_button_2,4,0,1,3)
        self.left_layout.addWidget(self.left_button_3,5,0,1,3)
        self.left_layout.addWidget(self.left_button_4,6,0,1,3)
        #--------------------------------------------------------------        
        self.right_userid_widget = QtWidgets.QWidget()
        self.right_userid_layout = QtWidgets.QGridLayout()
        self.right_userid_widget.setLayout(self.right_userid_layout)
        self.search_icon1 = QtWidgets.QLabel(chr(0xf007) + ' ' + 'Login  ')
        self.search_icon1.setFont(qtawesome.font('fa', 16))
        self.right_userid_widget_search_input = QtWidgets.QLineEdit()
        self.right_userid_widget_search_input.setPlaceholderText("Enter UserId")
             
        self.right_recommend_widget = QtWidgets.QWidget()
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)
        
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("Product1")
        self.recommend_button_1.clicked.connect(self.button1_read_Clicked)
        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("Product2")
        self.recommend_button_2.clicked.connect(self.button2_read_Clicked)
        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("Product3")
        self.recommend_button_3.clicked.connect(self.button3_read_Clicked)
        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("Product4")
        
        self.recommend_label_1 = QLabel(self)
        self.recommend_label_1.setGeometry(300, 250, 300, 100)
        self.recommend_label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.recommend_label_2 = QLabel(self)
        self.recommend_label_2.setGeometry(650, 250, 300, 100)
        self.recommend_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.recommend_label_3 = QLabel(self)
        self.recommend_label_3.setGeometry(300, 400, 300, 100)
        self.recommend_label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.recommend_label_4 = QLabel(self)
        self.recommend_label_4.setGeometry(650, 400, 300, 100)
        self.recommend_label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.recommend_label_5 = QLabel(self)
        self.recommend_label_5.setGeometry(475, 550, 300, 100)
        self.recommend_label_5.setFrameShape(QtWidgets.QFrame.Box)

 
        self.right_userid_layout.addWidget(self.search_icon1, 0, 0, 1, 1)
        self.right_userid_layout.addWidget(self.right_userid_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_userid_widget, 0, 0, 1, 9)
        

        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 2, 9)
        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        
        #--------------------------------------------------------------
        #decoration-left
        self.left_mini.setFixedSize(30, 30)
        self.left_return.setFixedSize(30, 30)
        self.left_close.setFixedSize(30, 30)
        
        self.left_return.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_widget.setStyleSheet('''
            QWidget#left_widget{
                background: gray;
                border - top: 1px solid white;
                border - bottom: 1px solid white;
                border - left: 1px solid white;
                border - top - left - radius: 10px;
                border - bottom - left - radius: 10px;
            }
        
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                color:#232C51;
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
           
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        #decoration-right
        self.right_userid_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                 
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        #decoration-whole
        self.setWindowOpacity(0.95)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)
        
    def addNum(self):
        userId = self.right_userid_widget_search_input.text()
        print(userId)
        
    def button1_read_Clicked(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="project")
        cur = conn.cursor()
        
        sql = "SELECT UserId, recommended_item, category_code, brand, frequency\
        FROM (SELECT UserId, recommended_item, frequency FROM recommended_item_single\
         WHERE UserId = '113868975' order by frequency DESC LIMIT 5) as recommend_round1\
        INNER JOIN original_data o\
        ON recommend_round1.recommended_item = o.product_id"
        
        cur.execute(sql)
        data1 = cur.fetchall()
        self.recommend_label_1.setText(data1[0][2])
        self.recommend_label_2.setText(data1[1][2])
        self.recommend_label_3.setText(data1[2][2])
        self.recommend_label_4.setText(data1[3][2])
        self.recommend_label_5.setText(data1[4][2])
        print(data1)
        

    def button2_read_Clicked(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="project")
        cur = conn.cursor()

        sql = "select recommended_item_1 reference_item, recommended_item_2 recommended_item, category_code, brand\
            from (select recommended_item_1, recommended_item_2, frequency from recommended_item_pairs\
             where recommended_item_1 = '1005115'\
            group by recommended_item_2\
            order by frequency DESC LIMIT 5) as recommend_round2\
            inner join original_data o\
            on recommended_item_2 = o.product_id\
            group by recommended_item_2\
            order by frequency\
            DESC LIMIT 5"

        cur.execute(sql)
        data2 = cur.fetchall()
        self.recommend_label_1.setText(data2[0][2])
        self.recommend_label_2.setText(data2[1][2])
        self.recommend_label_3.setText(data2[2][2])
        self.recommend_label_4.setText(data2[3][2])
        self.recommend_label_5.setText(data2[4][2])
        print(data2)
        
    def button3_read_Clicked(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="project")
        cur = conn.cursor()

        sql = "select reference_item1, reference_item2, recommended_item, category_code, brand from\
        (select recommended_item_1 reference_item1, recommended_item_2 reference_item2, recommended_item_3 recommended_item, frequency\
         from recommended_item_triple rt\
         where rt.recommended_item_1 = '1005115'\
         and rt.recommended_item_2 = '1004226'\
         group by recommended_item\
         order by frequency\
         DESC LIMIT 5) as recommend_round3\
        inner join original_data o\
        on o.product_id = recommend_round3.recommended_item"

        cur.execute(sql)
        
        data3 = cur.fetchall() 
        self.recommend_label_1.setText(data3[0][3])
        self.recommend_label_2.setText(data3[1][3])
        self.recommend_label_3.setText(data3[2][3])
        self.recommend_label_4.setText(data3[3][3])
        self.recommend_label_5.setText(data3[4][3])
        print(data3)
    
    def button4_read_Clicked(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="project")
        cur = conn.cursor()

        sql = "select reference_item1, reference_item2, reference_item3, recommended_item, category_code, brand from\
        (select recommended_item_1 reference_item1, recommended_item_2 reference_item2, recommended_item_3 reference_item3,\
         recommended_item_4 recommended_item, frequency from recommended_item_four rf\
         where rf.recommended_item_1 = '1005115'\
         and rf.recommended_item_2 = '1004226'\
         and rf.recommended_item_3 = '1004249'\
         group by recommended_item\
         order by frequency\
         DESC LIMIT 5) as recommend_round4\
        inner join original_data o\
        on o.product_id = recommend_round4.recommended_item"

        cur.execute(sql)
        
        data4 = cur.fetchall() 
        self.recommend_label_1.setText(data4[0][4])
        self.recommend_label_2.setText(data4[1][4])
        self.recommend_label_3.setText(data4[2][4])
        self.recommend_label_4.setText(data4[3][4])
        self.recommend_label_5.setText(data4[4][4])
        print(data4)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()