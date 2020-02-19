import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'OpenVPN GUI'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('openvpn.png'))
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        self.tabs.addTab(self.tab1,"Simple")
        self.tabs.addTab(self.tab2,"Advanced")
        
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Connect")
        self.pushButton2 = QPushButton("Disconnect")
        self.pushButton3 = QPushButton("Status")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.pushButton2)
        self.tab1.layout.addWidget(self.pushButton3)
        def connect():
            os.system("systemctl start myovpn.service")
        def disconnect():
            os.system("systemctl stop myovpn.service")
        def status():
            os.system("systemctl status myovpn.service")
        self.pushButton1.clicked.connect(connect)
        self.pushButton2.clicked.connect(disconnect)
        self.pushButton3.clicked.connect(status)
        self.tab1.setLayout(self.tab1.layout)

        def tos():
            os.system("openvpn --passtos") # Set the TOS field of the tunnel packet to what the payload's TOS is.
        def fastio():
            os.system("openvpn --fast-io") # Optimize  TUN/TAP/UDP I/O writes by avoiding a call to poll/epoll/select prior to the write operation.
        def multihome():
            os.system("openvpn --multihome") # Configure  a  multi-homed  UDP server.
        self.tab2.layout = QVBoxLayout(self)
        self.pushButton4 = QPushButton("TOS")
        self.tab2.layout.addWidget(self.pushButton4)
        self.pushButton4.clicked.connect(tos)
        self.pushButton5 = QPushButton("Optimize (Experimental)")
        self.tab2.layout.addWidget(self.pushButton5)
        self.pushButton5.clicked.connect(fastio)
        self.pushButton6 = QPushButton("Multi home")
        self.tab2.layout.addWidget(self.pushButton6)
        self.pushButton6.clicked.connect(multihome)
        self.tab2.setLayout(self.tab2.layout)


        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
