from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import  QQuickView
import sys

VIEW_PATH = "view.qml"

# Create the application object and pass command line arguments to it - okýnko
app = QGuiApplication(sys.argv)

# Create the view object - view = text uvnitř okýnka
view = QQuickView()
# Set the QML file to view
view.setSource(QUrl(VIEW_PATH))
# Resize the view with the window - uživatelské prostředí se roztáhne na velikost okna
view.setResizeMode(QQuickView.ResizeMode.SizeRootObjectToView)
# Show the view (open the window) - zobrazit to
view.show()

# Run the event loop
app.exec()

