"""
name the object as XXX_form
save the file as XXX.ui
compile with XXX_form.ui
"""

from PyQt5 import QtWidgets
from ui.XXX_form import Ui_XXX_form
#import other pages you want to go from this page

class XXXWidget(QtWidgets.QWidget, Ui_XXX_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(XXXWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

