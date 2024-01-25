import os
os.system("pip install feedparser")
os.system("pip install pytube")
os.system("pip install pyperclip")
os.system("pip install pyqt5")


import feedparser
import datetime
import random
from zipfile import ZipFile
from pytube import YouTube
from pytube.contrib.search import Search
import shutil

import pyperclip
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QInputDialog, QGridLayout, QMessageBox,  QTabWidget, QCheckBox, QLCDNumber,QListWidget, QListWidgetItem, QLabel, QWidget, QPushButton,QComboBox, QFileDialog,QLineEdit, QTextEdit
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer, Qt
import time

article = False

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
        self.link_prefix = 'https://www.youtube.com/watch?v='
        self.set_domain_for_sale = False
        self.domain_for_sale = ' '

        self.youtube_keywords = "hello 1"
        self.site_name = 'hello 2'
        self.number_of_video_pages = 'hello 3'
        self.amazon_search_buttons = 'hello 4'
        self.output_folder = 'hello 5'
        self.amazon_affiliate_id = '1212120fe-20'
        self.adsense_id = 'pub-6845153524189'
        self.search_domain = 'https://www.google.com'
        #TEMPLATE 'https://www.google.com/search?q={}&sxsrf=ALiCzsa54iXPqaDEDOTGpClCrzR0qRwXFg%3A1659162583785&source=hp&ei=18_kYuGOLc7TkgXZhoOgAg&iflsig=AJiK0e8AAAAAYuTd53S9WhUDjg2dvwsBmFRZ5hPRaXm-&ved=0ahUKEwih1raj_p_5AhXOqaQKHVnDACQQ4dUDCAc&uact=5&oq={}&gs_lcp=Cgdnd3Mtd2l6EAMyCgguEMcBENEDECcyBAgjECcyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIFCAAQgAQyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDAToHCCMQ6gIQJzoNCC4QxwEQ0QMQ6gIQJzoFCAAQkQI6EQguELEDEIMBEMcBENEDEJECOhAILhCxAxCDARDHARDRAxBDOgQIABBDOggIABCxAxCDAToECAAQAzoKCAAQsQMQgwEQQzoKCC4QxwEQ0QMQQzoICAAQgAQQsQNQng5Y8hRg4BdoAXAAeACAAf8BiAH0CpIBAzItNpgBAKABAbABCg&sclient=gws-wiz'
        self.google_analytics_id = 'UA-309309309-1'
        self.ad_unit_code = 'hello 10'
        self.remote_assets_folder = 'hello 11'
        self.ad_unit_banner = 'Q N Software Services +923335212460 qnsoftwareservices12272@gmail.com'
        self.ad_title_value = 'dtrgyuhijo'
        self.ad_text = 'cfgvhjb'
        self.button_text_value = 'hjbkn'
        self.button_link_value = 'ytfughjnk'
        self.ad_unit_banner = 'tyfgvbhjkn'
        self.ad_unit_code = 'fyughijkl'
        self.article_text = ' '
        self.analytics_script = " "
        self.adsense_script = " "

        self.label = QLabel("Video Domainer")
        self.label.setStyleSheet("background-color:cyan; color: black;")
        self.label.setFont(QFont("times new roman", 36))
        self.label.setFixedHeight(72)
        #self.label.setFixedWidth(600)
        self.label.setAlignment(Qt.AlignCenter)


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
        # self.site_type.addItem("Offline Site")
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

        self.check2 = QCheckBox("Add Domain for sale Banner")
        self.check2.setIconSize(QSize(50, 50))
        self.check2.setFont(QFont("times new roman", 12))
        self.check2.toggled.connect(self.item_selected2)
        vbox2.addWidget(self.check2)

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


        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()
        vbox6 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        vbox7 = QVBoxLayout()

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

        vbox0 = QVBoxLayout()

        self.list = QListWidget()


        self.mytext = '''Video Firestorm Gold


From webmoneytools.com









--------------------------------------------------------------------------------


Site Builder Tool



 






Selling Websites Created By This Software

You can use this software to create complete websites. You can then sell the websites on sites like flippa.com. When selling a site, the site must be for a single niche - and must already be hosted with its own domain name.

You are not permitted to use the software to create a package of web pages that people can install on their own websites. In other words, you cannot sell (or give away) any web pages generated by this software, except as part of a complete, hosted website.






Setting Up Your Templates 

In order to use this software, you need to use the Standard Templates Zip, which contains the standard set of templates.

If you haven't already downloaded the Standard Templates Zip, you can download it here (please make sure you are connected to the Internet before using this link).

Unzip these standard templates into a folder on your PC.

If you are only planning to create simple video sites (not offline sites, squeeze sites or sales sites) then you do not need to modify the templates (unless you want to). 

For details of how to edit the templates, see the "Editing The Templates" section below.





Setting Up Your Articles

In order to provide unique, niche-targeted content on each video page (for SEO), the software requires a set of suitable text articles.

A set of off-the-shelf Private Label Rights (PLR) articles is OK for this purpose. The software will randomly extract snippets from the articles, so the content will be unique, even if the original articles are not. The resulting text will not make sense to a visitor - but visitors will rarely look at the text, since they will only be interested in the videos. The text will however provide content for search engines. 

All your article text files should be in a single folder on your PC. 





The Video List 

The first time you build a new site, it's built using the current video feed data taken from YouTube. The software will then save a "Video List", which is a list of all the videos used to build the site. This "Video List" is saved in the same folder as the text articles. 

Once you have built a site, you can rebuild it at any time in the future, to change ads etc. - or to add more videos. You can rebuild the site using the current video feed data taken from YouTube. But if you rebuild the site on a different day to last time (or even later on the same day), the YouTube video feed data may have changed. This means you would get different videos - and different web pages with different names. This is generally not a good idea if you have already uploaded your website and had it indexed by search engines.

To avoid this problem, you can rebuild your site using the Video List. This will rebuild the site with exactly the same videos as last time, so that all the pages will have the same names and show the same videos. 

You can also add additional videos on top of the Video List. This is a good way to expand a site - so for example, you could add new videos every month. When you do this, the site will keep all the existing videos with the same web page names - and add additional pages on top. The Video List is updated with any new videos added to the site.

Any additional video pages are usually added at the front of the site (so they appear on the home page of the site), pushing the existing videos back. You can however add them at the back of the site instead, if you prefer. 

The software will never include any video more than once - so if it is already in the Video List, it will not be added again. Note however that some people upload the same video (or very similar videos) to YouTube more than once. In this case, each video would have a different YouTube video ID (and a different page on YouTube.com) - and the software will include all of them. 




Using Multiple Keywords 

YouTube will only return a maximum of 1000 videos for any keyword (and often doesn't even return that many). But you can use multiple (related) keywords to build larger sites.

All the videos will use the same text articles, so all keywords used should be related to the same general topic. 

You can enter as many keywords as you want - enter the keywords into the Site Builder Tool with one keyword per line. 

The software will never include any video more than once - so if it is already in the Video List, it will not be added again.




Ads On Videos  

A lot of YouTube videos now show Google ads on the video itself. There are "intro" ads and Adsense ads.

The intro ads are not currently shown on "embedded" videos (they only appear on YouTube.com), so they will not appear on your websites. 

The Adsense ads will appear on your websites. These Adsense ads pay the person who created the video (they do NOT pay you). There is no way to avoid these ads (they provide an incentive for people to create videos). But your website has your own ads at the side and below of the video - so someone responding to an ad is much more likely to respond to your ads than to the single Adsense ad on the video itself.







Using The Site Builder Tool

To use the Site Builder software, click the button above then enter your details into the boxes as follows:

Source Articles Folder
Click the Browse button and select any one of the article text files. All text files in the same folder will be used to build the site.



Template Folder
Click the Browse button and select the VideoPageTemplate.html file (which is one of the files in the template package). The software will assume that the other template files are in the same folder.

Site Name
Enter the name for your website. This will be used as the title shown at the top of each web page.


Type Of Site
You can build different types of sites - which differ in their home page. A simple video site has the first page of videos as the home page. Other types of sites have an extra page as the home page, such as a squeeze page or a sales page. This home page then links to the first page of videos. For full details, see the "Editing The Templates" section below. 



YouTube Keywords
This is the keyword (or search term) used to find videos on YouTube. For example if you are building a site about koi fish, you should use articles about koi fish and enter the YouTube keyword as "koi fish". You can enter more than one keyword, with each keyword on a separate line. 


Video Source
The first time you build a site, this should be set to "The current YouTube video feed". The tool will then get the latest videos from YouTube to build the site. Once you have built a site, you can rebuild it using the "Video List". You can also add additional videos on top of the Video List. See the section above on the "Video List" for more details. 



YouTube Feed To Use
Most people just leave this set to "Most relevant videos first - then the other feeds". 

YouTube provides 3 feeds for any particular keyword - the most popular videos that match the keyword, the most recent videos that match the keyword and the most relevant videos for that keyword. The 3 feeds contain different videos - although many videos do appear in more than one feed. 

The feeds are not perfect - in particular the most recent feed does not always have all the videos in the correct order. Also some of the videos, especially those towards the end of the feeds, may not be very relevant to the keyword. 

When building a site, the feed determines what videos are selected - and in what order they appear on the site. 

In addition to selecting which feed to use, you can also choose whether to use the other two feeds as well. This only matters if you want to add hundreds of videos in one go. All 3 feeds notionally contain 1000 videos - but in practice they typically contain more like 500 unique videos (the feeds contain lots of duplicates). If you want to build a site with more than the number of videos available in one feed, the software can scan the other two feeds as well - and add any extra videos found, to maximize the number of videos added.  


Number Of Video Pages / Additional Video Pages
If the Video Source is set to "The current YouTube video feed", this is the number of video pages that you want. The maximum is 1000 videos (which is the maximum number available in the feed at any one time). However the feeds usually contain less than 1000 videos. If you set the value to 1000 or more, the software will get as many videos as it can. 

If the Video Source is set to "The Video List Plus Additional Videos", this is the number of additional videos to be added (on top of those already in the Video List). The maximum is 1000 - but the feeds often contain less than 1000. If you set the value to 1000, the software will get as many videos as it can. You can also choose whether to insert the new videos at the front of the site (so they appear on the home page, pushing the existing videos back) - or at the back of the site (after all the existing videos). 


Primary Ad
The Primary Ad is the ad shown next to every video. It is the most important ad on the site. There are three options for the Primary Ad. You can edit the templates to include your ad, which allows you to see exactly what the ad looks like as you type it in. See the Editing The Templates section below for details. For this option, you do not want to use the Site Builder to set up an ad, so just set the Primary Ad option to "None". 

If you don't want to modify the templates, you can easily set up a text ad with a button, as your Primary Ad. Select the "Text ad with button" option, then click the Setup button to enter the ad title, ad text, text to be shown on the button and the link for the button. 

Alternatively, you can have an ad unit or banner (such as an Amazon banner). Select the "Ad unit or banner" option, then click the Setup button and paste the code for the ad unit or banner. Make sure the ad unit or banner is a suitable size - a unit of 300 pixels or less in width and height is generally best. 


Amazon Search Buttons
The standard templates have four buttons under the video, which can be used for searches on Amazon.com using your affiliate ID. You can enter up to four search terms. If you enter less than four, unused buttons are removed. If you do not enter anything, then all the buttons are removed. For example, typical search terms for a koi fish site, might be "Koi Fish Books", "Fish Food", "Pond Pumps". If a visitor clicks on the "Fish Food" button, a new browser window would open showing an Amazon.com search for "Fish Food", with your affiliate ID. If the visitor then orders anything from Amazon within the next 24 hours, you would earn a commission. 


Amazon Affiliate ID
If you use the Amazon Search Buttons feature, enter your Amazon affiliate ID into the box.


Search Domain
The standard templates have a search box at the bottom of every web page. When a visitor uses the search feature, it does a Google search of a particular website. You can either search the video site itself, or search YouTube.com. To search the video site, enter the relevant domain name into the Search Domain box. Note that only pages that google currently indexes will be searchable. Alternatively enter "youtube.com" into the Search Domain box, to search YouTube.com. Or you can leave the Search Domain box blank and the search boxes will not appear on your website. 


Adsense ID
This is only used if you have entered a domain name into the Search Domain box. It adds your Adsense ID to the Google searches, so you will get credited for any clicks on the ads shown on google.com. If you have an Adsense account, but don't know how to get your Adsense ID, see the section below. 


Ad Unit Code
The standard templates have an optional ad unit underneath the Amazon search buttons. This can be used for an ad unit from any source, such as the Amazon affiliate program. Ideally the ad unit should be "mobile friendly". Just paste the ad unit code into the box using the Paste button. You can use an Adsense ad unit - but since the primary content of these sites is a video created by someone else, it may not be considered an appropriate use of Adsense (the criteria for including Adsense ads on a web page are generally more stringent than for Adsense search).


Google Analytics ID (optional)
If you want to use the Google Analytics service to track the visitors to your site, enter your "UA number" into the box. For more details, see the Google Analytics section below.


Remote Assets Folder
Most people leave this blank. If you do not understand the following information, just ignore it and leave the box blank. The standard templates have an "assets" folder, which contains all the extra files for the sites (about 2.5 Megabytes of files). Unless you change the templates, the contents of the assets folder are the same for every video site. To avoid uploading multiple copies of the assets folder, you can upload it once and then enter the web address of the folder into the Remote Assets Folder box. Your video site will then use this (already uploaded) assets folder, instead of having its own assets folder.


Output Folder
Your "Output Folder" is the folder on your PC where the software puts the generated website files, ready to be uploaded to your web host. You should create a suitable folder on your PC then click the Browse button and select this folder.


Create Button
When you have filled in the boxes, click the Create button and the software will then generate all the files for your new website.

You should then upload all the files to your web host using the Website Uploader Tool below (or using any other FTP software).

The software will store a special file named VideoSiteBuilderSettings.dat in the folder containing the original article text files. This special file holds all the settings you used for the Site Builder Tool. If you need to re-build that website again in the future, just select the Source Articles folder as normal and the tool will then ask whether it should load the settings it used last time. This solution makes it easy to rebuild any of your sites in the future, without you needing to enter all the settings for that site again.









Getting Your Adsense ID

Here's the easiest way to get your Adsense ID... 

In your Adsense account on Google.com, go to the Products section (in Adsense Setup) and select Adsense For Content. Now create an ad unit. Pick any format and colors (they are not relevant for this purpose). 

Your Adsense code will then be shown in the Your AdSense code box at the bottom of the page. Click in the box and copy the contents to your Windows clipboard (right click and select Copy). 

Now go to the Site Builder Tool and click the Paste button next to the Adsense ID box. The tool will automatically extract your Adsense ID from the Adsense code and display it in the box. The tool will automatically remember your ID so you should only need to go through this process once.








Google Analytics 

Google Analytics is a free service from Google that allows you to track the visitors to your websites. You can create a free Analytics account at http://www.google.com/analytics/ 

Once you have an account, click on the "Create New Website Profile" link and enter the domain name of your website. 

The website will then appear in the Website Profiles table. 

You can do the same thing repeatedly to add as many websites as you want. 

In the Website Profiles table, a UA number will be shown next to each domain name. 

Your UA numbers should look something like this: UA-1234567-12
Your UA numbers will start with "UA-" but will have different digits.

Note that Google sometimes refer to a UA number as a "Web Property ID" - but most people call them UA numbers (for obvious reasons).

Just paste the UA number into the box on the Site Builder Tool.

That's all you need to do. The tol will automatically insert the Google Analytics code into your web pages.

To view your stats, just visit your Google Analytics account at any time in the future. The stats for each domain name will be shown in the Website Profiles table, next to the domain name. Click on the relevant "view report" link for more detailed stats.

Note that stats are collated at the end of each day, so stats for today will not appear in your Google Analytics account until the following day.












Editing The Templates

Ignore this section unless you want to modify the templates.

You can modify the templates using the free MobiRise editor available here. 

MobiRise is free - but there are options to pay to add some extra features. The templates were created using the free version of MobiRise, so you do NOT need any of the paid features in order to edit the templates.

After you have installed MobiRise, you can just double-click on the "project.mobirise" file in the templates folder, in order to edit the templates. 

You can edit the templates however you want, to change colors, fonts, layout, etc.

Some of the "blocks" on the page are automatically replaced with the YouTube videos. These should be pretty obvious. You can move these blocks around and change them as required. You can change most things - even changing the number of video images on each page, by changing the blocks. If you are unsure whether something will work, just give it a try. 

You can also use MobiRise to edit the Primary Ad on VideoPageTemplate.html, if you wish, as an alternative to using the Primary Ad options on the software. 


The software can build four different "types of sites": simple videos sites, offline sites, squeeze sites and sales sites. For simple video sites and sales sites, you do not need to modify templates (unless you want to). 

A "simple video site" just has pages of videos. The home page is the first page of videos. 

An "offline site" is a site for an offline business, such as a plumber. The site will have a home page giving contact details etc for the business. You need to use MobiRise to edit the OfflineHomePageTemplate.html page, which will become the home page for the site. You should also edit the primary ad on VideoPageTemplate.html, with a suitable ad promoting the business - with the button under the ad linking to the home page - the easiest way is to just enter "." (just a single dot) as the link. 

A "squeeze site" is a site for building a list. The site will have a home page offering a free gift (or free membership) in exchange for subscribing to your newsletter. You need to use MobiRise to edit the SqueezeHomePageTemplate.html page, which will become the home page for the site. You should also edit the primary ad on VideoPageTemplate.html, with a suitable ad promoting the free offer - with the button under the ad linking to the home page - the easiest way is to just enter "." (just a single dot) as the link. 

A "sales site" is an existing site that sells things, which you want to supplement with some secondary pages of video content for SEO or other purposes. In this case, you do not need to use MobiRise (unless you want to). Ideally you should edit your sales site to include a link to "videopage1.html" (which is the first video index page) somewhere on the site, so search engines can find the video pages. You should use the Primary Ad on the video pages to promote your sales pages. 

When you have finished editing the templates, click the "Publish" button (top right of the MobiRise screen) and select "Local Drive Folder" and make sure the box is showing the location of your templates folder. After publishing, you can use the Site Builder Tool. 



 





--------------------------------------------------------------------------------










Video List Editor Tool





 





Instructions For Use

See the "Video List" section above for details of the Video List.

This editor tool allows you to edit a Video List. You can manually add videos, delete any unwanted videos, modify video titles and move videos within the list. 

To use the tool, click the button above and select any one of the article text files for the video site. The Video List file is stored in the same folder as the article text files. If there is no Video List file present in the folder, the tool will create a new Video List. 

The tool will load the first video, showing it's screenshot and title. Use the arrow buttons at the top of the tool to move backwards and forwards through the list. 



Search Button 

You can use the Search button to find a particular video. 

You can enter the "Video Number", which is 1 for the first video, 2 for the second video, 3 for the third video, etc. 

Or you can enter the Video ID - the strange-looking string which uniquely identifies the video on YouTube.com. 

Or you can enter a Video Title. For video titles, you can enter any text and the tool will find the first video that contains that text somewhere in its title. Once you have entered a title string, an asterisk button will appear next to the Search button, which searches again for the same text, starting at the current position.



Inserting, Deleting and Changing Video Details 

You can edit the title of any video - or paste in a new title. 

You can also paste in a new video ID (replacing the existing video), if you wish. To do this, go to YouTube.com and find a suitable video, then copy the web address of the video's page to your Windows Clipboard. Now click the Paste button next to the Video ID box and the tool will automatically extract the video ID from the web address. The tool will also attempt to get the video title from YouTube.com. 

Each video has an associated checkbox: Keep this video in its current position when adding new videos to the site. If you add new videos to the front of the site using the Site Builder Tool, the new videos will be added AFTER any video that has this checkbox checked. For example, if videos 3, 7 and 12 have the checkbox checked, any new videos would be added after video 12. This feature is used in conjunction with the Moving Videos feature (see below). 

You can use the Delete button to delete the current video. The video is permanently deleted from the list - so even if you add new videos to the site in the future, that video will never appear again. 

You can use the Insert button to insert a new video into the list. The video is inserted after the current video. The inserted video is initially blank, so you need to paste in a video ID (see above for details). 



Moving Videos 

You can move the position of any video in the list. This feature is usually used to move particularly good videos to the front of the list, so they appear on your site home page. However you can move any video to any position. 

To move a video, just enter its new position in the "Move to position" box. For example, if you want the video to become the first video, enter "1". 

The videos are not actually moved until you click the "Do all moves" button. So you can go through and set all the positions you want on all the videos, then click "Do all moves" and the video list will be instantly re-ordered. 

When a video is moved, the Keep this video in its current position when adding new videos to the site checkbox is automatically checked for that video. This ensures that the video stays where you put it, even if you add new videos to the site in future using the Site Builder Tool. 



Save Button 

When you have finished editing the Video List, click the Save button to save your changes. You can then rebuild the site using the Site Builder Tool. 



 



--------------------------------------------------------------------------------







Website Uploader Tool 


You can use any FTP program to upload your website to your web host after using the Site Builder Tool, but this upload tool offers a very easy solution. 


 




Click the Browse button and select any one of the files in the folder containing the generated site files. The tool will upload everything in the same folder.

If you want to upload the site to a folder on your website, enter the name of the folder into the Folder On Web box (leave the box blank otherwise). The folder will be created if it does not already exist.

Click the FTP Setup button and enter your FTP details (domain name and your web host user name and password). These details will be remembered so it's even quicker to upload additional sites in future.

Then just click the Upload button and the whole site will be uploaded.




Notes On Entering Your FTP Details

The first time you use the tool, you need to enter the FTP details for your website. Click the FTP Setup button to enter these details.

You will need to know the user name and password for your web host. Your web hosting company should have provided these.

The tool automatically works out some of your web host settings, so it's easier to set up than normal FTP programs.

Please note that to use this software, you must have your domain name set up and working. This means that if you enter your web address (such as www.mysite.com) into your Internet browser, the browser must be able to find the site (even if it just displays a blank page). If your site is brand new, it may take a few hours before your domain name is fully set up and your browser can see it.

 



--------------------------------------------------------------------------------


Version History 


This software will occasionally connect to the Internet (when it is able to) and automatically check for new versions. All new versions can be downloaded automatically at no extra cost.

Version 2.1 - First release of this completely new version 2 of the software

--------------------------------------------------------------------------------
 

This software is for your personal use only and must not be distributed


Software Version 2.1
 
'''

        self.sampletext = self.mytext.split('\n')

        for i, line in enumerate(self.sampletext):
            if len(line.strip()) <= 1:
                self.sampletext.pop(i)

        for i, line in enumerate(self.sampletext):
            if i != 0:
                if len(self.sampletext[i].strip()) <= 25:
                    a = QListWidgetItem()
                    # a.setTextAlignment(Qt.AlignCenter)
                    a.setFont(QFont('times new roman', 16, QFont.Bold))
                    a.setText(line)
                else:
                    a = QListWidgetItem()
                    a.setFont(QFont('times new roman', 12, QFont.Normal))
                    a.setText(line)

            else:
                a = QListWidgetItem()
                a.setFont(QFont('times new roman', 12, QFont.Normal))
                a.setText(line)
            self.list.insertItem(i, a)


        vbox0.addWidget(self.list)

        self.tab0 = QWidget()
        self.tab0.setLayout(vbox0)

        self.tab1 = QWidget()
        hb1212 = QHBoxLayout()
        hb1212.addLayout(vbox)
        hb1212.addLayout(vbox7)
        vb1212 = QVBoxLayout()
        vb1212.addWidget(self.label)
        vb1212.addLayout(hb1212)
        vb1212.addWidget(btn_create)

        self.tab1.setLayout(vb1212)


        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab0, 'Instructions')
        self.tabs1.addTab(self.tab1, 'Videos')

        vbox4 = QVBoxLayout()

        vbox4.addWidget(self.tabs1)

        self.setLayout(vbox4)

        self.show()

    def path12(self):
        global article
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')


        print(path[0])
        self.line_edit1.setPlaceholderText(path[0])
        self.source_articles_folder = path[0]
        article = True
        return path[0]

    def open1(self):
        global article
        message = QMessageBox.question(self, "SELECT ARTICLE SOURCE", "\tDO you want Article from text file\n\tPress YES for selecting a text file\n\tPress NO for an RSS feed and input the link to it", QMessageBox.Yes |QMessageBox.No)

        if message == QMessageBox.Yes:
            self.path12()
        elif message == QMessageBox.No:
            text, ok = QInputDialog.getText(self, 'RSS Feed Selector', 'Enter text:')
            if ok:
                article = False
                self.line_edit1.setPlaceholderText(text)

                url = text

                self.rss_feed = ''

                f = feedparser.parse(url)

                for i, entries in enumerate(f.entries):
                    self.rss_feed += '\t\t\t' + str(i + 1) + str(entries.title) + '\n'
                    self.rss_feed += str(entries.description) + '\n\n'

    def open2(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        print(path[0])
        self.line_edit2.setPlaceholderText(path[0])
        self.templates_folder = path[0]
        return path[0]

    def open3(self):
        # path = QFileDialog.getOpenFileName(self, 'Open a file', '',
        #                                    'All Files (*.*)')

        path = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print(path)
        output = path
        # x = output.split('/')
        # y = x.pop(-1)
        self.output_folder = path

        self.line_edit5.setPlaceholderText(output)
        return output

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
        btn_submit.pressed.connect(self.submit_setup2)
        btn_submit.released.connect(lambda: settings_dialog.close())

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
        btn_ok.pressed.connect(self.submit_setup3)
        btn_ok.released.connect(lambda: settings_dialog.close())
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
        self.ad_title_value = self.ad_title.text().lstrip().rstrip()
        self.ad_text = self.text_edit11.toPlainText().lstrip().rstrip()
        self.button_text_value = self.button_text.text().lstrip().rstrip()
        self.button_link_value = self.button_link.text().lstrip().rstrip()

    def submit_setup3(self):
        self.ad_unit_banner = self.text_edit12.toPlainText().lstrip().rstrip()

    def submit_setup4(self):
        self.domain_for_sale = self.text_edit122.toPlainText().lstrip().rstrip()

    def item_selected2(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        # settings_dialog.setStyleSheet("background-color:white")
        settings_dialog.setWindowTitle("Domain For Sale - Ad Unit Or Banner")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)

        vbox122 = QVBoxLayout()

        self.label512 = QLabel("Paste the code for the Ad Unit or Banner into the box")
        # self.label52.setStyleSheet("background-color:white;")
        self.label512.setFont(QFont("times new roman", 16))
        self.label512.setFixedHeight(36)
        # self.label.setFixedWidth(600)
        self.label512.setAlignment(Qt.AlignCenter)
        vbox122.addWidget(self.label512)

        self.text_edit122 = QTextEdit()
        self.text_edit122.setStyleSheet("background-color:white;")
        self.text_edit122.setFont(QFont("times new roman", 16))
        self.text_edit122.setFixedHeight(144)
        # self.label.setFixedWidth(600)
        self.text_edit122.setAlignment(Qt.AlignCenter)
        vbox122.addWidget(self.text_edit122)

        hbox512 = QHBoxLayout()

        btn_paste12 = QPushButton('Paste')
        btn_paste12.setStyleSheet("background-color:orange; color: black;")
        btn_paste12.setFont(QFont("times new roman", 16))
        btn_paste12.setFixedHeight(44)
        btn_paste12.clicked.connect(self.paste3)
        hbox512.addWidget(btn_paste12)

        btn_ok12 = QPushButton('OK')
        btn_ok12.setStyleSheet("background-color:green; color: black;")
        btn_ok12.setFont(QFont("times new roman", 16))
        btn_ok12.setFixedHeight(44)
        btn_ok12.pressed.connect(self.submit_setup4)
        btn_ok12.released.connect(lambda: settings_dialog.close())
        hbox512.addWidget(btn_ok12)

        btn_cancel12 = QPushButton('Cancel')
        btn_cancel12.setStyleSheet("background-color:red; color: black;")
        btn_cancel12.setFont(QFont("times new roman", 16))
        btn_cancel12.setFixedHeight(44)
        btn_cancel12.clicked.connect(lambda: settings_dialog.close())
        hbox512.addWidget(btn_cancel12)

        vbox122.addLayout(hbox512)

        settings_dialog.setLayout(vbox122)
        settings_dialog.exec_()

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
        print('step 1 good')
        year = datetime.datetime.now().year

        self.youtube_keywords = self.text_edit.toPlainText().lstrip().rstrip()
        print(1, self.youtube_keywords)
        self.site_name = self.line_edit3.text().lstrip().rstrip()
        print(2, self.site_name)
        self.number_of_video_pages = self.line_edit4.text().lstrip().rstrip()
        print(3, self.number_of_video_pages)
        if len(self.line_edit1.text()) > 2:
            self.source_articles_folder = self.line_edit1.text().lstrip().rstrip()
        self.amazon_search_buttons = self.amazon_search.toPlainText().lstrip().rstrip()
        self.amazon_keywords = self.amazon_search_buttons.split('\n')
        self.amazon_search_buttons = ''
        if len(self.amazon_keywords) >= 1:
            for term in self.amazon_keywords:
                self.amazon_search_buttons += '<a class="btn btn-primary" target="_blank" href="https://www.amazon.com/s?k={}&amp;crid=1TSAZQPMU2I25&amp;sprefix={}%252Caps%252C310&amp;ref=nb_sb_noss_1&_encoding=UTF8&tag={}&linkCode=ur2&linkId=c3b55db574885d2c6484c1d8a351a503&camp=1789&creative=9325">{}</a>'.format(term, term, self.amazon_affiliate_id, term)

        print(4, self.amazon_search_buttons)
        if len(self.output_folder) < 5:#
            self.output_folder = self.line_edit5.text().lstrip().rstrip()
            if len(self.output_folder) < 5:
                self.output_folder = os.getcwd()

        print(5, self.output_folder)

        self.amazon_affiliate_id = self.affiliate_id.text().rstrip().lstrip()
        print(6, self.amazon_affiliate_id)
        self.article_text = self.line_edit1.text()
        if len(self.adsense.text()) > 3:
            self.adsense_id = self.adsense.text().lstrip().rstrip()
            self.adsense_script = '''<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
                  <ins class="adsbygoogle" style="display:block" data-ad-client="ca-{}" data-ad-slot="4532301685" data-ad-format="auto"></ins>
                  <script>(adsbygoogle = window.adsbygoogle ||[]).push({});</script>'''.format(self.adsense_id, self.adsense_id)
        print(7, self.adsense_id)
        self.search_domain = self.domain.text().lstrip().rstrip()
        print(8, self.search_domain)
        if len(self.analytics_id.text()) > 3:
            self.google_analytics_id = self.analytics_id.text().lstrip().rstrip()
            self.analytics_script = '''<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '{}');
</script>'''.format(self.google_analytics_id, self.google_analytics_id)
        print(9, self.google_analytics_id)
        self.ad_unit_code = self.ad_code.toPlainText().lstrip().rstrip()
        print(10, self.ad_unit_code)
        self.remote_assets_folder = self.remote_assets.text().lstrip().rstrip()
        print(11, self.remote_assets_folder)
        try:
            if article:
                file = self.source_articles_folder
                print('article file', self.article_text, len(self.article_text))
                if len(file) > 2:
                    print('correct file')
                    try:
                        fhand = open(self.source_articles_folder.lstrip().rstrip(), 'r')
                        for line in fhand:
                            self.article_text += line
                    except:
                        print("Article not found")
                    print(self.article_text)

            else:
                self.article_text = self.rss_feed
        except:
            time.sleep(0.1)



        print('step 2 good')

        a = Search(self.youtube_keywords)
        a.results

        print('step 3 good')

        for c, i in enumerate(a.results):
            print(c, i.title, '\t\t', i.video_id)
        print('\n\n\n')

        try:

            while len(a.results) < int(self.number_of_video_pages):
                a.get_next_results()
        except:
            print('error')
        print('step 4 good')

        embed_link = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        html_template = '''<!DOCTYPE html>
        <html>
        <head>
          <!-- Site made with Mobirise Website Builder v3.12.1, https://mobirise.com -->
          <meta charset="UTF-8">
          
          {}
          {}
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="generator" content="Mobirise v3.12.1, mobirise.com">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="shortcut icon" href="assets/images/videoplaybutton-128x128.png" type="image/x-icon">
          <meta name="description" content="">
          <title>{}</title>
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic&amp;subset=latin">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,700">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i">
          <link rel="stylesheet" href="assets/bootstrap-material-design-font/css/material.css">
          <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
          <link rel="stylesheet" href="assets/et-line-font-plugin/style.css">
          <link rel="stylesheet" href="assets/tether/tether.min.css">
          <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
          <link rel="stylesheet" href="assets/socicon/css/styles.css">
          <link rel="stylesheet" href="assets/theme/css/style.css">
          <link rel="stylesheet" href="assets/mobirise-gallery/style.css">
          <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">



        </head>
        <body>
        <section class="mbr-section article" id="msg-box8-r" style="background-color: rgb(201, 76, 76); padding-top: 40px; padding-bottom: 40px;">


            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2 text-xs-center">
                        <h1 class="mbr-section-title display-2">{}</h1>


                    </div>
                </div>
            </div>

        </section>

        <section class="engine"><a rel="external" href="https://mobirise.com">Web Page Builder</a></section><section class="mbr-section mbr-section__container article" id="header3-s" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 0px;">
            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <h1 class="mbr-section-title display-2">{}</h1>
                        
                    </div>
                </div>
            </div>
        </section>
        
        <div>
        {}
        </div>

        <section class="mbr-section" id="msg-box4-q" style="background-color: rgb(255, 255, 255); padding-top: 40px; padding-bottom: 40px;">


            <div class="container">
                <div class="row">
                    <div class="mbr-table-md-up">

                      <div class="mbr-table-cell mbr-right-padding-md-up mbr-valign-top col-md-7 image-size" style="width: 70%;">
                          <div class="mbr-figure"><iframe class="mbr-embedded-video" src="https://www.youtube.com/embed/{}?rel=0&amp;amp;showinfo=0&amp;autoplay=0&amp;loop=0" width="1280" height="720" frameborder="0" allowfullscreen></iframe></div>
                      </div>




                      <div class="mbr-table-cell col-md-5 text-xs-center text-md-left content-size">
                          <h3 class="mbr-section-title display-2">{}</h3>
                          <div class="lead">

                            <p></p><p>{}</p><p></p>

                          </div>

                          <div><a class="btn btn-primary" href="{}" target="_blank">{}</a></div>
                      </div>

                    


                    </div>
                </div>
            </div>

        </section>
        
        
                    
        <section class="mbr-section mbr-section__container article" id="header3-4b" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 20px;">
            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <h3 class="mbr-section-title display-2">{}</h3>

                    </div>
                </div>
            </div>
            
        </section>
        
        <div class="container">
            <div style="width: 412px; float: right;">
            <form>
                        <div class="mb-3" style="object-position: right">
                          <label for="exampleFormControlInput1" class="form-label">Name</label>
                          <input type="text" class="form-control" id="exampleFormControlInput12" placeholder="John Martin">
                        </div>
                        <br>
                        <div class="mb-3" style="object-position: right">
                          <label for="exampleFormControlInput1" class="form-label">Email</label>
                          <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
                        </div>
                        <br>
                        <div class="mb-3" style="object-position: right">
                          <label for="exampleFormControlTextarea1" class="form-label">Details</label>
                          <textarea class="form-control" id="exampleFormControlTextarea1" rows="5"></textarea>
                        </div>
                    </form>
                    <br><br>
                    <form class="mbr-form" action="{}" targer="_blank" method="post">

                                <div class="mbr-subscribe mbr-subscribe-dark input-group">
                                    <input type="text" class="form-control" name="text12" required="" style="font-family: times new roman; font-size:22; color:black" data-form-field="Text" placeholder="Search Videos" >
                                    <span class="input-group-btn"><button type="submit" class="btn btn-success">Search</button></span>
                                </div>
                            </form>
            </div>
        </div>
        
        

        <section class="mbr-section article mbr-section__container" id="content1-t" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 20px;">

            <div class="container">
                <div class="row">
                    <div class="col-xs-12 lead">{}</div>
                </div>
            </div>

        </section>
        <section class="mbr-section mbr-section__container" id="buttons1-1w" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 20px;">
    
    <div class="row">
                    <div class="col-xs-12">
                        <div class="container"><h5><pre>{}</pre></h5></div>
                    </div>
                </div>
                <br>
                <br>
                
    <div class="container"> 
        <div class="row">
            <div class="col-xs-12">
                <div class="text-xs-center">{}</div>
            </div>
        </div>
    </div>

</section> 
<br>
        
            
        <div class="container">
            <table>
                <tr>  
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                </tr>
                <tr>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                </tr>
                <tr>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                    <td><div class="card" style="height:290px; width: 290px;">
                            <div class="card-image">
                            <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                            </div>
                            <div class="card-content">
                                <p><h6>{}</h6></p>
                            </div>
                            <div class="card-action">
                                <a href="{}"></a>
                            </div>
                        </div></td>
                </tr>
            </table>
        </div>
            

        <section class="mbr-section mbr-section__container" id="buttons1-35" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 20px;">

            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <div class="text-xs-center"><a class="btn btn-primary" href="{}">More Videos</a> </div>
                    </div>
                </div>
                
                
            </div>

        </section>
        
        <div class="Container">
            
        </div>
        
        <section class="mbr-section mbr-section__container article" id="header3-4b" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 20px;">
            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <h3 class="mbr-section-title display-2">{}</h3>

                    </div>
                </div>
            </div>
        </section>

        <section class="mbr-section article mbr-section__container" id="content1-t" style="background-color: rgb(255, 255, 255); padding-top: 20px; padding-bottom: 20px;">

            <div class="container">
                <div class="row">
                    <div class="col-xs-12 lead">{}</div>
                </div>
            </div>

        </section>
        
        
        
        
        

        <section class="mbr-section" id="form2-1f" style="background-color: rgb(50, 50, 50); padding-top: 0px; padding-bottom: 0px;">
                <div class="mbr-section mbr-section__container mbr-section__container--middle">
                <div class="container">
                    <div class="row">
                        <div class="col-xs-12 text-xs-center">


                        </div>
                    </div>
                </div>
            </div>
            <div class="mbr-section mbr-section-nopadding">
                <div class="container">
                    <div class="row">
                        <div class="col-xs-12 col-lg-10 col-lg-offset-1" data-form-type="formoid">

                            
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="mbr-section mbr-section-md-padding" id="social-buttons3-z" style="background-color: rgb(50, 50, 50); padding-top: 30px; padding-bottom: 0px;">

            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2 text-xs-center">
                        <h3 class="mbr-section-title display-2">Share This Page</h3>
                        <div>

                          <div class="mbr-social-likes" data-counters="false">
                            <span class="btn btn-social facebook" title="Share link on Facebook">
                                <i class="socicon socicon-facebook"></i>
                            </span>
                            <span class="btn btn-social twitter" title="Share link on Twitter">
                                <i class="socicon socicon-twitter"></i>
                            </span>
                            <span class="btn btn-social plusone" title="Share link on Google+">
                                <i class="socicon socicon-googleplus"></i>
                            </span>


                          </div>

                        </div>
                    </div>
                </div>
            </div>
        </section>

        <footer class="mbr-small-footer mbr-section mbr-section-nopadding" id="footer1-m" style="background-color: rgb(50, 50, 50); padding-top: 1.75rem; padding-bottom: 1.75rem;">

            <div class="container">
                <p class="text-xs-center">Copyright (c) {}, All Rights Reserved - <a href="https://prointernetincome.com" target="_blank">Copyright Pro Internet Income</a></p>
                <br>
                <h6>Purchased From VideoDomainer.com Link: <a>https://videodomainer.com </a></h6> 
            </div>
        </footer>


          <script src="assets/web/assets/jquery/jquery.min.js"></script>
          <script src="assets/tether/tether.min.js"></script>
          <script src="assets/bootstrap/js/bootstrap.min.js"></script>
          <script src="assets/smooth-scroll/smooth-scroll.js"></script>
          <script src="assets/masonry/masonry.pkgd.min.js"></script>
          <script src="assets/imagesloaded/imagesloaded.pkgd.min.js"></script>
          <script src="assets/bootstrap-carousel-swipe/bootstrap-carousel-swipe.js"></script>
          <script src="assets/social-likes/social-likes.js"></script>
          <script src="assets/theme/js/script.js"></script>
          <script src="assets/mobirise-gallery/player.min.js"></script>
          <script src="assets/mobirise-gallery/script.js"></script>
          


        </body>
        </html>'''

        html_template_2 = '''<!DOCTYPE html>
<html>
<head>
  <!-- Site made with Mobirise Website Builder v3.12.1, https://mobirise.com -->
  <meta charset="UTF-8">
  {}
  {}
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v3.12.1, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="assets/images/videoplaybutton-128x128.png" type="image/x-icon">
  <meta name="description" content="">
  <title>{}</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic&amp;subset=latin">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i">
  <link rel="stylesheet" href="assets/bootstrap-material-design-font/css/material.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  
  
  
</head>
<body>
<section class="mbr-section mbr-section__container article" id="header3-4u" style="background-color: magenta; padding-top: 40px; padding-bottom: 40px;">
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <h3 class="mbr-section-title display-2">{}</h3>
                
            </div>
        </div>
    </div>
</section>

<section class="engine"><a rel="external" href="https://mobirise.com">Web Maker</a></section><section class="mbr-section" id="msg-box5-53" style="background-color: rgb(255, 255, 255); padding-top: 40px; padding-bottom: 40px;">

    
    <div class="container">
        <div class="row">
            <div class="mbr-table-md-up">

              

              <div class="mbr-table-cell col-md-5 text-xs-center text-md-right content-size">
                  <h5 class="mbr-section-title display-2">{}</h5>
                  <div class="lead">

                    <p>{}</p>

                  </div>

                  
              </div>


              


              <div class="mbr-table-cell mbr-left-padding-md-up mbr-valign-top col-md-7 image-size" style="width: 50%;">
                  <div class="mbr-figure"><iframe width="560" height="315" src="https://www.youtube.com/embed/{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
              </div>

            </div>
        </div>
    </div>

</section>
    
    <div class="container">
            <h6><pre>{}</pre></h6>
        </div>
    
<section class="mbr-section" id="form2-54" style="background-color: rgb(50, 50, 50); padding-top: 40px; padding-bottom: 120px;">
        <div class="mbr-section mbr-section__container mbr-section__container--middle">
        <div class="container">
            <div class="row">
                <div class="col-xs-12 text-xs-center">
                    
                    <small class="mbr-section-subtitle">Enter your email address below for instant free access</small>
                </div>
            </div>
        </div>
    </div>
    <div class="mbr-section mbr-section-nopadding">
        <div class="container">
            <div class="row">
                <div class="col-xs-12 col-lg-10 col-lg-offset-1" data-form-type="formoid">
                    <div data-form-alert="true"><div hidden="" data-form-alert-success="true">Thanks for filling out form!</div></div>
                    <form class="mbr-form" action="{}" method="post" data-form-title="SUBSCRIBE FORM">
                        <input type="hidden" value="617VtQyYKeATcc6gO37UgoXuQRsNB614VQNP1K7+1haNAVfqCycZ4AaRXEv5qJy8cDS7SGZNN6hQd9EWW8L599ZENbRuYde2yM1QroPyrLJq6hPf5zvveSC5GDCpEkQm" data-form-email="true">
                        <div class="mbr-subscribe mbr-subscribe-dark input-group">
                            <input type="email" class="form-control" name="email" required="" data-form-field="Email" placeholder="Enter Your Email Address..." id="form2-54-email">
                            <span class="input-group-btn"><button type="submit" class="btn btn-primary">SUBSCRIBE</button></span>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="mbr-section mbr-section__container article" id="header3-50" style="background-color: rgb(50, 50, 50); padding-top: 40px; padding-bottom: 20px;">
    <div class="container">
        <div class="row">
            <div class="col-xs-12">
                <h3 class="mbr-section-title display-2"><a href="videopage1.html">Get help with all aspects of ......</a><br><a href="videopage1.html">in our special Video Directory</a></h3>
                
            </div>
        </div>
    </div>
</section>

<section class="mbr-section mbr-section-md-padding" id="social-buttons3-51" style="background-color: rgb(50, 50, 50); padding-top: 30px; padding-bottom: 0px;">
    
    <div class="container">
        <div class="row">
            <div class="col-md-8 col-md-offset-2 text-xs-center">
                <h3 class="mbr-section-title display-2">Share This Page</h3>
                <div>

                  <div class="mbr-social-likes" data-counters="false">
                    <span class="btn btn-social facebook" title="Share link on Facebook">
                        <i class="socicon socicon-facebook"></i>
                    </span>
                    <span class="btn btn-social twitter" title="Share link on Twitter">
                        <i class="socicon socicon-twitter"></i>
                    </span>
                    <span class="btn btn-social plusone" title="Share link on Google+">
                        <i class="socicon socicon-googleplus"></i>
                    </span>
                    
                    
                  </div>

                </div>
            </div>
        </div>
    </div>
</section>

<footer class="mbr-small-footer mbr-section mbr-section-nopadding" id="footer1-4v" style="background-color: cyan; padding-top: 1.75rem; padding-bottom: 1.75rem;">
    
    <div class="container">
        <p class="text-xs-center">Copyright (c) {}, All Rights Reserved - <a href="https://www.prointernetincome.com" target="_blank">Pro Internet Income</a></p>
        <br>
        <h6>Purchased From VideoDomainer.com Link: <a>https://videodomainer.com </a></h6>
    </div>
</footer>


  <script src="assets/web/assets/jquery/jquery.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/smooth-scroll/smooth-scroll.js"></script>
  <script src="assets/social-likes/social-likes.js"></script>
  <script src="assets/theme/js/script.js"></script>
  <script src="assets/formoid/formoid.min.js"></script>
  
  
</body>
</html>'''

        html_template_3 = '''
        <!DOCTYPE html>
        <html>
        <head>
          <!-- Site made with Mobirise Website Builder v3.12.1, https://mobirise.com -->
          <meta charset="UTF-8">
          {}
          {}
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="generator" content="Mobirise v3.12.1, mobirise.com">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="shortcut icon" href="assets/images/videoplaybutton-128x128.png" type="image/x-icon">
          <meta name="description" content="">
          <title>{}</title>
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic&amp;subset=latin">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,700">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i">
          <link rel="stylesheet" href="assets/bootstrap-material-design-font/css/material.css">
          <link rel="stylesheet" href="assets/tether/tether.min.css">
          <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
          <link rel="stylesheet" href="assets/socicon/css/styles.css">
          <link rel="stylesheet" href="assets/theme/css/style.css">
          <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
          
          
          
        </head>
        <body>
        <section class="mbr-section mbr-section__container article" id="header3-3j" style="background-color: rgb(50, 50, 50); padding-top: 40px; padding-bottom: 40px;">
            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <h3 class="mbr-section-title display-2">{}</h3>
                        
                    </div>
                </div>
            </div>
        </section>
        
        <div class="container">
                    <table>
                        <tr>  
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                        </tr>
                        <tr>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                        </tr>
                        <tr>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                        </tr>
                        
                        <tr>  
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                        </tr>
                        <tr>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                        </tr>
                        <tr>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                            <td><div class="card" style="height:290px; width: 290px;">
                                    <div class="card-image">
                                    <a href="{}"><img src="{}" style="height:200px; width: 290px;"></a>
                                    </div>
                                    <div class="card-content">
                                        <p><h6>{}</h6></p>
                                    </div>
                                    <div class="card-action">
                                        <a href="{}"></a>
                                    </div>
                                </div></td>
                        </tr>
                    </table>
                </div>
            
            
            <div class="container">
                    <h6><pre>{}</pre></h6>
                </div>
            
        <section class="mbr-section mbr-section__container" id="buttons1-i" style="background-color: rgb(50, 50, 50); padding-top: 40px; padding-bottom: 20px;">
        
            <div class="container">
                <div class="row">
                    <div class="col-xs-12">
                        <div class="text-xs-center"> <a class="btn btn-white-outline btn-white" href="{}">&lt;&lt; Previous Page</a> <a class="btn btn-white-outline btn-white" href=".">{}</a> <a class="btn btn-white-outline btn-white" href="{}">Next Page &gt;&gt;</a></div>
                    </div>
                </div>
            </div>
        
        </section>
        
        <section class="mbr-section" id="form2-1r" style="background-color: rgb(50, 50, 50); padding-top: 0px; padding-bottom: 0px;">
                <div class="mbr-section mbr-section__container mbr-section__container--middle">
                <div class="container">
                    <div class="row">
                        <div class="col-xs-12 text-xs-center">
                            
                            
                        </div>
                    </div>
                </div>
            </div>
            <div class="mbr-section mbr-section-nopadding">
                <div class="container">
                    <div class="row">
                        <div class="col-xs-12 col-lg-10 col-lg-offset-1" data-form-type="formoid">
                            
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="mbr-section mbr-section-md-padding" id="social-buttons3-1q" style="background-color: rgb(50, 50, 50); padding-top: 30px; padding-bottom: 0px;">
            
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2 text-xs-center">
                        <h3 class="mbr-section-title display-2">Share This Page</h3>
                        <div>
        
                          <div class="mbr-social-likes" data-counters="false">
                            <span class="btn btn-social facebook" title="Share link on Facebook">
                                <i class="socicon socicon-facebook"></i>
                            </span>
                            <span class="btn btn-social twitter" title="Share link on Twitter">
                                <i class="socicon socicon-twitter"></i>
                            </span>
                            <span class="btn btn-social plusone" title="Share link on Google+">
                                <i class="socicon socicon-googleplus"></i>
                            </span>
                            
                            
                          </div>
        
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="mbr-small-footer mbr-section mbr-section-nopadding" id="footer1-2" style="background-color: rgb(50, 50, 50); padding-top: 1.75rem; padding-bottom: 1.75rem;">
            
            <div class="container">
                <p class="text-xs-center">Copyright (c) {}, All Rights Reserved - <a href="https://www.prointernetincome.com" target="_blank">Pro Internet Income</a></p>
                <br>
                <h6>Purchased From VideoDomainer.com Link: <a>https://videodomainer.com </a></h6>
            </div>
        </footer>
        
        
          <script src="assets/web/assets/jquery/jquery.min.js"></script>
          <script src="assets/tether/tether.min.js"></script>
          <script src="assets/bootstrap/js/bootstrap.min.js"></script>
          <script src="assets/smooth-scroll/smooth-scroll.js"></script>
          <script src="assets/social-likes/social-likes.js"></script>
          <script src="assets/theme/js/script.js"></script>
          
          
        </body>
        </html>'''

        punc = '''`=+|><!()-[]{};:'"\,<>./?@#$%^&*_~'''
        allowed = 'abcdefghijklmnopqrst uvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        src = r"{}\\assets".format(os.getcwd())
        dst = r"{}\\assets".format(self.output_folder)



        year = str(year) + ' :  ' + str(self.site_name) + '.com'

        try:
            shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2,
                            ignore_dangling_symlinks=False, dirs_exist_ok=False)
        except:
            time.sleep(0.01)

        if self.site_type.currentText() == "Simple Video Site":
            for c, i in enumerate(a.results):

                try:
                    self.video_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    for j in range(12):
                        NAAM = ''
                        count = random.randint(0, int(len(a.results)))
                        try:
                            self.video_cards[j] = [a.results[count].title]
                        except:
                            time.sleep(0.01)

                        try:
                            for ele in self.video_cards[j][0]:
                                if ele in allowed:
                                    NAAM += ele
                        except:
                            time.sleep(0.01)
                        self.video_cards[j][0] = NAAM
                        self.video_cards[j].append(self.output_folder + '/' + NAAM + '.html')
                        self.video_cards[j].append(a.results[count].thumbnail_url)

                        print(f'i = {i}, \tj = {j}')
                        print(self.video_cards)
                    print(c, i.title, '\t\t', i.video_id)  # length, views, author
                    print("link : \t {}{}".format(self.link_prefix, i.video_id))

                    print('Embed link : \t {}'.format(embed_link.format(i.video_id)))
                    el = embed_link.format(i.video_id)
                    naam = ''
                    for ele in i.title:
                        if ele in allowed:
                            naam += ele
                    name = self.output_folder + '/' + naam + '.html'
                    self.more_video = self.output_folder + '/' + self.video_cards[0][0] + '.html'

                    f = open(name, 'w')
                    f.write(
                        html_template.format(self.analytics_script, self.adsense_script, naam, self.site_name, naam, self.domain_for_sale, i.video_id.lstrip().rstrip(),
                                             self.ad_title_value,
                                             self.ad_text, self.button_link_value, self.button_text_value, self.ad_unit_banner, self.ad_unit_code, self.search_domain, self.article_text,
                                             self.amazon_search_buttons,
                                             self.video_cards[0][1], self.video_cards[0][2], self.video_cards[0][0],
                                             self.video_cards[0][1],
                                             self.video_cards[1][1], self.video_cards[1][2], self.video_cards[1][0],
                                             self.video_cards[1][1],
                                             self.video_cards[2][1], self.video_cards[2][2], self.video_cards[2][0],
                                             self.video_cards[2][1],
                                             self.video_cards[3][1], self.video_cards[3][2], self.video_cards[3][0],
                                             self.video_cards[3][1],
                                             self.video_cards[4][1], self.video_cards[4][2], self.video_cards[4][0],
                                             self.video_cards[4][1],
                                             self.video_cards[5][1], self.video_cards[5][2], self.video_cards[5][0],
                                             self.video_cards[5][1],
                                             self.video_cards[6][1], self.video_cards[6][2], self.video_cards[6][0],
                                             self.video_cards[6][1],
                                             self.video_cards[7][1], self.video_cards[7][2], self.video_cards[7][0],
                                             self.video_cards[7][1],
                                             self.video_cards[8][1], self.video_cards[8][2], self.video_cards[8][0],
                                             self.video_cards[8][1],
                                             self.video_cards[9][1], self.video_cards[9][2], self.video_cards[9][0],
                                             self.video_cards[9][1],
                                             self.video_cards[10][1], self.video_cards[10][2], self.video_cards[10][0],
                                             self.video_cards[10][1],
                                             self.video_cards[11][1], self.video_cards[11][2], self.video_cards[11][0],
                                             self.video_cards[11][1],
                                             self.more_video, self.ad_unit_banner, self.ad_unit_code, year))
                    f.close()
                    print(c)
                except:
                    print('error in link :', c)

        elif self.site_type.currentText() == 'Squeeze Site':
            for c, i in enumerate(a.results):
                try:

                    print(c, i.title, '\t\t', i.video_id)  # length, views, author
                    print("link : \t {}{}".format(self.link_prefix, i.video_id))

                    print('Embed link : \t {}'.format(embed_link.format(i.video_id)))
                    el = embed_link.format(i.video_id)
                    naam = ''
                    for ele in i.title:
                        if ele in allowed:
                            naam += ele
                    name = self.output_folder + '/' + naam + '.html'

                    f = open(name, 'w')
                    f.write(
                        html_template_2.format(self.analytics_script, self.adsense_script, naam, self.site_name, naam, i.description.lstrip().rstrip(), i.video_id.lstrip().rstrip(),
                                             self.article_text, self.search_domain, year))
                    f.close()
                    print(c)
                except:
                    print("Error in site:\t", c)

        elif self.site_type.currentText() == 'Sales Site':
            for c in range(int((len(a.results))/24)):
                self.previous = self.output_folder + '/videopage1' + '.html'
                self.more_video_next = self.output_folder + '/videopage1' + '.html'
                try:
                    self.video_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                    for j in range(24):
                        NAAM = ''
                        count = (c * 24) + j
                        try:
                            self.video_cards[j] = [a.results[count].title]
                        except:
                            time.sleep(0.01)

                        try:
                            for ele in self.video_cards[j][0]:
                                if ele in allowed:
                                    NAAM += ele
                        except:
                            time.sleep(0.01)
                        self.video_cards[j][0] = NAAM
                        self.video_cards[j].append(self.output_folder + '/' + NAAM + '.html')
                        self.video_cards[j].append(a.results[count].thumbnail_url)


                        print(f'i = {c}, \tj = {j}')
                        print(c, a.results[count].title, '\t\t', a.results[count].video_id)  # length, views, author
                        print("link : \t {}{}".format(self.link_prefix, a.results[count].video_id))


                    name = self.output_folder + '/videopage' + str(c+1) + '.html'
                    print(name)
                    self.previous = self.more_video_next
                    self.more_video_next = self.output_folder + '/videopage' + str((c + 2)) + '.html'
                    self.current_page = str((c+1))

                    print(self.more_video_next)

                    f = open(name, 'w')
                    print('wwwww')
                    f.write(html_template_3.format(self.analytics_script, self.adsense_script, 'Video Page {}'.format(str(c+1)), self.site_name,
                                             self.video_cards[0][1], self.video_cards[0][2], self.video_cards[0][0],
                                             self.video_cards[0][1],
                                             self.video_cards[1][1], self.video_cards[1][2], self.video_cards[1][0],
                                             self.video_cards[1][1],
                                             self.video_cards[2][1], self.video_cards[2][2], self.video_cards[2][0],
                                             self.video_cards[2][1],
                                             self.video_cards[3][1], self.video_cards[3][2], self.video_cards[3][0],
                                             self.video_cards[3][1],
                                             self.video_cards[4][1], self.video_cards[4][2], self.video_cards[4][0],
                                             self.video_cards[4][1],
                                             self.video_cards[5][1], self.video_cards[5][2], self.video_cards[5][0],
                                             self.video_cards[5][1],
                                             self.video_cards[6][1], self.video_cards[6][2], self.video_cards[6][0],
                                             self.video_cards[6][1],
                                             self.video_cards[7][1], self.video_cards[7][2], self.video_cards[7][0],
                                             self.video_cards[7][1],
                                             self.video_cards[8][1], self.video_cards[8][2], self.video_cards[8][0],
                                             self.video_cards[8][1],
                                             self.video_cards[9][1], self.video_cards[9][2], self.video_cards[9][0],
                                             self.video_cards[9][1],
                                             self.video_cards[10][1], self.video_cards[10][2], self.video_cards[10][0],
                                             self.video_cards[10][1],
                                             self.video_cards[11][1], self.video_cards[11][2], self.video_cards[11][0],
                                             self.video_cards[11][1],
                                             self.video_cards[12][1], self.video_cards[12][2], self.video_cards[12][0],
                                             self.video_cards[12][1],
                                             self.video_cards[13][1], self.video_cards[13][2], self.video_cards[13][0],
                                             self.video_cards[13][1],
                                             self.video_cards[14][1], self.video_cards[14][2], self.video_cards[14][0],
                                             self.video_cards[14][1],
                                             self.video_cards[15][1], self.video_cards[15][2], self.video_cards[15][0],
                                             self.video_cards[15][1],
                                             self.video_cards[16][1], self.video_cards[16][2], self.video_cards[16][0],
                                             self.video_cards[16][1],
                                             self.video_cards[17][1], self.video_cards[17][2], self.video_cards[17][0],
                                             self.video_cards[17][1],
                                             self.video_cards[18][1], self.video_cards[18][2], self.video_cards[18][0],
                                             self.video_cards[18][1],
                                             self.video_cards[19][1], self.video_cards[19][2], self.video_cards[19][0],
                                             self.video_cards[19][1],
                                             self.video_cards[20][1], self.video_cards[20][2], self.video_cards[20][0],
                                             self.video_cards[20][1],
                                             self.video_cards[21][1], self.video_cards[21][2], self.video_cards[21][0],
                                             self.video_cards[21][1],
                                             self.video_cards[22][1], self.video_cards[22][2], self.video_cards[22][0],
                                             self.video_cards[22][1],
                                             self.video_cards[23][1], self.video_cards[23][2], self.video_cards[23][0],
                                             self.video_cards[23][1], self.article_text, self.previous, self.current_page, self.more_video_next, year))
                    f.close()
                    print(c)

                except:
                    print('error in link :', c)

        print('\n\n\n\tfinished !')
        try:
            shutil.make_archive(self.output_folder, 'zip', self.output_folder)
        except:
            print("Zip not made")






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())




