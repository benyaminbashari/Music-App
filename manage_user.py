from PyQt5 import QtWidgets
from ui.manage_user_form import Ui_manage_user_form


class ManageUserWidget(QtWidgets.QWidget, Ui_manage_user_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(ManageUserWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):

        self.playlist_widget.clear()
        self.music_widget.clear()
        self.user_widget.clear()
        self.playlist_combo.clear()
        self.music_combo.clear()
        self.user_combo.clear()
        self.request_widget.clear()

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id, username FROM playlist")
        for row in cursor:
            s = row[0] + "-" + str(row[1]) + "-" + str(row[2])
            self.playlist_widget.addItem(s)
            self.playlist_combo.addItem(s)


        cursor.execute("SELECT music.title, music.id, composer_music.username FROM music, composer_music WHERE music.id=composer_music.music_id")
        for row in cursor:
            s = row[0] + "-" + str(row[1]) + "-" + str(row[2])
            self.music_widget.addItem(s)
            self.music_combo.addItem(s)

        cursor.execute("SELECT name FROM user")
        for row in cursor:
            s = str(row[0])
            if s != self.username:
                self.user_widget.addItem(s)
                self.user_combo.addItem(s)

        cursor.execute("SELECT request_music.username, music.title, request_music.music_id FROM request_music, music WHERE music.id=request_music.music_id")
        for row in cursor:
            s = row[0] + "-" + str(row[1]) + "-" + str(row[2])
            self.request_widget.addItem(s)
            self.request_combo.addItem(s)

        self.back_button.clicked.connect(self.back)
        self.playlist_button.clicked.connect(self.delete_playlist)
        self.music_button.clicked.connect(self.delete_music)
        self.user_button.clicked.connect(self.delete_user)
        self.accept_button.clicked.connect(self.accept)

    def accept(self):
        try:
            music_selected = self.request_combo.currentText()
            if music_selected == "":
                raise Exception
            music_id = (music_selected.split("-"))[2]

            cursor = self.sql_connector.cursor()
            cursor.execute('DELETE FROM request_music WHERE request_music.music_id=%s ', (music_id,))
            cursor.execute('INSERT INTO accept_music VALUES (%s, %s)', (self.username, music_id))
            self.sql_connector.commit()
            self.setup()

        except:
            pass

    def delete_playlist(self):
        try :
            playlist_name = self.playlist_combo.currentText()
            if playlist_name == "":
                raise Exception
            playlist_id = (playlist_name.split("-"))[1]

            cursor = self.sql_connector.cursor()
            cursor.execute('DELETE FROM music_list WHERE music_list.id=%s ', (playlist_id,))
            self.sql_connector.commit()
            self.setup()

        except:
            pass

    def delete_music(self):
        try:
            music_name = self.music_combo.currentText()
            if music_name == "":
                raise  Exception
            music_id = (music_name.split("-"))[1]

            cursor = self.sql_connector.cursor()
            cursor.execute('DELETE FROM music WHERE music.id=%s', (music_id, ))
            cursor.execute("DELETE FROM composer_music WHERE composer_music.music_id=%s", (music_id, ))
            self.sql_connector.commit()
            self.setup()

        except:
            pass

    def delete_user(self):

        username = self.user_combo.currentText()
        if username == "":
            raise Exception

        cursor = self.sql_connector.cursor()
        cursor.execute('DELETE FROM user WHERE name=%s', (username,))
        self.sql_connector.commit()
        self.setup()

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self


