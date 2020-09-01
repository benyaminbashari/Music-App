from PyQt5 import QtWidgets
from ui.dashboard_form import Ui_dashboard_form
from profile import ProfileWidget
from manage_playlist import ManagePlayWidget
from search import SearchWidget
from first_page import First_page
from follow import FollowWidget
from rate import RateWidget
from like import LikeWidget
from manager_profile import ManagerProfileWidget
import datetime


class DashboardWidget(QtWidgets.QWidget, Ui_dashboard_form):
    def __init__(self, user_name, sql_connector, central_widget, parent=None):
        super(DashboardWidget, self).__init__(parent)
        self.setupUi(self)
        self.username = user_name
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.setup()

    def setup(self):
        self.manage_playlist.clear()
        self.playlist_list.clear()
        self.id_line.clear()
        self.playlist_title_line_2.clear()
        self.playlist_duration_line_2.clear()
        self.playlist_star_line_2.clear()
        self.public_button_2.clearFocus()

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT playlist.title, playlist.id FROM playlist, user WHERE playlist.username=%s", (self.username, ))
        for row in cursor:
            s = row[0] + "-" + str(row[1])
            self.playlist_list.addItem(s)
            self.manage_playlist.addItem(s)

        self.search_button.clicked.connect(self.search)
        self.manage_button.clicked.connect(self.manage)
        self.profile_button.clicked.connect(self.profile)
        self.creat_button_2.clicked.connect(self.create_playlist)
        self.exit_button.clicked.connect(self.exit)
        self.firstPage_button.clicked.connect(self.first_page)
        self.follow_button.clicked.connect(self.foll)
        self.rate_button.clicked.connect(self.rast)
        self.like_button.clicked.connect(self.like)

    def like(self):
        self.hide()
        like_widget = LikeWidget(self.username, self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(like_widget)
        self.central_widget.setCurrentWidget(like_widget)

    def foll(self):
        self.hide()
        follow_widget = FollowWidget(self.username, self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(follow_widget)
        self.central_widget.setCurrentWidget(follow_widget)

    def rast(self):
        self.hide()
        rate_widget = RateWidget(self.username, self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(rate_widget)
        self.central_widget.setCurrentWidget(rate_widget)


    def search(self):
        self.hide()
        search_widget = SearchWidget(self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(search_widget)
        self.central_widget.setCurrentWidget(search_widget)

    def profile(self):

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT type FROM user WHERE name=%s", (self.username, ))
        type = ""
        for row in cursor:
            type = row[0]

        if type == "ordinary" or type == "composer":
            self.hide()
            profile_widget = ProfileWidget(self.username, self.sql_connector, self.central_widget, self)
            self.central_widget.addWidget(profile_widget)
            self.central_widget.setCurrentWidget(profile_widget)

        elif type == "manager":
            self.hide()
            profile_widget = ManagerProfileWidget(self.username, self.sql_connector, self.central_widget, self)
            self.central_widget.addWidget(profile_widget)
            self.central_widget.setCurrentWidget(profile_widget)

    def manage(self):
        try :
            playlist_name = self.manage_playlist.currentText()
            if playlist_name == "":
                raise Exception
            playlist_id = (playlist_name.split("-"))[1]
            self.hide()
            manage_widget = ManagePlayWidget(self.username, playlist_id, self.sql_connector, self.central_widget, self)
            self.central_widget.addWidget(manage_widget)
            self.central_widget.setCurrentWidget(manage_widget)

        except:
            self.error_label.setText("No playlist select")

    def first_page(self):
        self.hide()
        first_widget = First_page(self.username, self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(first_widget)
        self.central_widget.setCurrentWidget(first_widget)

    def create_playlist(self):
        try:
            title = self.playlist_title_line_2.text()
            id = self.id_line.text()
            duration = self.playlist_duration_line_2.text()
            stars = self.playlist_star_line_2.text()
            ty = False

            if self.public_button_2.isChecked():
                ty = True
            else:
                ty = False

            if title == "" or duration == "" or stars == "" or id == "":
                print("12")
                raise Exception

            cursor = self.sql_connector.cursor()
            cursor.execute("INSERT INTO music_list VALUES(%s, %s, %s, %s, %s, %s, %s)", (int(id), title, int(duration), int(stars), self.username, "playlist", ty))
            cursor.execute("INSERT INTO music_list_producer VALUES(%s, %s, %s)", (self.username, int(id), datetime.datetime.now()))

            self.sql_connector.commit()
            self.setup()
            self.error_label_2.setText("Playlist created")

        except:
            self.error_label_2.setText("One field is empty")

    def exit(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self
