
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(278, 372)
        MainWindow.setStyleSheet("background-color: rgb(194, 219, 238);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ciktiLabel = QtWidgets.QLabel(self.centralwidget)
        self.ciktiLabel.setGeometry(QtCore.QRect(0, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ciktiLabel.setFont(font)
        self.ciktiLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ciktiLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ciktiLabel.setStyleSheet("background-color: rgb(255, 237, 237);")
        self.ciktiLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.ciktiLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ciktiLabel.setLineWidth(1)
        self.ciktiLabel.setMidLineWidth(1)
        self.ciktiLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ciktiLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ciktiLabel.setObjectName("ciktiLabel")
        self.C_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("C"))
        self.C_Button.setGeometry(QtCore.QRect(0, 80, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.C_Button.setFont(font)
        self.C_Button.setStyleSheet("#C_button{ \n""    background-color: rgb(255, 237, 237);\n""   border:none;\n""   border-radius:2px;\n""}\n""\n""")
        self.C_Button.setIconSize(QtCore.QSize(20, 20))
        self.C_Button.setObjectName("C_Button")
        self.kaldirButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.karakter_kaldir())
        self.kaldirButton.setGeometry(QtCore.QRect(70, 80, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.kaldirButton.setFont(font)
        self.kaldirButton.setStyleSheet("#kaldirButton{ \n""    background-color: rgb(255, 237, 237);\n""   border:none;\n""   border-radius:2px;\n""}\n""\n""")
        self.kaldirButton.setIconSize(QtCore.QSize(20, 20))
        self.kaldirButton.setObjectName("kaldirButton")
        self.pozitifnegatifButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.p_n_degisim())
        self.pozitifnegatifButton.setGeometry(QtCore.QRect(140, 80, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pozitifnegatifButton.setFont(font)
        self.pozitifnegatifButton.setStyleSheet("#pozitifnegatifButton{ \n""    background-color: rgb(255, 237, 237);\n""   border:none;\n""   border-radius:2px;\n""}\n""\n""")
        self.pozitifnegatifButton.setIconSize(QtCore.QSize(30, 30))
        self.pozitifnegatifButton.setObjectName("pozitifnegatifButton")
        self.yuzdeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("%"))
        self.yuzdeButton.setGeometry(QtCore.QRect(210, 80, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yuzdeButton.setFont(font)
        self.yuzdeButton.setStyleSheet("#yuzdeButton{ \n""    background-color: rgb(255, 237, 237);\n""   border:none;\n""   border-radius:2px;\n""}\n""\n""")
        self.yuzdeButton.setIconSize(QtCore.QSize(20, 20))
        self.yuzdeButton.setObjectName("yuzdeButton")
        self.yediButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("7"))
        self.yediButton.setGeometry(QtCore.QRect(0, 140, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yediButton.setFont(font)
        self.yediButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.yediButton.setObjectName("yediButton")
        self.dokuzButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("9"))
        self.dokuzButton.setGeometry(QtCore.QRect(140, 140, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dokuzButton.setFont(font)
        self.dokuzButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.dokuzButton.setObjectName("dokuzButton")
        self.sekizButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("8"))
        self.sekizButton.setGeometry(QtCore.QRect(70, 140, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sekizButton.setFont(font)
        self.sekizButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.sekizButton.setObjectName("sekizButton")
        self.bolmeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("/"))
        self.bolmeButton.setGeometry(QtCore.QRect(210, 140, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bolmeButton.setFont(font)
        self.bolmeButton.setStyleSheet("#bolmeButton{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"")
        self.bolmeButton.setIconSize(QtCore.QSize(20, 20))
        self.bolmeButton.setObjectName("bolmeButton")
        self.dortButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.tikla("4"))
        self.dortButton.setGeometry(QtCore.QRect(0, 200, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dortButton.setFont(font)
        self.dortButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.dortButton.setObjectName("dortButton")
        self.altiButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("6"))
        self.altiButton.setGeometry(QtCore.QRect(140, 200, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.altiButton.setFont(font)
        self.altiButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.altiButton.setObjectName("altiButton")
        self.besButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("5"))
        self.besButton.setGeometry(QtCore.QRect(70, 200, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.besButton.setFont(font)
        self.besButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.besButton.setObjectName("besButton")
        self.carpmaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("*"))
        self.carpmaButton.setGeometry(QtCore.QRect(210, 200, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.carpmaButton.setFont(font)
        self.carpmaButton.setStyleSheet("#carpmaButton{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"")
        self.carpmaButton.setIconSize(QtCore.QSize(20, 20))
        self.carpmaButton.setAutoRepeatDelay(301)
        self.carpmaButton.setObjectName("carpmaButton")
        self.birButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("1"))
        self.birButton.setGeometry(QtCore.QRect(0, 260, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.birButton.setFont(font)
        self.birButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.birButton.setObjectName("birButton")
        self.ucButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("3"))
        self.ucButton.setGeometry(QtCore.QRect(140, 260, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ucButton.setFont(font)
        self.ucButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.ucButton.setObjectName("ucButton")
        self.ikiButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("2"))
        self.ikiButton.setGeometry(QtCore.QRect(70, 260, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ikiButton.setFont(font)
        self.ikiButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.ikiButton.setObjectName("ikiButton")
        self.eksiButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("-"))
        self.eksiButton.setGeometry(QtCore.QRect(210, 260, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.eksiButton.setFont(font)
        self.eksiButton.setStyleSheet("#eksiButton{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"")
        self.eksiButton.setObjectName("eksiButton")
        self.sifirButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.tikla("0"))
        self.sifirButton.setGeometry(QtCore.QRect(0, 320, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sifirButton.setFont(font)
        self.sifirButton.setStyleSheet("#C_button{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"#C_button:hover{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 196, 214, 209), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"#C_button:pressed{\n"
"   padding-left: 5px;\n"
"   padding-top: 5px;\n"
"\n"
"}\n"
" ")
        self.sifirButton.setObjectName("sifirButton")
        self.esittirButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.matematik())
        self.esittirButton.setGeometry(QtCore.QRect(140, 320, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.esittirButton.setFont(font)
        self.esittirButton.setStyleSheet("#esittirButton{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"")
        self.esittirButton.setObjectName("esittirButton")
        self.noktaButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.nokta())
        self.noktaButton.setGeometry(QtCore.QRect(70, 320, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.noktaButton.setFont(font)
        self.noktaButton.setStyleSheet("#QPushButton{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"")
        self.noktaButton.setObjectName("noktaButton")
        self.artiButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.tikla("+"))
        self.artiButton.setGeometry(QtCore.QRect(210, 320, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.artiButton.setFont(font)
        self.artiButton.setStyleSheet("#artiButton{ \n"
"    background-color: rgb(255, 237, 237);\n"
"   border:none;\n"
"   border-radius:2px;\n"
"}\n"
"\n"
"")
        self.artiButton.setObjectName("artiButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Karakteri kaldır
    def karakter_kaldir(self):
        # Ekranda olanı  al
        ekran1 = self.ciktiLabel.text()
        # liste dizesindeki son öğeyi kaldır
        ekran1 = ekran1[:-1]
        # ekrana geri çıktı
        self.ciktiLabel.setText(ekran1)



    def matematik(self):
        # Ekranda olanı al
        ekran1 = self.ciktiLabel.text()
        try:      #try bir kod blogunu hatalar için test eder.
            #Matematik yap
            cevap1 = eval(ekran1)   #eval = Python komutları içeren bir dizeyi yorumlayıcıya gönderir ve sonucu geri verir.
            self.ciktiLabel.setText(str(cevap1))
        except:   #Hatayı işlemeye izin verir
            #Ekrana cıkış hatası
            self.ciktiLabel.setText("ERROR")



    # pozitif/negatif değişiklik
    def p_n_degisim(self):
        ekran1 = self.ciktiLabel.text()
        if "-" in ekran1:
            self.ciktiLabel.setText(ekran1.replace("-","")) #Yer değiştiriyor
        else:
            self.ciktiLabel.setText(f'-{ekran1}')



    def nokta1(self):
            # Ekranda olanı al
            ekran1 = self.ciktiLabel.text()
            if ekran1[-1] == ".":
                pass
            else:
                self.ciktiLabel.setText(f'{ekran1}')


    def tikla(self, bas):

        if bas == "C":
                self.ciktiLabel.setText("0")
                #O ile başlayıp başlamadığını kontrol et ve 0 ı sil
        else:
                if self.ciktiLabel.text() == "0":
                    self.ciktiLabel.setText("")
                    #basılan tuşu orada olanla birleştir.
                self.ciktiLabel.setText(f'{self.ciktiLabel.text()}{bas}')

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.ciktiLabel.setText(_translate("MainWindow", "0"))
            self.C_Button.setText(_translate("MainWindow", "C"))
            self.kaldirButton.setText(_translate("MainWindow", "<<"))
            self.pozitifnegatifButton.setText(_translate("MainWindow", "+/-"))
            self.yuzdeButton.setText(_translate("MainWindow", "%"))
            self.yediButton.setText(_translate("MainWindow", "7"))
            self.dokuzButton.setText(_translate("MainWindow", "9"))
            self.sekizButton.setText(_translate("MainWindow", "8"))
            self.bolmeButton.setText(_translate("MainWindow", "/"))
            self.dortButton.setText(_translate("MainWindow", "4"))
            self.altiButton.setText(_translate("MainWindow", "6"))
            self.besButton.setText(_translate("MainWindow", "5"))
            self.carpmaButton.setText(_translate("MainWindow", "*"))
            self.birButton.setText(_translate("MainWindow", "1"))
            self.ucButton.setText(_translate("MainWindow", "3"))
            self.ikiButton.setText(_translate("MainWindow", "2"))
            self.eksiButton.setText(_translate("MainWindow", "-"))
            self.sifirButton.setText(_translate("MainWindow", "0"))
            self.esittirButton.setText(_translate("MainWindow", "="))
            self.noktaButton.setText(_translate("MainWindow", "."))
            self.artiButton.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
