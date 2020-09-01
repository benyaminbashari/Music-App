from PyQt5 import QtWidgets
from ui.change_pass_form import Ui_change_pass_form
import re


class Change_pass(QtWidgets.QWidget, Ui_change_pass_form):
    def __init__(self, username, sql_connector, central_widget, parent=None):
        super(Change_pass, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.username = username
        self.setup()

    def setup(self):

        self.ok_button.clicked.connect(self.ok)
        self.back_button.clicked.connect(self.back)

    def ok(self):
        old_pass = self.curren_pass_line.text()
        new_pass = self.new_pass_line.text()

        try:
            cursor = self.sql_connector.cursor()
            cursor.execute("SELECT password FROM user where name = %s", (self.username,))
            password = ""

            for row in cursor:
                password = row[0]

            if old_pass != password:
                raise Exception

            if len(new_pass) >= 8 and bool(re.search(r'\d', password)) and bool(re.search(r'\D', password)):
                cursor.execute('UPDATE user SET password=%s WHERE name=%s', (new_pass, self.username))
                self.sql_connector.commit()
                self.back()
            else:
                raise Exception

        except:
            self.error_label.setText("Old password is wrong or password is not qualified")

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self