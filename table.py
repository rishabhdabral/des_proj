from PyQt4 import QtGui, QtCore
import threading
import time
from threading import Timer
import pyttsx

class TableWidget(QtGui.QTableWidget):
    cellExited = QtCore.pyqtSignal(int, int)
    itemExited = QtCore.pyqtSignal(QtGui.QTableWidgetItem)

    def __init__(self, rows, columns, parent=None):
        QtGui.QTableWidget.__init__(self, rows, columns, parent)
        self._last_index = QtCore.QPersistentModelIndex()
        self.viewport().installEventFilter(self)

    def eventFilter(self, widget, event):
        if widget is self.viewport():
            index = self._last_index
            if event.type() == QtCore.QEvent.MouseMove:
                index = self.indexAt(event.pos())
            elif event.type() == QtCore.QEvent.Leave:
                index = QtCore.QModelIndex()
            if index != self._last_index:
                row = self._last_index.row()
                column = self._last_index.column()
                item = self.item(row, column)
                if item is not None:
                    self.itemExited.emit(item)
                self.cellExited.emit(row, column)
                self._last_index = QtCore.QPersistentModelIndex(index)
        return QtGui.QTableWidget.eventFilter(self, widget, event)

class Window(QtGui.QWidget):
    def __init__(self, rows, columns):
        QtGui.QWidget.__init__(self)
        self.table = TableWidget(rows, columns, self)
	self.num_rows = rows
	self.num_columns = columns
	self.text_field = QtGui.QLabel("Hi")
	'''
        for column in xrange(columns):
            for row in xrange(rows):
                item = QtGui.QTableWidgetItem(str(row) + "_" + str(column))
                self.table.setItem(row, column, item)
	'''	
	'''
	for row in xrange(rows-1):
		for column in xrange(columns):
			item = QtGui.QTableWidgetItem(str(3*row + column + 1))
			self.table.setItem(row,column,item)
	#setting the last row of the numpad:
	item = QtGui.QTableWidgetItem("*")
	self.table.setItem(3,0,item)
	item0 = QtGui.QTableWidgetItem("0")
	self.table.setItem(3,1,item0)
	item1 = QtGui.QTableWidgetItem("#")
	self.table.setItem(3,2,item1)
	'''
	item = QtGui.QTableWidgetItem("Could you please get me a glass of water?")
	self.table.setItem(0,0,item)
	item = QtGui.QTableWidgetItem("I wish to watch the cricket match.")
	self.table.setItem(0,1,item)
	item = QtGui.QTableWidgetItem("I am feeling uncomfortable, I want to rest.")
        self.table.setItem(0,2,item)
	item = QtGui.QTableWidgetItem("Call my son.")
        self.table.setItem(0,3,item)
	item = QtGui.QTableWidgetItem("Get me my medication.")
        self.table.setItem(0,4,item)

	for column in xrange(columns):
		self.table.setColumnWidth(column,150)
	for row in xrange(rows+1):
		self.table.setRowHeight(row,60)

	self.point = QtCore.QPoint(0,0) #global variable to know which item in the table is clicked
	self.display_text = ""
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
	layout.addWidget(self.text_field)
	self.table.setMouseTracking(True)
        self.table.cellClicked.connect(self.on_item_clicked)
	self.table.itemEntered.connect(self.handleItemEntered)
        self.table.itemExited.connect(self.handleItemExited)	
	self.freq = 9
	self.freq1 = 10
	self.freq2 = 11
	self.freq3 = 12
	self.freq4 = 13

    def handleItemEntered(self, item):
	'''
	point = QtCore.QPoint(item.row(),item.column())
	#button = item
	print point
        item2 = self.table.itemAt(point)
	print item2
	#print item.row()'''
	
	# Setting timer to click on that button after certain time has elapsed and the cursor is still hovering in the same button!
	self.time_to_click = Timer(1.5,self.on_item_clicked,args = [item.row(),item.column(),])
	self.time_to_click.start()	#This function is called after two seconds if the function remains in the same block.
	
	self.stop = threading.Event()
	item.setBackground(QtGui.QColor('black'))
	try:
		self.thread = threading.Thread(target = self.blink, args = (item,2.5,))
		self.thread.start()
	except:
		print "Unable to start thread"
	try:
		item2 = self.table.item(item.row()+1,item.column())
		item2.setBackground(QtGui.QColor('black'))
		try:
			#self.stop2 = threading.Event()
			self.thread2 = threading.Thread(target = self.blink, args = (item2,3.3,))
			self.thread2.start()
		except:
			print "Unable to start thread2"
	except:
		pass
	try:
		item1 = self.table.item(item.row()-1,item.column())
		item1.setBackground(QtGui.QColor('black'))
		try:
                        #self.stop1 = threading.Event()
                        self.thread1 = threading.Thread(target = self.blink, args = (item1,4.0,))
                        self.thread1.start()
                except:
                        print "Unable to start thread1"

	except:
		pass
	try:
		if item.column() == self.num_columns-1:
			raise Exception
		item3 = self.table.item(item.row(),item.column()+1)
		item3.setBackground(QtGui.QColor('black'))
		try:
                        #self.stop3 = threading.Event()
                        self.thread3 = threading.Thread(target = self.blink, args = (item3,4.3,))
                        self.thread3.start()
                except:
                        print "Unable to start thread3"

	except:
		pass
	try:
		if item.column() == 0:
			raise Exception
		item4 = self.table.item(item.row(),item.column()-1)
		item4.setBackground(QtGui.QColor('black'))
		try:
                        #self.stop4 = threading.Event()
                        self.thread4 = threading.Thread(target = self.blink, args = (item4,5.0,))
                        self.thread4.start()
                except:
                        print "Unable to start thread4"

	except:
		pass

	#Threading to pass to the blinking function
	"""
	while not self.thread1_stop.is_set():
		try:
			self.thread1 = threading.Thread(target = self.blink, args = (item1,))
			self.thread1.start()
		except:
			pass
		"""
	"""
		thread.start_new_thread(blink,(item1,200))
		thread.start_new_thread(blink,(item,300))
		thread.start_new_thread(blink,(item3,400))
		thread.start_new_thread(blink,(item4,500))
	try:
		#self.thread1_stop.clear()
		self.thread1_stop = threading.Event()
		self.thread1 = threading.Thread(target = self.blink, args = (item1,))
		self.thread1.start()
	except:
		 print "Error: Unable to start thread"
	"""


    def on_item_clicked(self,x,y):
	cell_text = self.table.item(x,y).text()
	speak = pyttsx.init()
	speak.say(cell_text)
	speak.runAndWait()
	speak.stop()
	self.display_text += " " + cell_text
	self.text_field.setText(self.display_text)	

    def handleItemExited(self, item):
	self.time_to_click.cancel()
	try:
		self.stop.set()
		#self.stop2.set()
		#self.stop3.set()
		#self.stop4.set()
		self.thread.join()
		self.thread1.join()
		self.thread2.join()
		self.thread3.join()
		self.thread4.join()
		#print "Thread released"
		#self.thread1_stop.clear()
	except:
		print "Error"

	try:
		item2 = self.table.item(item.row()+1,item.column())
	        item2.setBackground(QtGui.QTableWidgetItem().background())
	except:
		pass
	try:
		item1 = self.table.item(item.row()-1,item.column())
		item1.setBackground(QtGui.QTableWidgetItem().background())
	except:
		pass
	try:
		if item.column() == self.num_columns-1:
			raise Exception
		item3 = self.table.item(item.row(),item.column()+1)
		item3.setBackground(QtGui.QTableWidgetItem().background())
	except:
		pass
	try:
		if item.column() == 0:
			raise Exception
		item4 = self.table.item(item.row(),item.column()-1)
		item4.setBackground(QtGui.QTableWidgetItem().background())
	except:
		pass
	item.setBackground(QtGui.QTableWidgetItem().background())	

    def blink(self, item,t):
	#print "It's blinking"
	while (self.stop.is_set()==False):
		#for i in xrange(1000):
		item.setBackground(QtGui.QColor('black'))
		time.sleep(0.01*t)
		item.setBackground(QtGui.QTableWidgetItem().background())
		time.sleep(0.01*t)
	#self.thread1_stop.clear()	


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window(1,5)
    window.setGeometry(500, 300, 800, 350)
    window.show()
    sys.exit(app.exec_())
