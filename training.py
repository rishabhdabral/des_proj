# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
import time
from table import Window as w
import threading
"""
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s
"""

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow,self).__init__(parent)
		self.central_widget = QtGui.QStackedWidget()
		self.setCentralWidget(self.central_widget)

		self.time1 = 3.5
		self.time2 = 4
		self.time3 = 4.5
		self.time4 = 5
		self.time5 = 6

		homePage = HomePage()
		homePage.button.clicked.connect(self.page1)
		self.central_widget.addWidget(homePage)
	
	def page1(self):
		page_1 = Pages(self.time1)
		
		#self.setBGColor(page_)
		self.central_widget.addWidget(page_1)
		self.central_widget.setCurrentWidget(page_1)
		#self.central_widget.setBackgroundColor(QtGui.QColor('black'))
		page_1.next_button.clicked.connect(self.page2)
	
	def page2(self):
		page_2 = Pages(self.time2)
		self.central_widget.addWidget(page_2)
		self.central_widget.setCurrentWidget(page_2)
		page_2.next_button.clicked.connect(self.page3)

	def page3(self):
		page_3 = Pages(self.time3)
		self.central_widget.addWidget(page_3)
		self.central_widget.setCurrentWidget(page_3)
		page_3.next_button.clicked.connect(self.page4)

	def page4(self):
		page_4 = Pages(self.time4)
		self.central_widget.addWidget(page_4)
		self.central_widget.setCurrentWidget(page_4)
		page_4.next_button.clicked.connect(self.page5)

	def page5(self):
		page_5 = Pages(self.time5)
		self.central_widget.addWidget(page_5)
		self.central_widget.setCurrentWidget(page_5)
		page_5.next_button.clicked.connect(self.page6)

	def page6(self):
		endPage = HomePage()
		endPage.button.setText("End Test")
		endPage.button.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.central_widget.addWidget(endPage)
		self.central_widget.setCurrentWidget(endPage)
	"""	
	def setBGColor(self,page):
		pale = self.page.palette()
		pale.setColor(self.page.backgroundRole(),QtGui.QColor('black'))
		self.page.setPalette(pale)	    
	"""
class HomePage(QtGui.QWidget):
	def __init__(self,parent=None):
		super(HomePage,self).__init__(parent)
		layout = QtGui.QHBoxLayout()
		self.button = QtGui.QPushButton('Start Test')
		layout.addWidget(self.button)
		self.setLayout(layout)
		
class Pages(QtGui.QTableWidget):
	def __init__(self,time,parent=None):
		super(Pages,self).__init__(parent)
		print time
		
		layout = QtGui.QVBoxLayout()
		self.label = QtGui.QLabel('Testing...')
		self.next_button = QtGui.QPushButton('Go To Next Page')
		
		
		#Code for testing the Table
		self.table = QtGui.QTableWidget(1,1,self)
		item = QtGui.QTableWidgetItem("hi")
		self.table.setItem(0,0,item)
		self.table.setColumnWidth(0,465)
		self.table.setRowHeight(0,380)	
		self.table.setShowGrid(False)
		layout.addWidget(self.table)
		self.thread = threading.Thread(target = self.blink, args = (item,time))
		self.thread.start()
		layout.addWidget(self.next_button)
		layout.addWidget(self.label)
		self.setLayout(layout)
		

	def blink(self,item,t):
		print "It's blinking"
		while(True):
			item.setBackground(QtGui.QColor('black'))
			time.sleep(0.01*t)
			item.setBackground(QtGui.QTableWidgetItem().background())
			time.sleep(0.01*t)
		"""
	def blink(self,t):
		print "it's blinking"
		while(True):
			print "It's looping"
			#self.blink_button.setStyleSheet(_fromUtf8("background-color: moccasin"))
			palette = QtGui.QPalette(self.blink_button.palette())
			palette.setColor(QtGui.QPalette.Button, QtGui.QColor('moccasin'))
			self.blink_button.setPalette(palette)
			time.sleep(0.01*t)
			palette.setColor(QtGui.QPalette.Button, QtGui.QColor('white'))
			self.blink_button.setPalette(palette)
			#self.blink_button.setStyleSheet(_fromUtf8("background-color: white"))
			
			time.sleep(0.01*t)
		"""	

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.setGeometry(500,300,500,300)
	p = window.palette()
	p.setColor(window.backgroundRole(),QtGui.QColor('black'))
	window.setPalette(p)
	window.show()
	sys.exit(app.exec_())
