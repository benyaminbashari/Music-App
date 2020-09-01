from PyQt5 import QtWidgets
from ui.forget_form import Ui_forget_form
import constants
from error import ErrorWidget


class ForgetWidget(QtWidgets.QWidget, Ui_forget_form):
    def __init__(self, sql_connector, central_widget, parent=None):
        super(ForgetWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.central_widget = central_widget
        self.sql_connector = sql_connector
        self.setup()

    def setup(self):
        self.back_button.clicked.connect(self.back)
        self.ok_button.clicked.connect(self.ok)
        for q in constants.pq:
            self.personal_question.addItem(q)

    def ok(self):
        username = self.username_label.text()
        answer = self.personal_answer.text()
        question = self.personal_question.currentText()
        answer = answer.lower()
        answer = answer.strip()

        ans = ""
        ques = ""
        password = ""

        try:
            cursor = self.sql_connector.cursor()
            cursor.execute("SELECT name, p_question, p_answer, password from user where user.name = %s ", (username, ))
            for row in cursor:
                ques = row[1]
                ans = row[2]
                ans = ans.lower()
                ans = ans.strip()
                password = row[3]

            if question == ques and answer == ans:
                self.hide()
                error_widget = ErrorWidget(self.sql_connector, self.central_widget, "Your password is: " + str(password), True, self)
                self.central_widget.addWidget(error_widget)
                self.central_widget.setCurrentWidget(error_widget)

            else:
                raise Exception
        except:
            self.error_label.setText("Answer or Username is not correct")

    def back(self):
        self.central_widget.setCurrentWidget(self.parent)
        self.central_widget.removeWidget(self)
        del self
