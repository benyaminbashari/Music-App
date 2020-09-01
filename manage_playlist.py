from PyQt5 import QtWidgets
from ui.manage_playlist_form import Ui_manage_playlist_form
from PyQt5.QtWidgets import QFileDialog
import datetime


class ManagePlayWidget(QtWidgets.QWidget, Ui_manage_playlist_form):
    def __init__(self, user_name, playlist_id, sql_connector, central_widget, parent=None):
        super(ManagePlayWidget, self).__init__(parent)
        self.setupUi(self)
        self.username = user_name
        self.playlist_id = playlist_id
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.image = None
        self.setup()

    def setup(self):

        self.new_playlist_name_line.clear()
        self.song_title_line.clear()
        self.song_writer_line.clear()
        self.duration_line.clear()
        self.photo_choose.clearFocus()
        self.lyrics_line.clear()

        cursor = self.sql_connector.cursor()
        cursor.execute('SELECT type FROM user WHERE name=%s', (self.username, ))
        user_type = ""
        for row in cursor:
            user_type = row[0]

        if user_type == "ordinary" or user_type == "manager":
            self.label_7.hide()
            self.label_8.hide()
            self.song_title_line.hide()
            self.label_2.hide()
            self.id_line.hide()
            self.label_9.hide()
            self.song_writer_line.hide()
            self.label_10.hide()
            self.duration_line.hide()
            self.label_13.hide()
            self.photo_choose.hide()
            self.label_12.hide()
            self.lyrics_line.hide()
            self.add_new_song_button.hide()

        self.rename_ok_button.clicked.connect(self.rename_playlist)
        self.back_button.clicked.connect(self.back)
        self.remove_button.clicked.connect(self.remove)
        self.add_new_song_button.clicked.connect(self.add_song)
        self.photo_choose.clicked.connect(self.select_file)

    def rename_playlist(self):
        new_name = self.new_playlist_name_line.text()
        cursor = self.sql_connector.cursor()
        cursor.execute('UPDATE music_list SET title=%s WHERE music_list.id=%s', (new_name, self.playlist_id))
        self.sql_connector.commit()
        self.back()

    def remove(self):
        cursor = self.sql_connector.cursor()
        cursor.execute('DELETE FROM music_list WHERE music_list.id=%s ', (self.playlist_id,))
        self.sql_connector.commit()
        self.back()

    def select_file(self):
        self.image = QFileDialog.getOpenFileName()[0]

    def add_song(self):
        try:
            title = self.song_title_line.text()
            id = self.id_line.text()
            song_writer = self.song_writer_line.text()
            duration = self.duration_line.text()
            lyrics = self.lyrics_line.text()

            if title == "" or song_writer == "" or id == "" or duration == "" or lyrics == "":
                raise Exception

            cursor = self.sql_connector.cursor()
            cursor.execute("INSERT INTO music VALUES(%s, %s, %s, %s, %s, %s, %s)", (int(id), title, song_writer, int(duration), 0,  lyrics, self.image[0:29]))
            cursor.execute("INSERT INTO composer_music VALUES(%s, %s, %s)", (self.username, int(id), datetime.datetime.now()))
            cursor.execute("INSERT INTO music_list_music VALUES(%s, %s)", (int(self.playlist_id), int(id)))
            cursor.execute("INSERT INTO request_music VALUES (%s, %s)", (self.username, id))
            self.sql_connector.commit()
            self.setup()
            self.error_label.setText("Music requested")

        except:
            self.error_label.setText("One field is empty")

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self
