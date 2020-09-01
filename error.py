from PyQt5 import QtWidgets
from ui.error_form import Ui_error_form


class ErrorWidget(QtWidgets.QWidget, Ui_error_form):
    def __init__(self, sql_connector, central_widget, msg, backback,  parent=None):
        super(ErrorWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.msg = msg
        self.backback = backback
        self.setup()

    def setup(self):
        self.ok_button.clicked.connect(self.back)
        self.error_label.setText(self.msg)

    def back(self):
        if self.backback:
            self.central_widget.setCurrentWidget(self.parent.parent)
            self.central_widget.removeWidget(self)
            self.central_widget.removeWidget(self.parent)
            del self.parent
            del self
        else:
            self.central_widget.setCurrentWidget(self.parent)
            self.central_widget.removeWidget(self)
            del self

