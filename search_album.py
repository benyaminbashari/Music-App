from PyQt5 import QtWidgets
from ui.search_album_form import Ui_search_album_form
import datetime

class SearchAlbum(QtWidgets.QWidget, Ui_search_album_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(SearchAlbum, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.setup()

    def setup(self):

        self.result_line.clear()

        self.result_line.clear()

        self.back_button.clicked.connect(self.back)
        self.search_calender_button.clicked.connect(self.search_calender)
        self.composer_button.clicked.connect(self.composer_find)
        self.album_button.clicked.connect(self.album_find)
        self.tag_button.clicked.connect(self.tag_find)


    def composer_find(self):
        self.result_line.clear()
        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id FROM album where username=%s", (self.composer_line.text(), ))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.result_line.addItem(s)

    def album_find(self):
        self.result_line.clear()
        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id FROM album where title=%s", (self.album_line.text(),))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.result_line.addItem(s)


    def tag_find(self):
        self.result_line.clear()
        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT album.title, album.id FROM album, music_list_tag where album.id=music_list_tag.music_list_id  and music_list_tag.tag_name=%s", (self.tags_line.text(),))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.result_line.addItem(s)

    def search_calender(self):
        self.result_line.clear()
        self.setup()
        date = self.calendar_widget.selectedDate()
        date = date.toPyDate()
        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT album.title, album.id FROM album, music_list_producer WHERE music_list_producer.music_list_id=album.id and music_list_producer.published_date<=%s", (date,))

        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.result_line.addItem(s)






    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self