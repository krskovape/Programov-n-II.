# okýnka D, M, S, pro převedené D
#tlačítko nahoře To DEG, To DMS

from PySide6.QtCore import QObject, Slot, Property, QUrl, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView
import sys

VIEW_URL = "view_d.qml"

class dmsModel(QObject):
    def __init__(self):
        QObject.__init__(self)
        self._deg = 0
        self._min = 0
        self._sec = 0
        self._deg_float = 0.0
    
    #Property deg
    def get_deg(self):
        return self._deg
    
    def set_deg(self,val):
        print(f"Current: {self._deg}, new: {val}")
        if val != self._deg:
            self._deg = val
            self.deg_changed.emit()
    
    deg_changed = Signal()
    deg = Property(int, get_deg, set_deg, notify=deg_changed)

    #Property min
    def get_min(self):
        return self._min
    
    def set_min(self,val):
        print(f"Current: {self._min}, new: {val}")
        if val != self._min:
            self._min = val
            self.min_changed.emit()
    
    min_changed = Signal()
    min = Property(int, get_min, set_min, notify=min_changed)

    #Property sec
    def get_sec(self):
        return self._sec

    def set_sec(self,val):
        print(f"Current {self._sec}, new: {val}")
        if val != self._sec:
            self._sec = val
            self.sec_changed.emit()

    sec_changed = Signal()
    sec = Property(int, get_sec, set_sec, notify=sec_changed)

    #Property deg_float
    def get_deg_float(self):
        return self._deg_float

    def set_deg_float(self,val):
        print(f"Current {self._deg_float}, new: {val}")
        if val != self._deg_float:
            self._deg_float = val
            self.deg_float_changed.emit()
    
    deg_float_changed = Signal()
    deg_float = Property(float,get_deg_float,set_deg_float,notify=deg_float_changed)

    @Slot()
    def to_deg(self):
        print("Converting to DEG")
        self.deg_float = self.deg + self.min/60 + self.sec/3600
    
    @Slot()
    def to_dms(self):
        print("Converting to DMS")
        self.deg = int(self.deg_float)
        val = (self.deg_float - self.deg)*60
        self.min = int(val)
        self.sec = int((val - self.sec)*60)

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)

dms_model = dmsModel()
ctxt = view.rootContext()
ctxt.setContextProperty("dmsModel", dms_model)

view.setSource(url)
view.show()
app.exec_()