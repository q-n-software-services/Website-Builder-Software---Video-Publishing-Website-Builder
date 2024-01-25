import os
import pyperclip
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox,  QTabWidget, QCheckBox, QLCDNumber,QListWidget, QListWidgetItem, QLabel, QWidget, QPushButton,QComboBox, QFileDialog,QLineEdit, QTextEdit
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer, Qt
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1350, 700)
        self.setWindowTitle("Video Domainer Site Builder Tool")
        self.setWindowIcon(QIcon("burger.ico"))
        self.setStyleSheet("background-color:White")

        self.main_function()

    def main_function(self):
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        hbox = QHBoxLayout()

        self.label = QLabel("Video Domainer Site Builder Tool")
        self.label.setStyleSheet("background-color:cyan; color: black;")
        self.label.setFont(QFont("times new roman", 36))
        self.label.setFixedHeight(72)
        #self.label.setFixedWidth(600)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.label2 = QLabel("Article source folder")
        self.label2.setStyleSheet("background-color:white;")
        self.label2.setFont(QFont("times new roman", 16))
        self.label2.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label2.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label2)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setStyleSheet("background-color:white;")
        self.line_edit1.setFont(QFont("times new roman", 16))
        self.line_edit1.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.line_edit1.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.line_edit1)

        btn1 = QPushButton("Browse")
        btn1.setStyleSheet("background-color:magenta; color: white;")
        btn1.setFont(QFont("times new roman", 14))
        btn1.setFixedHeight(36)
        btn1.setFixedWidth(72)
        btn1.clicked.connect(self.open1)
        vbox3.addWidget(btn1)


        self.label3 = QLabel("Template Folder")
        self.label3.setStyleSheet("background-color:white;")
        self.label3.setFont(QFont("times new roman", 16))
        self.label3.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label3.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label3)

        self.line_edit2 = QLineEdit()
        self.line_edit2.setStyleSheet("background-color:white;")
        self.line_edit2.setFont(QFont("times new roman", 16))
        self.line_edit2.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.line_edit2.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.line_edit2)

        btn2 = QPushButton("Browse")
        btn2.setStyleSheet("background-color:magenta; color: white;")
        btn2.setFont(QFont("times new roman", 14))
        btn2.setFixedHeight(36)
        btn2.setFixedWidth(72)
        btn2.clicked.connect(self.open2)
        vbox3.addWidget(btn2)


        self.label4 = QLabel("Site Name")
        self.label4.setStyleSheet("background-color:white;")
        self.label4.setFont(QFont("times new roman", 16))
        self.label4.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label4.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label4)

        self.line_edit3 = QLineEdit()
        self.line_edit3.setStyleSheet("background-color:white;")
        self.line_edit3.setFont(QFont("times new roman", 16))
        self.line_edit3.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.line_edit3.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.line_edit3)

        self.label6 = QLabel("Type of Site")
        self.label6.setStyleSheet("background-color:white;")
        self.label6.setFont(QFont("times new roman", 16))
        self.label6.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label6.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label6)

        self.site_type = QComboBox()
        self.site_type.setStyleSheet("background-color:white;")
        self.site_type.setFont(QFont("times new roman", 16))
        self.site_type.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.site_type.addItem("Simple Video Site")
        self.site_type.addItem("Offline Site")
        self.site_type.addItem("Squeeze Site")
        self.site_type.addItem("Sales Site")
        self.site_type.currentIndexChanged.connect(self.hovered)
        vbox2.addWidget(self.site_type)

        self.label5 = QLabel("YouTube Keywords")
        self.label5.setStyleSheet("background-color:white;")
        self.label5.setFont(QFont("times new roman", 16))
        self.label5.setFixedHeight(144)
        #self.label.setFixedWidth(600)
        self.label5.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label5)

        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("background-color:white;")
        self.text_edit.setFont(QFont("times new roman", 16))
        self.text_edit.setFixedHeight(144)
        #self.label.setFixedWidth(600)
        self.text_edit.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.text_edit)

        self.label7 = QLabel("Video Source")
        self.label7.setStyleSheet("background-color:white;")
        self.label7.setFont(QFont("times new roman", 16))
        self.label7.setFixedHeight(50)
        #self.label.setFixedWidth(600)
        self.label7.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label7)

        self.video_source = QComboBox()
        self.video_source.setStyleSheet("background-color:white;")
        self.video_source.setFont(QFont("times new roman", 16))
        self.video_source.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.video_source.addItem("The current YouTube feed")
        self.video_source.addItem("The Video List (the same videos that were used last time)")
        self.video_source.addItem("The Video List PLUS additional videos from Youtube")
        self.video_source.currentIndexChanged.connect(self.hovered2)
        vbox2.addWidget(self.video_source)

        self.check1 = QCheckBox("Insert any additional videos at the front of the site")
        self.label7.setAlignment(Qt.AlignCenter)
        self.check1.setIconSize(QSize(50, 50))
        self.check1.setFont(QFont("times new roman", 12))
        self.check1.setDisabled(True)
        self.check1.toggled.connect(self.item_selected)
        vbox2.addWidget(self.check1)

        self.label8 = QLabel("YouTube Feed to use")
        self.label8.setStyleSheet("background-color:white;")
        self.label8.setFont(QFont("times new roman", 16))
        self.label8.setFixedHeight(50)
        #self.label.setFixedWidth(600)
        self.label8.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label8)

        self.youtube_feed = QComboBox()
        self.youtube_feed.setStyleSheet("background-color:white;")
        self.youtube_feed.setFont(QFont("times new roman", 16))
        self.youtube_feed.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.youtube_feed.addItem("Most popular videos")
        self.youtube_feed.addItem("Most relevant videos")
        self.youtube_feed.addItem("Most recent videos")
        self.youtube_feed.addItem("Most popular videos first - then the other feeds")
        self.youtube_feed.addItem("Most relevant videos first - then the other feeds")
        self.youtube_feed.addItem("Most recent videos first - then the other feeds")
        self.youtube_feed.currentIndexChanged.connect(self.hovered3)
        vbox2.addWidget(self.youtube_feed)

        self.label9 = QLabel("Number of Video Pages")
        self.label9.setStyleSheet("background-color:white;")
        self.label9.setFont(QFont("times new roman", 16))
        self.label9.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label9.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label9)

        self.line_edit4 = QLineEdit()
        self.line_edit4.setStyleSheet("background-color:white;")
        self.line_edit4.setFont(QFont("times new roman", 16))
        self.line_edit4.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.line_edit4.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.line_edit4)

        self.label10 = QLabel()
        self.label10.setFixedHeight(385)
        vbox3.addWidget(self.label10)

        self.label14 = QLabel("Output folder")
        self.label14.setStyleSheet("background-color:white;")
        self.label14.setFont(QFont("times new roman", 16))
        self.label14.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label14.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.label14)

        self.line_edit5 = QLineEdit()
        self.line_edit5.setStyleSheet("background-color:white;")
        self.line_edit5.setFont(QFont("times new roman", 16))
        self.line_edit5.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.line_edit5.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.line_edit5)

        btn4 = QPushButton("Browse")
        btn4.setStyleSheet("background-color:magenta; color: white;")
        btn4.setFont(QFont("times new roman", 14))
        btn4.setFixedHeight(36)
        btn4.setFixedWidth(72)
        btn4.clicked.connect(self.open3)
        vbox3.addWidget(btn4)

        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox3)

        vbox.addLayout(hbox)

        btn_create = QPushButton("Create")
        btn_create.setStyleSheet("background-color:blue; color: white;")
        btn_create.setFont(QFont("times new roman", 16))
        btn_create.setFixedHeight(44)
        btn_create.clicked.connect(self.create_submit)
        vbox.addWidget(btn_create)

        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()
        vbox6 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        vbox7 = QVBoxLayout()

        self.label = QLabel("Video Domainer Site Builder Tool")
        self.label.setStyleSheet("background-color:purple; color: white;")
        self.label.setFont(QFont("times new roman", 36))
        self.label.setFixedHeight(72)
        #self.label.setFixedWidth(600)
        self.label.setAlignment(Qt.AlignCenter)
        vbox7.addWidget(self.label)

        self.label11 = QLabel("Primary Ad")
        self.label11.setStyleSheet("background-color:white;")
        self.label11.setFont(QFont("times new roman", 16))
        self.label11.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label11.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label11)

        self.primary_ad_choice = QComboBox()
        self.primary_ad_choice.setStyleSheet("background-color:white;")
        self.primary_ad_choice.setFont(QFont("times new roman", 16))
        self.primary_ad_choice.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.primary_ad_choice.addItem("None")
        self.primary_ad_choice.addItem("Text Ad with button")
        self.primary_ad_choice.addItem("Ad unit or banner")
        self.primary_ad_choice.currentIndexChanged.connect(self.hovered4)
        vbox5.addWidget(self.primary_ad_choice)

        btn3 = QPushButton("Setup")
        btn3.setStyleSheet("background-color:brown; color: white;")
        btn3.setFont(QFont("times new roman", 14))
        btn3.setFixedHeight(36)
        btn3.setFixedWidth(72)
        btn3.clicked.connect(self.setup)
        vbox6.addWidget(btn3)

        self.label12 = QLabel("Amazon search buttons")
        self.label12.setStyleSheet("background-color:white;")
        self.label12.setFont(QFont("times new roman", 16))
        #self.label5.setFixedHeight()
        #self.label.setFixedWidth(600)
        self.label12.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label12)

        self.amazon_search = QTextEdit()
        self.amazon_search.setStyleSheet("background-color:white;")
        self.amazon_search.setFont(QFont("times new roman", 16))
        # self.text_edit.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.amazon_search.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.amazon_search)


        self.label15 = QLabel("Amazon affiliate ID")
        self.label15.setStyleSheet("background-color:white;")
        self.label15.setFont(QFont("times new roman", 16))
        self.label15.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label15.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label15)

        self.affiliate_id = QLineEdit()
        self.affiliate_id.setStyleSheet("background-color:white;")
        self.affiliate_id.setFont(QFont("times new roman", 16))
        self.affiliate_id.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.affiliate_id.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.affiliate_id)

        self.label16 = QLabel("Search domain")
        self.label16.setStyleSheet("background-color:white;")
        self.label16.setFont(QFont("times new roman", 16))
        self.label16.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label16.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label16)

        self.domain = QLineEdit()
        self.domain.setStyleSheet("background-color:white;")
        self.domain.setFont(QFont("times new roman", 16))
        self.domain.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.domain.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.domain)

        self.label17 = QLabel("Adsense ID")
        self.label17.setStyleSheet("background-color:white;")
        self.label17.setFont(QFont("times new roman", 16))
        self.label17.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label17.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label17)

        self.adsense = QLineEdit()
        self.adsense.setStyleSheet("background-color:white;")
        self.adsense.setFont(QFont("times new roman", 16))
        self.adsense.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.adsense.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.adsense)

        self.label13 = QLabel()
        self.label13.setFixedHeight(202)
        vbox6.addWidget(self.label13)

        btn5 = QPushButton("Paste")
        btn5.setStyleSheet("background-color:brown; color: white;")
        btn5.setFont(QFont("times new roman", 14))
        btn5.setFixedHeight(36)
        btn5.setFixedWidth(72)
        btn5.clicked.connect(self.paste1)
        vbox6.addWidget(btn5)

        btn6 = QPushButton("Paste")
        btn6.setStyleSheet("background-color:brown; color: white;")
        btn6.setFont(QFont("times new roman", 14))
        btn6.setFixedHeight(36)
        btn6.setFixedWidth(72)
        btn6.clicked.connect(self.paste2)
        vbox6.addWidget(btn6)

        self.label25 = QLabel()
        self.label25.setFixedHeight(158)
        vbox6.addWidget(self.label25)

        self.label18 = QLabel("Ad unit code")
        self.label18.setStyleSheet("background-color:white;")
        self.label18.setFont(QFont("times new roman", 16))
        #self.label5.setFixedHeight()
        #self.label.setFixedWidth(600)
        self.label18.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label18)

        self.ad_code = QTextEdit()
        self.ad_code.setStyleSheet("background-color:white;")
        self.ad_code.setFont(QFont("times new roman", 16))
        # self.text_edit.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.ad_code.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.ad_code)

        self.label19 = QLabel("Google Analytics ID")
        self.label19.setStyleSheet("background-color:white;")
        self.label19.setFont(QFont("times new roman", 16))
        self.label19.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label19.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label19)

        self.analytics_id = QLineEdit()
        self.analytics_id.setStyleSheet("background-color:white;")
        self.analytics_id.setFont(QFont("times new roman", 16))
        self.analytics_id.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.analytics_id.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.analytics_id)

        self.label20 = QLabel("Remote assets folder")
        self.label20.setStyleSheet("background-color:white;")
        self.label20.setFont(QFont("times new roman", 16))
        self.label20.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.label20.setAlignment(Qt.AlignCenter)
        vbox4.addWidget(self.label20)

        self.remote_assets = QLineEdit()
        self.remote_assets.setStyleSheet("background-color:white;")
        self.remote_assets.setFont(QFont("times new roman", 16))
        self.remote_assets.setFixedHeight(36)
        #self.label.setFixedWidth(600)
        self.remote_assets.setAlignment(Qt.AlignCenter)
        vbox5.addWidget(self.remote_assets)


        hbox2.addLayout(vbox4)
        hbox2.addLayout(vbox5)
        hbox2.addLayout(vbox6)

        vbox7.addLayout(hbox2)


        btn_create2 = QPushButton("Create")
        btn_create2.setStyleSheet("background-color:yellow; color: black;")
        btn_create2.setFont(QFont("times new roman", 16))
        btn_create2.setFixedHeight(44)
        btn_create2.clicked.connect(self.create_submit)
        vbox7.addWidget(btn_create2)

        self.tab1 = QWidget()
        self.tab1.setLayout(vbox)

        self.tab2 = QWidget()
        self.tab2.setLayout(vbox7)

        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab1, 'Videos')
        self.tabs1.addTab(self.tab2, 'Ads')

        vbox4 = QVBoxLayout()

        vbox4.addWidget(self.tabs1)

        self.setLayout(vbox4)

        self.show()


    def open1(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        print(path[0])
        self.line_edit1.setPlaceholderText(path[0])
        self.source_articles_folder = path[0]
        return path[0]

    def open2(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        print(path[0])
        self.line_edit2.setPlaceholderText(path[0])
        self.templates_folder = path[0]
        return path[0]

    def open3(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        print(path[0])
        self.line_edit5.setPlaceholderText(path[0])
        self.output_folder = path[0]
        return path[0]

    def hovered(self):
        text = self.site_type.currentText()
        self.type_of_site = text

    def hovered2(self):
        text = self.video_source.currentText()
        if text == 'The Video List (the same videos that were used last time)':
            self.label8.setDisabled(True)
            self.label9.setDisabled(True)
            self.youtube_feed.setDisabled(True)
            self.line_edit4.setDisabled(True)
        else:
            self.label8.setEnabled(True)
            self.label9.setEnabled(True)
            self.youtube_feed.setEnabled(True)
            self.line_edit4.setEnabled(True)

        if text == 'The Video List PLUS additional videos from Youtube':
            self.check1.setEnabled(True)
        else:
            self.check1.setDisabled(True)

        self.source_of_videos = text

    def hovered3(self):
        text = self.youtube_feed.currentText()
        self.youtube_feed_to_use = text

    def hovered4(self):
        text = self.primary_ad_choice.currentText()
        self.primary_ad = text

    def setup(self):
        # A New Dialog box window opens up
        if self.primary_ad_choice.currentText().strip() == 'None':
            self.warning_message()
        elif self.primary_ad_choice.currentText().strip() == 'Text Ad with button':
            self.setup2()
        elif self.primary_ad_choice.currentText().strip() == 'Ad unit or banner':
            self.setup3()


    def warning_message(self):
        QMessageBox.warning(self, "Video Domainer Site Builder Tool", "Please choose a primary ad type before clicking this button")


    def setup2(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:white")
        settings_dialog.setWindowTitle("Primary Ad - Text Ad with Button")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 175, 700, 200)

        vbox11 = QVBoxLayout()
        vbox12 = QVBoxLayout()
        hbox11 = QHBoxLayout()

        self.label201 = QLabel("Ad Title")
        self.label201.setStyleSheet("background-color:white;")
        self.label201.setFont(QFont("times new roman", 16))
        self.label201.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label201.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label201)

        self.ad_title = QLineEdit()
        self.ad_title.setStyleSheet("background-color:white;")
        self.ad_title.setFont(QFont("times new roman", 16))
        self.ad_title.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.ad_title.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.ad_title)

        self.label51 = QLabel("Ad Text")
        self.label51.setStyleSheet("background-color:white;")
        self.label51.setFont(QFont("times new roman", 16))
        self.label51.setFixedHeight(144)
        # self.label.setFixedWidth(600)
        self.label51.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label51)

        self.text_edit11 = QTextEdit()
        self.text_edit11.setStyleSheet("background-color:white;")
        self.text_edit11.setFont(QFont("times new roman", 16))
        self.text_edit11.setFixedHeight(144)
        # self.label.setFixedWidth(600)
        self.text_edit11.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.text_edit11)

        self.label202 = QLabel("Button Text")
        self.label202.setStyleSheet("background-color:white;")
        self.label202.setFont(QFont("times new roman", 16))
        self.label202.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label202.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label202)

        self.button_text = QLineEdit()
        self.button_text.setStyleSheet("background-color:white;")
        self.button_text.setFont(QFont("times new roman", 16))
        self.button_text.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.button_text.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.button_text)

        self.label203 = QLabel("Button Link")
        self.label203.setStyleSheet("background-color:white;")
        self.label203.setFont(QFont("times new roman", 16))
        self.label203.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label203.setAlignment(Qt.AlignCenter)
        vbox11.addWidget(self.label203)

        self.button_link = QLineEdit()
        self.button_link.setStyleSheet("background-color:white;")
        self.button_link.setFont(QFont("times new roman", 16))
        self.button_link.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.button_link.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.button_link)

        hbox11.addLayout(vbox11)
        hbox11.addLayout(vbox12)

        btn_submit = QPushButton('Submit')
        btn_submit.setStyleSheet("background-color:yellow; color: black;")
        btn_submit.setFont(QFont("times new roman", 16))
        btn_submit.setFixedHeight(44)
        btn_submit.clicked.connect(self.submit_setup2)

        vbox_master = QVBoxLayout()
        vbox_master.addLayout(hbox11)
        vbox_master.addWidget(btn_submit)

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def setup3(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        # settings_dialog.setStyleSheet("background-color:white")
        settings_dialog.setWindowTitle("Primary Ad - Ad Unit Or Banner")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)

        vbox12 = QVBoxLayout()

        self.label52 = QLabel("Paste the code for the Ad Unit or Banner into the box")
        #self.label52.setStyleSheet("background-color:white;")
        self.label52.setFont(QFont("times new roman", 16))
        self.label52.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label52.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.label52)

        self.text_edit12 = QTextEdit()
        self.text_edit12.setStyleSheet("background-color:white;")
        self.text_edit12.setFont(QFont("times new roman", 16))
        self.text_edit12.setFixedHeight(144)
        # self.label.setFixedWidth(600)
        self.text_edit12.setAlignment(Qt.AlignCenter)
        vbox12.addWidget(self.text_edit12)

        hbox55 = QHBoxLayout()

        btn_paste = QPushButton('Paste')
        btn_paste.setStyleSheet("background-color:orange; color: black;")
        btn_paste.setFont(QFont("times new roman", 16))
        btn_paste.setFixedHeight(44)
        btn_paste.clicked.connect(self.paste3)
        hbox55.addWidget(btn_paste)

        btn_ok = QPushButton('OK')
        btn_ok.setStyleSheet("background-color:green; color: black;")
        btn_ok.setFont(QFont("times new roman", 16))
        btn_ok.setFixedHeight(44)
        btn_ok.clicked.connect(self.submit_setup3)
        hbox55.addWidget(btn_ok)

        btn_cancel = QPushButton('Cancel')
        btn_cancel.setStyleSheet("background-color:red; color: black;")
        btn_cancel.setFont(QFont("times new roman", 16))
        btn_cancel.setFixedHeight(44)
        btn_cancel.clicked.connect(lambda: settings_dialog.close())
        hbox55.addWidget(btn_cancel)

        vbox12.addLayout(hbox55)

        settings_dialog.setLayout(vbox12)
        settings_dialog.exec_()

    def submit_setup2(self):
        pass

    def submit_setup3(self):
        pass

    def paste1(self):
        self.adsense.setPlaceholderText(pyperclip.paste())
        self.adsense_id = pyperclip.paste()

    def paste2(self):
        self.ad_code.setPlaceholderText(pyperclip.paste())
        self.ad_unit_code = pyperclip.paste()

    def paste3(self):
        self.text_edit12.setPlaceholderText(pyperclip.paste())
        self.ad_unit_banner = pyperclip.paste()

    def item_selected(self):
        value = ""

        if self.check1.isChecked():
            self.front = True
        else:
            self.front = False

        self.label.setText(value)
    def create_submit(self):
        self.youtube_keywords = self.text_edit.toPlainText().lstrip().rstrip()
        self.site_name = self.line_edit3.text().lstrip().rstrip()
        self.number_of_video_pages = self.line_edit4.text().lstrip().rstrip()
        self.amazon_search_buttons = self.amazon_search.toPlainText().lstrip().rstrip()
        if len(self.output_folder) < 5:
            self.output_folder = self.line_edit5.text().lstrip().rstrip()
            if len(self.output_folder) < 5:
                self.output_folder = os.getcwd()

        self.amazon_affiliate_id = self.affiliate_id.text().rstrip().lstrip()
        if len(self.adsense_id) <= 1:
            self.adsense_id = self.adsense.text().lstrip().rstrip()
        self.search_domain = self.domain.text().lstrip().rstrip()
        self.google_analytics_id = self.analytics_id.text().lstrip().rstrip()
        if len(self.ad_unit_code) <= 1:
            self.ad_unit_code = self.ad_code.toPlainText().lstrip().rstrip()
        self.remote_assets_folder = self.remote_assets.text().lstrip().rstrip()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
