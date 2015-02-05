from PyQt4 import QtGui, QtCore

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
	self.text_field = QtGui.QLabel("Hi")
        for column in xrange(columns):
            for row in xrange(rows):
                item = QtGui.QTableWidgetItem(str(row) + "_" + str(column))
                self.table.setItem(row, column, item)

	self.point = QtCore.QPoint(0,0) #global variable to know which item in the table is clicked
	self.display_text = ""
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
	layout.addWidget(self.text_field)
	self.table.setMouseTracking(True)
        self.table.cellClicked.connect(self.on_item_clicked)
	self.table.itemEntered.connect(self.handleItemEntered)
        self.table.itemExited.connect(self.handleItemExited)

    def handleItemEntered(self, item):
	'''
	point = QtCore.QPoint(item.row(),item.column())
	#button = item
	print point
        item2 = self.table.itemAt(point)
	print item2
	#print item.row()'''
	#	print item.row(),item.column()
	#	item.setBackground(QtGui.QColor('moccasin'))
	item2 = self.table.item(item.row()+1,item.column())
	#print item2.row(),item2.column()
	item2.setBackground(QtGui.QColor('moccasin'))
	item1 = self.table.item(item.row()-1,item.column())
	item1.setBackground(QtGui.QColor('moccasin'))
	item3 = self.table.item(item.row(),item.column()+1)
	item3.setBackground(QtGui.QColor('moccasin'))
	item4 = self.table.item(item.row(),item.column()-1)
	item4.setBackground(QtGui.QColor('moccasin'))



    def on_item_clicked(self,x,y):
	cell_text = self.table.item(x,y).text()
	self.display_text += cell_text
	self.text_field.setText(self.display_text)	

    def handleItemExited(self, item):
	item2 = self.table.item(item.row()+1,item.column())
        item2.setBackground(QtGui.QTableWidgetItem().background())
	item1 = self.table.item(item.row()-1,item.column())
	item1.setBackground(QtGui.QTableWidgetItem().background())
	item3 = self.table.item(item.row(),item.column()+1)
	item3.setBackground(QtGui.QTableWidgetItem().background())
	item4 = self.table.item(item.row(),item.column()-1)
	item4.setBackground(QtGui.QTableWidgetItem().background())
	


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window(8, 6)
    window.setGeometry(500, 300, 650, 250)
    window.show()
    sys.exit(app.exec_())
