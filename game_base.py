from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from collections import deque
from random import choice


class Ui_TicTacToe(object):
    def setupUi(self, TicTacToe):
        TicTacToe.setObjectName("TicTacToe")
        TicTacToe.resize(420, 480)
        self.centralwidget = QtWidgets.QWidget(TicTacToe)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 238, 102);\n"
"background-color: rgb(128, 0, 128);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_1.setGeometry(QtCore.QRect(0, 40, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_1_1.setFont(font)
        self.btn_1_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_1_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_1_1.setAutoFillBackground(False)
        self.btn_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_1_1.setText("")
        self.btn_1_1.setObjectName("btn_1_1")
        self.btn_1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_2.setGeometry(QtCore.QRect(140, 40, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_1_2.setFont(font)
        self.btn_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_1_2.setText("")
        self.btn_1_2.setObjectName("btn_1_2")
        self.btn_1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_3.setGeometry(QtCore.QRect(280, 40, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_1_3.setFont(font)
        self.btn_1_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_1_3.setText("")
        self.btn_1_3.setObjectName("btn_1_3")
        self.btn_2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_1.setGeometry(QtCore.QRect(0, 180, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_2_1.setFont(font)
        self.btn_2_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_2_1.setText("")
        self.btn_2_1.setObjectName("btn_2_1")
        self.btn_2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_2.setGeometry(QtCore.QRect(140, 180, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_2_2.setFont(font)
        self.btn_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_2_2.setText("")
        self.btn_2_2.setObjectName("btn_2_2")
        self.btn_2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_3.setGeometry(QtCore.QRect(280, 180, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_2_3.setFont(font)
        self.btn_2_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_2_3.setText("")
        self.btn_2_3.setObjectName("btn_2_3")
        self.btn_3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3_1.setGeometry(QtCore.QRect(0, 320, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_3_1.setFont(font)
        self.btn_3_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_3_1.setText("")
        self.btn_3_1.setObjectName("btn_3_1")
        self.btn_3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3_2.setGeometry(QtCore.QRect(140, 320, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_3_2.setFont(font)
        self.btn_3_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_3_2.setText("")
        self.btn_3_2.setObjectName("btn_3_2")
        self.btn_3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3_3.setGeometry(QtCore.QRect(280, 320, 140, 140))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.btn_3_3.setFont(font)
        self.btn_3_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_3_3.setText("")
        self.btn_3_3.setObjectName("btn_3_3")
        TicTacToe.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TicTacToe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        TicTacToe.setMenuBar(self.menubar)
        self.btn_reset = QtWidgets.QAction(TicTacToe)
        self.btn_reset.setObjectName("btn_reset")
        self.btn_hint = QtWidgets.QAction(TicTacToe)
        self.btn_hint.setObjectName("btn_hint")
        self.btn_wins = QtWidgets.QAction(TicTacToe)
        self.btn_wins.setObjectName("btn_wins")
        self.menuGame.addAction(self.btn_reset)
        self.menuGame.addAction(self.btn_wins)
        self.menuGame.addAction(self.btn_hint)
        self.menubar.addAction(self.menuGame.menuAction())

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

        self.number_of_wins = 0
        self.number_of_loses = 0
        self.end_game = False
        self.afterHint = False
        self.count = 0
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.check = [[[1, 1], [1, 2], [1, 3]], [[2, 1], [2, 2], [2, 3]], [[3, 1], [3, 2], [3, 3]],
                      [[1, 1], [2, 1], [3, 1]], [[1, 2], [2, 2], [3, 2]], [[1, 3], [2, 3], [3, 3]],
                      [[1, 1], [2, 2], [3, 3]], [[1, 3], [2, 2], [3, 1]]]
        self.who_is_first()

        self.add_functions()

    def retranslateUi(self, TicTacToe):
        self._translate = QtCore.QCoreApplication.translate
        TicTacToe.setWindowTitle(self._translate("TicTacToe", "MainWindow"))
        self.label.setText(self._translate("TicTacToe", "Good luck!"))
        self.menuGame.setTitle(self._translate("TicTacToe", "Game"))
        self.btn_reset.setText(self._translate("TicTacToe", "reset"))
        self.btn_reset.setShortcut(self._translate("TicTacToe", "Ctrl+R"))
        self.btn_hint.setText(self._translate("TicTacToe", "hint"))
        self.btn_hint.setShortcut(self._translate("TicTacToe", "Ctrl+H"))
        self.btn_wins.setText(self._translate("TicTacToe", "number of wins"))
        self.btn_wins.setShortcut(self._translate("TicTacToe", "Ctrl+W"))

    def add_functions(self):

        self.btn_reset.triggered.connect(lambda: self.action_btn(self.btn_reset.text()))
        self.btn_hint.triggered.connect(lambda: self.action_btn(self.btn_hint.text()))
        self.btn_wins.triggered.connect(lambda: self.action_btn(self.btn_wins.text()))
        self.btn_1_1.clicked.connect(lambda: self.write_sign(self.btn_1_1.text(), 1, 1))
        self.btn_1_2.clicked.connect(lambda: self.write_sign(self.btn_1_2.text(), 1, 2))
        self.btn_1_3.clicked.connect(lambda: self.write_sign(self.btn_1_3.text(), 1, 3))
        self.btn_2_1.clicked.connect(lambda: self.write_sign(self.btn_2_1.text(), 2, 1))
        self.btn_2_2.clicked.connect(lambda: self.write_sign(self.btn_2_2.text(), 2, 2))
        self.btn_2_3.clicked.connect(lambda: self.write_sign(self.btn_2_3.text(), 2, 3))
        self.btn_3_1.clicked.connect(lambda: self.write_sign(self.btn_3_1.text(), 3, 1))
        self.btn_3_2.clicked.connect(lambda: self.write_sign(self.btn_3_2.text(), 3, 2))
        self.btn_3_3.clicked.connect(lambda: self.write_sign(self.btn_3_3.text(), 3, 3))

    def write_sign(self, text, row, col):

        def is_win_or_pot(res):
            potential = deque()
            empty_list = []

            for strike in self.check:
                human = 0
                bot = 0
                empty = 0
                for cor in strike:
                    r, c = cor
                    if self.grid[r - 1][c - 1] == 1:
                        human += 1
                    elif self.grid[r - 1][c - 1] == 2:
                        bot += 1
                    else:
                        empty_cor = [r, c]
                        empty_list.append(empty_cor)
                        empty += 1
                if human == 3:
                    self.label.setText("You won! 😁")
                    self.number_of_wins += 1
                    self.end_game = True
                    return
                elif bot == 3:
                    self.label.setText("You lost! 😢")
                    self.number_of_loses += 1
                    self.end_game = True
                    return
                else:
                    if empty == 1:
                        if bot == 2:
                            potential.appendleft(empty_cor)
                        elif human == 2:
                            potential.append(empty_cor)
            if not res:
                if not potential:
                    return choice(empty_list)
                else:
                    return potential[0]
            elif res and self.count == 9:
                self.label.setText("Draw, friendship won! 🤝🍉")
                self.end_game = True

        def bot_turn():
            self.count += 1
            r, c = is_win_or_pot('')
            self.grid[r - 1][c - 1] = 2
            if self.first == 'bot':
                signal = 'X'
            else: signal = 'O'
            self.cor_to_btn(r, c, signal)
            is_win_or_pot('is there any winner?')

        if text == '' and not self.end_game:
            self.count += 1
            self.grid[row - 1][col - 1] = 1
            if self.first == 'human':
                signal = 'X'
            else: signal = 'O'
            self.cor_to_btn(row, col, signal)

            is_win_or_pot('is there any winner?')
            if not self.end_game: bot_turn()

    def action_btn(self, page):
        if page == 'reset':
            self.end_game = False
            self.count = 0
            self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            if self.afterHint:
                self.label.setText(self._translate("TicTacToe", "Try the hint!"))
            else: self.label.setText(self._translate("TicTacToe", "Good luck!"))
            self.afterHint = False

            self.btn_1_1.setText('')
            self.btn_1_2.setText('')
            self.btn_1_3.setText('')
            self.btn_2_1.setText('')
            self.btn_2_2.setText('')
            self.btn_2_3.setText('')
            self.btn_3_1.setText('')
            self.btn_3_2.setText('')
            self.btn_3_3.setText('')

            self.who_is_first()
        elif page == "number of wins":
            s = self.number_of_wins
            if s == 1:
                self.label.setText('You won ' + str(self.number_of_wins) + ' time! And lost ' +
                                   str(self.number_of_loses))
            else:
                self.label.setText('You won ' + str(self.number_of_wins) + ' times! And lost ' +
                                   str(self.number_of_loses))
        elif page == "hint":
            print('hint')
            hint = QMessageBox()
            hint.setWindowTitle("Hint for a player")
            hint.setText("Here is a secret way to beat the smart bot:")
            hint.setIcon(QMessageBox.Information)
            hint.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
            hint.setDefaultButton(QMessageBox.Ok)

            hint.setInformativeText('Click "Show details"')
            hint.setDetailedText("It is allways draw, unless you mark the center first. "
                                 "Then, the bot chooses an adjacent square. Further, "
                                 "just choose corners, and you will win!")

            hint.buttonClicked.connect(self.popup_action)

            hint.exec_()

    def popup_action(self, btn):
        if btn.text() == "Reset":
            self.afterHint = True
            self.action_btn('reset')



    def cor_to_btn(self, row, col, sign):
        if row == 1:
            if col == 1:
                self.btn_1_1.setText(sign)
                if sign == 'X':
                    self.btn_1_1.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_1_1.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
            elif col == 2:
                self.btn_1_2.setText(sign)
                if sign == 'X':
                    self.btn_1_2.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_1_2.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
            elif col == 3:
                self.btn_1_3.setText(sign)
                if sign == 'X':
                    self.btn_1_3.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_1_3.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
        if row == 2:
            if col == 1:
                self.btn_2_1.setText(sign)
                if sign == 'X':
                    self.btn_2_1.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_2_1.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
            elif col == 2:
                self.btn_2_2.setText(sign)
                if sign == 'X':
                    self.btn_2_2.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_2_2.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
            elif col == 3:
                self.btn_2_3.setText(sign)
                if sign == 'X':
                    self.btn_2_3.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_2_3.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
        if row == 3:
            if col == 1:
                self.btn_3_1.setText(sign)
                if sign == 'X':
                    self.btn_3_1.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_3_1.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
            elif col == 2:
                self.btn_3_2.setText(sign)
                if sign == 'X':
                    self.btn_3_2.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_3_2.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")
            elif col == 3:
                self.btn_3_3.setText(sign)
                if sign == 'X':
                    self.btn_3_3.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(255, 0, 0);")
                elif sign == "O":
                    self.btn_3_3.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 255);")

    def who_is_first(self):
        self.first = choice(['human', 'bot'])
        if self.first == 'bot':
            self.count += 1
            a, b = choice([1, 2, 3]), choice([1, 2, 3])
            self.grid[a - 1][b - 1] = 2
            self.cor_to_btn(a, b, 'X')









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TicTacToe = QtWidgets.QMainWindow()
    ui = Ui_TicTacToe()
    ui.setupUi(TicTacToe)
    TicTacToe.show()
    sys.exit(app.exec_())