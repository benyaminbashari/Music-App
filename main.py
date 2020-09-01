from PyQt5 import QtWidgets
from login import LoginWidget
import mysql.connector as mariadb


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, sql_connector, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = LoginWidget(sql_connector, self.central_widget, self)
        self.central_widget.addWidget(login_widget)
        self.sql_connector = sql_connector


if __name__ == '__main__':
    mariadb_connection = mariadb.connect(user='user1', password='user1', database='music_spot')
    app = QtWidgets.QApplication([])
    window = MainWindow(mariadb_connection)
    window.show()
    app.exec_()


