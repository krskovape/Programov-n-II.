from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2 import QtCore
import typing
import sys
import json

VIEW_URL = "view_mod.qml"  


class NumberListModel(QAbstractListModel):
    """ Class for maintaining list of cities"""

    def __init__(self):
        QAbstractListModel.__init__(self)
        self.number_list = [1,2,3,4]
        self._input_idx = 0
        self._input_num = 0
    
    # property input_idx
    def get_idx(self):
        return self._input_idx
    
    def set_idx(self,val):
        if val != self.input_idx:
            self._input_idx = val
            self.input_idx_changed.emit()
    
    input_idx_changed = Signal()
    input_idx = Property(int, get_idx, set_idx, notify=input_idx_changed)

    #property input_num
    def get_num(self):
        return self._input_num
    
    def set_num(self, val):
        if val != self.input_num:
            self._input_num = val
            self.input_num_changed.emit()
    
    input_num_changed = Signal()
    input_num = Property(int, get_num, set_num, notify=input_num_changed)

    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        return len(self.number_list)

    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        """ For given index and DisplayRole return name of the selected number"""
        # Return None if the index is not valid
        if not index.isValid():
            return None
        # If the role is the DisplayRole, return the number
        if role == QtCore.Qt.DisplayRole:
            return self.number_list[index.row()]
    
    @Slot()
    def add_num(self):
        print("Adding 42")
        self.beginInsertRows(self.index(0).parent(),self.input_idx, self.input_idx)
        self.number_list.insert(self.input_idx, self.input_num)
        self.endInsertRows()
        print(self.number_list)
    
    @Slot(int)
    def remove_num(self,idx: int):
        if idx == -1: #není zvolený žádný prvek
            return
        print(f"Removing row {idx}")
        self.beginRemoveRows(self.index(0).parent(),idx,idx)
        self.number_list.pop(idx)
        self.endRemoveRows()

    @Slot()
    def remove_all(self):
        self.beginRemoveRows(self.index(0).parent(), 0 , len(self.number_list)-1)
        self.number_list = []
        self.endRemoveRows()

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
numberlist_model = NumberListModel()
ctxt = view.rootContext()
ctxt.setContextProperty('numberListModel',numberlist_model)
view.setSource(url)
view.show()
app.exec_()