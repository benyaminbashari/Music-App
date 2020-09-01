
from PyQt5 import QtWidgets
from ui.like_form import Ui_like_form


class LikeWidget(QtWidgets.QWidget, Ui_like_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(LikeWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):
        self.liked_list.clear()
        self.music_list.clear()
        self.music_combo.clear()

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id FROM music")
        musics = []
        for row in cursor:
            self.music_list.addItem(row[0] + "-" + str(row[1]))
            musics.append((row[0], str(row[1])))

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT music.title, music.id FROM music, user_music_like WHERE music.id=user_music_like.music_id and user_music_like.username=%s", (self.username, ))
        liked = set()
        for row in cursor:
            self.liked_list.addItem(row[0] + "-" + str(row[1]))
            liked.add((row[0], str(row[1])))

        for music in musics:
            if music not in liked:
                self.music_combo.addItem(music[0]+"-"+ music[1])

        self.like_button.clicked.connect(self.like)
        self.back_button.clicked.connect(self.back)


    def like(self):
        id = int(self.music_combo.currentText().split('-')[1])
        cursor = self.sql_connector.cursor()
        cursor.execute("INSERT INTO user_music_like VALUES(%s, %s)", (self.username, id))
        self.sql_connector.commit()
        self.setup()

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

