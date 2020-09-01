from PyQt5 import QtWidgets
from ui.login_form import Ui_login_form
from register import RegisterWidget
from forget import ForgetWidget
from dashboard import DashboardWidget


class LoginWidget(QtWidgets.QWidget, Ui_login_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(LoginWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.image_label.setStyleSheet("background-image:url(./music_spot.jpeg)")
        self.setup()

    def setup(self):
        self.username_line.clear()
        self.password_line.clear()
        cursor = self.sql_connector.cursor()
        cursor.execute("SELECT count(name) FROM user")
        user_cnt = 0
        songs_cnt = 0
        for row in cursor:
            user_cnt = row[0]

        cursor.execute("SELECT count(id) FROM music")
        for row in cursor:
            songs_cnt = row[0]

        self.user_number_label.setText(str(user_cnt))
        self.songs_number_label.setText(str(songs_cnt))
        self.register_button.clicked.connect(self.reg_button)
        self.forgot_button.clicked.connect(self.forget_button)
        self.sign_button.clicked.connect(self.sign_in_button)

    def reg_button(self):
        self.hide()
        register_widget = RegisterWidget(self.sql_connector ,self.central_widget, self)
        self.central_widget.addWidget(register_widget)
        self.central_widget.setCurrentWidget(register_widget)


    def forget_button(self):
        self.hide()
        forget_widget = ForgetWidget(self.sql_connector, self.central_widget, self)
        self.central_widget.addWidget(forget_widget)
        self.central_widget.setCurrentWidget(forget_widget)

    def sign_in_button(self):
        try:
            username_enter = self.username_line.text()
            password_enter = self.password_line.text()

            cursor = self.sql_connector.cursor()
            cursor.execute("SELECT name, password FROM user where name = %s", (username_enter,))
            username = ""
            password = ""

            for row in cursor:
                username = row[0]
                password = row[1]

            if username != username_enter:
                raise Exception

            if username == username_enter and password == password_enter:
                self.hide()
                dashboard_widget = DashboardWidget(username, self.sql_connector, self.central_widget, self)
                self.central_widget.addWidget(dashboard_widget)
                self.central_widget.setCurrentWidget(dashboard_widget)
            else :
                raise Exception

        except:
            self.error_label.setText("Username or password is wrong!")


