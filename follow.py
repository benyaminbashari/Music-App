"""
name the object as XXX_form
save the file as XXX.ui
compile with XXX_form.ui
"""

from PyQt5 import QtWidgets
from ui.follow_form import Ui_follow_form


class FollowWidget(QtWidgets.QWidget, Ui_follow_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(FollowWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):
        self.followers_list.clear()
        self.followings_list.clear()
        self.users_list.clear()
        self.followable_combo.clear()
        self.back_button.clicked.connect(self.back)
        self.follow_button.clicked.connect(self.fol)
        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT follower FROM user_follow WHERE following=%s", (self.username,))
        for row in cursor:
            self.followers_list.addItem(row[0])

        users = []
        foll = set()
        cursor.execute("SELECT following FROM user_follow WHERE follower=%s", (self.username,))
        for row in cursor:
            self.followings_list.addItem(row[0])
            foll.add(row[0])

        cursor.execute("SELECT name FROM user")
        for row in cursor:
            self.users_list.addItem(row[0])
            users.append(row[0])

        for user in users:
            if user not in foll and user != self.username:
                self.followable_combo.addItem(user)

    def fol(self):
        cursor = self.sql_connector.cursor()
        print("HERE", self.username, self.followable_combo.currentText())
        cursor.execute("INSERT into user_follow VALUES(%s, %s)", (self.username, self.followable_combo.currentText()))
        self.sql_connector.commit()
        self.setup()

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

