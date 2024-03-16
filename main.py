import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QGridLayout, QFrame, QMessageBox,QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from questions import dict_questions

questions = dict_questions()
QUESTION_COUNT = len(questions)

class Button(QPushButton):
    def __init__(self, caption: str, text_size=14, parent=None):
        super().__init__(caption, parent)
        self.setStyleSheet(f"""
        background-color: #101820;
        color: #FEE715;
        font-size: {text_size}px;
        border-radius: 5px;
        padding: 7px;
        """)

class RButton(QRadioButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("font-family: Times New Roman;")
        
class Label(QLabel):
    def __init__(self, text: str, text_size=14, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(f"""
        color: #101820;
        font-size: {text_size}px;
        font-family: Times New Roman;
        """)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QuizApp')
        self.setWindowIcon(QIcon('quiz.png'))
        self.setGeometry(700, 300, 900, 500)
        self.setStyleSheet("""
            background-color: #FEE715;
        """)

        self.list_Rbuttons = []
        self.index = 0
        self.score_count = 0
        self.correct_answer = questions[self.index]['correct_answer']

        self.score_label = Label('You have got 0 correct answers out of 0 so far', 20)
        self.question_label = Label(questions[self.index]['question'], 20)
        self.question_label.setStyleSheet("color: white")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLabel)

        self.remaining_time = Label('Remaining time for the question: 3 minutes', 20)

        self.timer.start(1000)

        self.countdown_time = 180

        self.prev_button = Button('Previous', 20)
        self.next_button = Button('Next', 20,)

        self.next_button.clicked.connect(self.next_pressed)
        self.prev_button.clicked.connect(self.prev_pressed)

        self.main_grid = QGridLayout(self)
        self.setLayout(self.main_grid)

        self.left_grid = QGridLayout(self)
        self.opt_form = QFrame(self)
        self.opt_form.setStyleSheet("""background-color: #101820;
                                    border-radius: 10px;
                                    font-size: 20px;
                                    color: #FEE715;
                                    padding: 5px
                                    """)

        self.options_grid = QGridLayout(self.opt_form)

        self.options_grid.addWidget(self.question_label, 0, 0)
        self.get_question()
        self.index += 1

        self.main_grid.addLayout(self.left_grid, 0, 0)
        self.left_grid.addWidget(self.score_label, 0, 0)
        self.left_grid.addWidget(self.opt_form, 1, 0)

        self.button_lay = QVBoxLayout()
        self.button_lay.addWidget(self.prev_button)
        self.button_lay.addWidget(self.next_button)

        self.left_grid.addLayout(self.button_lay, 2, 0)
        self.left_grid.addWidget(self.remaining_time, 3, 0)

        self.show()

    def updateLabel(self):
        minutes = self.countdown_time // 60
        seconds = self.countdown_time % 60
        self.remaining_time.setText(f'Remaining time for the quiz: {minutes:02d}:{seconds:02d}')
        self.countdown_time -= 1

        if self.countdown_time < 0:
            self.showMessageBox('Time is up!', f'Your time is up: Correct answers: {self.score_count}')
            self.timer.stop()

    def showMessageBox(self, window_title, text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(window_title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)
        result = msgBox.exec_()
        if result == QMessageBox.Ok:
            print('Ok button clicked')
        elif result == QMessageBox.Cancel:
            print('Cancel button clicked')

    def get_question(self):
        if self.index == len(questions)-1:
            self.next_button.setText("Finish")
            self.question_label.setText('You finished the quiz!')      
            return

        self.question_label.setText(questions[self.index]['question'])
        for i in range(len(questions[self.index]['answers'])):
            temp = RButton(questions[self.index]['answers'][f'answer_{chr(i+97)}'])
            self.options_grid.addWidget(temp, i+1, 0)
            self.list_Rbuttons.append(temp)
        print(self.index)
        self.correct_answer = questions[self.index]['correct_answer']

    def next_pressed(self):
        isChecked = [True for x in self.list_Rbuttons if x.isChecked()]
        print(self.correct_answer)

        if self.index < len(questions):  # Use len(questions) instead of QUESTION_COUNT
            if any(isChecked):
                user_answer = [self.list_Rbuttons[i] for i in range(len(self.list_Rbuttons)) if self.list_Rbuttons[i].isChecked()]

                if user_answer[0].text() == self.correct_answer:
                    if not questions[self.index]['answered']:
                        self.score_count += 1
                    self.score_label.setText(f'You have got {str(self.score_count)} correct answers out of {self.index+1} so far')
                else:
                    self.score_label.setText(f'You have got {str(self.score_count)} correct answers out of {self.index+1} so far')

                questions[self.index]['answered'] = True
                self.list_Rbuttons = []
                for i in reversed(range( 1, self.options_grid.count())):
                    self.options_grid.itemAt(i).widget().setParent(None)

                self.index += 1
                if self.index < len(questions):
                    self.get_question()
            else:
                self.showMessageBox('', 'An option must be chosen!')

        else:
            pass


    def prev_pressed(self):
        if self.index > 0:
            for i in reversed(range(1, self.options_grid.count())):
                self.options_grid.itemAt(i).widget().setParent(None)

            self.index -= 1
            self.get_question()

if __name__ == '__main__':
    app = QApplication([])
    mw = MainWindow()
    sys.exit(app.exec_())
