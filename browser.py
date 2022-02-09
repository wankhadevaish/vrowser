import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngine import*
from PyQt5.QtWebEngineWidgets import*

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView() #see webview
        self.browser.setUrl(QUrl('http://google.com')) #url in qurl
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn =QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn =QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)


        reload_btn =QAction('Reload',self)
        back_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)


        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home) #new mwthod created
        navbar.addAction((home_btn))


        self.url_bar = QLineEdit() #instance attribute
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)




    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
       url = self.url_bar.text()
       self.browser.setUrl(QUrl(url))




app =QApplication(sys.argv)
QApplication.setApplicationName('Vrowser')
window = MainWindow()
app.exec_()

