from PyQt5 import QtWidgets
from ui.first_page_form import Ui_first_page_form


class First_page(QtWidgets.QWidget, Ui_first_page_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(First_page, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):
        self.back_button.clicked.connect(self.back)

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id FROM album WHERE username=%s", (self.username,))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.album_line.addItem(s)

        cursor.execute("SELECT music.title, music.id FROM music, composer_music WHERE composer_music.username=%s and music.id=composer_music.music_id ", (self.username,))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.music_line.addItem(s)

        cursor.execute("SELECT title, id FROM playlist WHERE username=%s", (self.username,))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.playlist_line.addItem(s)


    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

