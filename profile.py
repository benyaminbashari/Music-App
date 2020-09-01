from PyQt5 import QtWidgets
from ui.profile_form import Ui_profile_form
from manage_playlist import ManagePlayWidget
from change_pass import Change_pass
from PyQt5.QtWidgets import QFileDialog


class ProfileWidget(QtWidgets.QWidget, Ui_profile_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(ProfileWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):
        self.tags_combo_2.clear()
        self.tags_view_2.clear()
        self.playlist_view_2.clear()
        self.listen_mu_view_2.clear()
        self.post_music_view_2.clear()
        self.liked_mu_view_2.clear()

        self.dashboard_button_2.clicked.connect(self.back)
        self.photo_choose.clicked.connect(self.photo)
        cursor = self.sql_connector.cursor()



        cursor.execute("SELECT email, type FROM user WHERE name=%s", (self.username, ))
        for row in cursor:
            self.email_label.setText(row[0])

        self.username_label.setText(self.username)

        cursor.execute("SELECT photo_path FROM user WHERE name=%s", (self.username, ))
        for row in cursor:
            d = row[0]
            self.image_label.setStyleSheet("background-image:url(" + d + ")")


        cursor.execute("SELECT count(*) FROM user_follow WHERE following=%s", (self.username, ))
        for row in cursor:
            self.follow_num.setText(str(row[0]))

        cursor.execute("SELECT count(*) FROM user_follow WHERE follower=%s", (self.username, ))
        for row in cursor:
            self.following_num.setText(str(row[0]))

        cursor.execute("SELECT title FROM music, user_music_like WHERE music.id = user_music_like.music_id and user_music_like.username=%s", (self.username, ))
        for row in cursor:
            self.liked_mu_view_2.addItem(row[0])

        cursor.execute("SELECT title FROM music, user_listen WHERE music.id = user_listen.music_id and user_listen.username=%s", (self.username,))
        for row in cursor:
            self.listen_mu_view_2.addItem(row[0])

        cursor.execute("SELECT name FROM tag")
        for row in cursor:
            self.tags_combo_2.addItem(row[0])

        self.add_tag_button_2.clicked.connect(self.add_tag)

        cursor.execute("SELECT tag_name FROM user_tag WHERE username = %s", (self.username,))
        for row in cursor:
            self.tags_view_2.addItem(row[0])

        cursor.execute("SELECT title FROM composer_music, music WHERE composer_music.music_id=music.id and username = %s", (self.username,))
        for row in cursor:
            self.post_music_view_2.addItem(row[0])

        cursor.execute("SELECT title, id FROM playlist WHERE username = %s", (self.username,))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.playlist_view_2.addItem(s)
            self.manage_playlist_2.addItem(s)

        self.manage_playlist_button_2.clicked.connect(self.manage)
        self.delete_ac_button.clicked.connect(self.delete_acc)
        self.change_pass_button.clicked.connect(self.change_pass)

    def delete_acc(self):
        cursor = self.sql_connector.cursor()
        cursor.execute('DELETE FROM user WHERE user.name=%s ', (self.username,))
        self.sql_connector.commit()
        self.parent.parent.setup()
        self.central_widget.setCurrentWidget(self.parent.parent)
        self.central_widget.removeWidget(self)
        del self

    def change_pass(self):
        change_widget = Change_pass(self.username, self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(change_widget)
        self.central_widget.setCurrentWidget(change_widget)

    def manage(self):
        try :
            playlist_name = self.manage_playlist_2.currentText()
            if playlist_name == "":
                raise Exception
            playlist_id = (playlist_name.split("-"))[1]
            self.hide()
            manage_widget = ManagePlayWidget(self.username, playlist_id, self.sql_connector, self.central_widget, self)
            self.central_widget.addWidget(manage_widget)
            self.central_widget.setCurrentWidget(manage_widget)

        except:
            self.error_label_2.setText("No playlist select")


    def add_tag(self):
        cursor = self.sql_connector.cursor()
        cursor.execute("INSERT INTO user_tag VALUES(%s, %s)", (self.username, self.tags_combo.currentText()))
        self.sql_connector.commit()
        self.setup()

    def photo(self):
        image_path = QFileDialog.getOpenFileName()[0]
        self.image_label.setStyleSheet("background-image:url(" + image_path + ")")
        cursor = self.sql_connector.cursor()
        cursor.execute("UPDATE user SET photo_path=%s WHERE name=%s", (image_path, self.username))
        self.sql_connector.commit()


    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

