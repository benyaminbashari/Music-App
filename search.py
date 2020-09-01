
from PyQt5 import QtWidgets
from ui.search_form import Ui_search_form
from search_name import SearchNameWidget
from search_album import SearchAlbum
from search_music import SearchMusic

class SearchWidget(QtWidgets.QWidget, Ui_search_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(SearchWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.setup()


    def setup(self):
        self.result_list.clear()
        self.back_button.clicked.connect(self.back)
        self.ok_button.clicked.connect(self.search)
        self.search_name_button.clicked.connect(self.srch_name)
        self.search_album_button.clicked.connect(self.search_album)
        self.pushBusearch_music_buttontton_3.clicked.connect(self.search_music)


    def search_music(self):
        self.hide()
        searchmusic_widget = SearchMusic(self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(searchmusic_widget)
        self.central_widget.setCurrentWidget(searchmusic_widget)

    def srch_name(self):
        self.hide()
        searchn_widget = SearchNameWidget(self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(searchn_widget)
        self.central_widget.setCurrentWidget(searchn_widget)


    def search_album(self):
        self.hide()
        searchalbum_widget = SearchAlbum(self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(searchalbum_widget)
        self.central_widget.setCurrentWidget(searchalbum_widget)




    def search(self):
        self.setup()
        cursor = self.sql_connector.cursor()
        txt = self.name_search_line.text()
        cursor.execute("SELECT name from user WHERE name=%s", (txt, ))
        for row in cursor:
            self.result_list.addItem("Username: " + row[0])

        cursor.execute("SELECT title, id from music WHERE title=%s", (txt,))
        for row in cursor:
            self.result_list.addItem("Music ID: " + str(row[1]) + " Music Title: " + row[0])

        cursor.execute("SELECT title, id from music_list WHERE title=%s", (txt,))
        for row in cursor:
            self.result_list.addItem("List ID: " + str(row[1]) + " List Title: " + row[0])


    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

