import openpyxl, sys
from PyQt5 import QtCore, QtGui, QtWidgets

book = openpyxl.open("03_04_2022_PRM.xlsx", read_only=True)
sheet = book.active
maszna4 = []  # массив для сортировки переменный


# метод пузырьковой сортировки
def bubble(list_nums):
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for i in range(len(list_nums) - 1):
            if list_nums[i] > list_nums[i + 1]:
                list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
                swap_bool = True


# метод перамидальной
def heapify(sort_nums, heap_size, root):
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[l]:
        l = left
    if right < heap_size and sort_nums[right] > sort_nums[l]:
        l = right
    if l != root:
        sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
        heapify(sort_nums, heap_size, l)
def heap(sort_nums):
    size = len(sort_nums)
    for i in range(size, -1, -1):
        heapify(sort_nums, size, i)
    for i in range(size - 1, 0, -1):
        sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
        heapify(sort_nums, i, 0)


# метод слияния
def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSort(nums[:mid+1])
    lst2 = mergeSort(nums[mid+1:])
    result = merge(lst1, lst2)
    return result
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 340)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_mtd = QtWidgets.QLabel(self.centralwidget)
        self.label_mtd.setGeometry(QtCore.QRect(20, 10, 120, 22))
        self.label_mtd.setObjectName("label_mtd")
        self.pB_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pB_exit.setGeometry(QtCore.QRect(515, 300, 75, 22))
        self.pB_exit.setObjectName("pB_exit")
        self.hS = QtWidgets.QSlider(self.centralwidget)
        self.hS.setGeometry(QtCore.QRect(10, 130, 580, 22))
        self.hS.setMouseTracking(True)
        self.hS.setTabletTracking(False)
        self.hS.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.hS.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.hS.setAcceptDrops(False)
        self.hS.setAutoFillBackground(False)
        self.hS.setInputMethodHints(QtCore.Qt.ImhNone)
        self.hS.setMinimum(0)
        self.hS.setMaximum(100)
        self.hS.setPageStep(100)
        self.hS.setProperty("value", 50)
        self.hS.setSliderPosition(50)
        self.hS.setOrientation(QtCore.Qt.Horizontal)
        self.hS.setInvertedAppearance(False)
        self.hS.setInvertedControls(False)
        self.hS.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.hS.setTickInterval(10)
        self.hS.setObjectName("hS")
        self.label_s_txt = QtWidgets.QLabel(self.centralwidget)
        self.label_s_txt.setGeometry(QtCore.QRect(40, 90, 171, 16))
        self.label_s_txt.setObjectName("label_s_txt")
        self.tb_out = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_out.setGeometry(QtCore.QRect(10, 200, 580, 91))
        self.tb_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tb_out.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tb_out.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tb_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tb_out.setReadOnly(False)
        self.tb_out.setObjectName("tb_out")
        self.label_out_TB = QtWidgets.QLabel(self.centralwidget)
        self.label_out_TB.setGeometry(QtCore.QRect(158, 170, 230, 20))
        self.label_out_TB.setObjectName("label_out_TB")
        self.label_s = QtWidgets.QLabel(self.centralwidget)
        self.label_s.setGeometry(QtCore.QRect(20, 50, 150, 22))
        self.label_s.setObjectName("label_s")
        self.pB_vvod = QtWidgets.QPushButton(self.centralwidget)
        self.pB_vvod.setGeometry(QtCore.QRect(425, 300, 75, 23))
        self.pB_vvod.setObjectName("pB_vvod")
        self.l_out_hS = QtWidgets.QLabel(self.centralwidget)
        self.l_out_hS.setGeometry(QtCore.QRect(250, 90, 31, 16))
        self.l_out_hS.setObjectName("l_out_hS")
        self.cB_column = QtWidgets.QComboBox(self.centralwidget)
        self.cB_column.setGeometry(QtCore.QRect(230, 50, 69, 22))
        self.cB_column.setObjectName("cB_column")
        self.cB_column.addItem("")
        self.cB_column.addItem("")
        self.cB_column.addItem("")
        self.cB_mtd = QtWidgets.QComboBox(self.centralwidget)
        self.cB_mtd.setGeometry(QtCore.QRect(180, 10, 121, 22))
        self.cB_mtd.setObjectName("cB_mtd")
        self.cB_mtd.addItem("")
        self.cB_mtd.addItem("")
        self.cB_mtd.addItem("")
        self.l_author = QtWidgets.QLabel(self.centralwidget)
        self.l_author.setGeometry(QtCore.QRect(430, 0, 161, 71))
        self.l_author.setObjectName("l_author")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pB_exit.clicked.connect(MainWindow.close)
        self.hS.valueChanged['int'].connect(self.l_out_hS.setNum)
        self.cB_column.currentIndexChanged['QString'].connect(self._click_column)
        self.cB_mtd.currentIndexChanged['QString'].connect(self._click_mtd)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алгоритм сортировки"))
        self.label_mtd.setText(_translate("MainWindow", "Алгоритм сортировки:"))
        self.pB_exit.setText(_translate("MainWindow", "Выход"))
        self.label_s_txt.setText(_translate("MainWindow", "Будет затронуто строк массива:"))
        self.label_out_TB.setText(_translate("MainWindow", "Выходные данные сортированных столбцов"))
        self.label_s.setText(_translate("MainWindow", "Выбор столбца сортировки:"))
        self.pB_vvod.setText(_translate("MainWindow", "Рассчитать"))
        self.l_out_hS.setText(_translate("MainWindow", "50"))
        self.cB_column.setItemText(0, _translate("MainWindow", "7"))
        self.cB_column.setItemText(1, _translate("MainWindow", "8"))
        self.cB_column.setItemText(2, _translate("MainWindow", "9"))
        self.cB_mtd.setItemText(0, _translate("MainWindow", "Слиянием"))
        self.cB_mtd.setItemText(1, _translate("MainWindow", "Пузырьковый"))
        self.cB_mtd.setItemText(2, _translate("MainWindow", "Пирамидальнаый"))
        self.l_author.setText(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Работа выполнена:</p>\n"
                                         "<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">студентом группы УБСС2001</p>\n"
                                         "<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Сучилиной Светланой</p></body></html>"))

        self.pB_vvod.clicked.connect(lambda: self._click_rez())
        self.row_1 = 7  # стандартные значения
        self.mtd = str("Слиянием")  # стандартные значения
        print("Заданы стандартные значения", self.row_1, self.mtd)

    def _click_rez(self):
        self.tb_out.clear()
        if self.row_1 == 7 or self.row_1 == 8 or self.row_1 == 9:  # входные значения столбцов
            for x in range(2, self.hS.value() + 2):  # получение данных
                maszna4.append(sheet[x][int(self.row_1)].value)  # ошибка перевода буквы в число

            if str(self.mtd) == "Слиянием":
                if self.hS.value() == 0:
                    self.tb_out.setText("Нечего сортировать")
                    return
                else:
                    mergeSort(maszna4)
                    print(self.mtd)
                    self.tb_out.setText(str(maszna4))

            elif str(self.mtd) == "Пузырьковый":
                bubble(maszna4)
                print(self.mtd)
                self.tb_out.setText(str(maszna4))

            elif str(self.mtd) == "Пирамидальнаый":
                heap(maszna4)
                print(self.mtd)
                self.tb_out.setText(str(maszna4))

            else:  # ничего не делать если входные данные другие, отладка, исключение
                return

        else:  # ничего не делать если входные данные другие, отладка, исключение
            return
        maszna4.clear()  # для отсутствия дублирования в выходе

    def _click_mtd(self, mtd):  # метод
        self.mtd = mtd

        return mtd

    def _click_column(self, row_1):  # строка
        self.row_1 = int(row_1)
        return row_1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
