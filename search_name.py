from PyQt5 import QtWidgets
from ui.search_name_form import Ui_search_name_form


class SearchNameWidget(QtWidgets.QWidget, Ui_search_name_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(SearchNameWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.setup()

    def setup(self):

        self.result_line.clear()
        self.back_button.clicked.connect(self.back)
        self.search_button.clicked.connect(self.search)

    def search(self):
        self.setup()
        cursor = self.sql_connector.cursor()
        txt = self.username_line.text()
        cursor.execute("SELECT name from user WHERE name=%s", (txt,))
        for row in cursor:
            self.result_line.addItem("Username: " + row[0])



    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

