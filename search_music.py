from PyQt5 import QtWidgets
from ui.search_music_form import Ui_search_music_form


class SearchMusic(QtWidgets.QWidget, Ui_search_music_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(SearchMusic, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.setup()

    def setup(self):
        self.result_line.clear()

        self.back_button.clicked.connect(self.back)

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self