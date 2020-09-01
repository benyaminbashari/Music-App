from PyQt5 import QtWidgets
from ui.register_form import Ui_register_form
from PyQt5.QtWidgets import QFileDialog
import re
import constants


class RegisterWidget(QtWidgets.QWidget, Ui_register_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(RegisterWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.image = None
        self.setup()

    def setup(self):
        self.back_button.clicked.connect(self.back)
        self.reg_button.clicked.connect(self.register)
        for q in constants.pq:
            self.pq_combo.addItem(q)
        self.ordinary_check.setChecked(True)
        self.ordinary_check.clicked.connect(self.ord_check)
        self.composer_check.clicked.connect(self.compo_check)
        self.photo_button.clicked.connect(self.select_file)

    def ord_check(self):
        if self.ordinary_check.isChecked():
            pass
        self.ordinary_check.setChecked(True)
        self.composer_check.setChecked(False)

    def compo_check(self):
        if self.composer_check.isChecked():
            pass
        self.ordinary_check.setChecked(False)
        self.composer_check.setChecked(True)

    def select_file(self):
        self.image = QFileDialog.getOpenFileName()[0]

    def register(self):
        username = self.username_line.text()
        password = self.password_line.text()
        email = self.email_line.text()
        pq = self.pq_combo.currentText()
        pa = self.pa_line.text()
        ty = ''

        if self.composer_check.isChecked():
            ty = 'composer'
        else:
            ty = 'ordinary'
        try:
            cursor = self.sql_connector.cursor()

            if len(password) >= 8 and bool(re.search(r'\d', password)) and bool(re.search(r'\D', password)):
                cursor.execute("INSERT INTO user VALUES(%s, %s, %s, %s, %s, %s, %s)",
                               (username, email, password, pq, pa, self.image, ty))
                self.sql_connector.commit()
                self.back()
            else:
                raise Exception

        except:
            if not bool(re.search(r'\d', password)) or not bool(re.search(r'\D', password)) or len(password) <= 8:
                self.error_label.setText('Password is not qualified')
            else:
                self.error_label.setText('Username already exist')

    def back(self):
        self.parent.setup()
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self
