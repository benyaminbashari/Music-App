"""
name the object as XXX_form
save the file as XXX.ui
compile with XXX_form.ui
"""

from PyQt5 import QtWidgets
from ui.rate_form import Ui_rate_form


class RateWidget(QtWidgets.QWidget, Ui_rate_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(RateWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):
        self.album_list.clear()
        self.album_combo.clear()
        self.fol_list.clear()

        self.back_button.clicked.connect(self.back)
        self.rate_button.clicked.connect(self.rate)
        self.follow_button.clicked.connect(self.fol)

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id, stars FROM music_list")
        for row in cursor:
            self.album_list.addItem(row[0] + " - " + str(row[1])+" - Stars:" + str(row[2]))

        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT title, id FROM music_list")
        for row in cursor:
            self.album_combo.addItem(row[0] + "-" + str(row[1]))

        #cursor.execute("SELECT music_list_id FROM music_list_follow WHERE username=%s", (self.username, ))
        cursor.execute("SELECT music_list.title, music_list.id FROM music_list, music_list_follow WHERE music_list.id=music_list_follow.music_list_id and music_list_follow.username=%s", (self.username, ))
        for row in cursor:
            self.fol_list.addItem(row[0] + "-" + str(row[1]))
            #self.fol_list.addItem(str(row[0]))


    def rate(self):
        id = int(self.album_combo.currentText().split('-')[1])
        cursor = self.sql_connector.cursor()
        cursor.execute("UPDATE music_list set stars=%s WHERE id=%s", (int(self.star_line.text()), id))
        self.sql_connector.commit()
        self.setup()

    def fol(self):
        id = int(self.album_combo.currentText().split('-')[1])
        cursor = self.sql_connector.cursor()
        cursor.execute("INSERT INTO music_list_follow VALUES(%s, %s)", (self.username, id))
        self.sql_connector.commit()
        self.setup()

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self

