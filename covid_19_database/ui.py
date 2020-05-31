# 某个国家某个省份的现存确诊、疑似病例、死亡人数、治愈人数、累计确诊数变化
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import sys
from generate_chart import generate_line_chart, generate_heat_map, generate_drug_map


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(1200, 900)

        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setObjectName("main_widget")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件main_widget

        self.query_widget = QtWidgets.QTabWidget()
        self.query_widget.setObjectName('query_widget')

        self.result_widget = QtWebEngineWidgets.QWebEngineView()
        self.result_widget.setObjectName('result_widget')

        self.main_layout.addWidget(self.query_widget, 2)
        self.main_layout.addWidget(self.result_widget, 4)

        self.query_1 = QtWidgets.QWidget()
        self.query_layout_1 = QtWidgets.QGridLayout()
        self.query_1.setLayout(self.query_layout_1)
        self.query_widget.addTab(self.query_1, '病例-日期折线图')

        self.country1 = QtWidgets.QComboBox()
        self.country1.setObjectName('country1')
        self.country1.addItems(
            ['None', 'Brazil', 'Canada', 'China', 'Italy', 'Russia', 'Spain', 'United Kingdom', 'United States'])
        self.country1.currentIndexChanged.connect(self.set_province_1)
        self.country1.setMaximumSize(200, 50)
        self.country2 = QtWidgets.QComboBox()
        self.country2.setObjectName('country2')
        self.country2.addItems(
            ['None', 'Brazil', 'Canada', 'China', 'Italy', 'Russia', 'Spain', 'United Kingdom', 'United States'])
        self.country2.currentIndexChanged.connect(self.set_province_2)
        self.country2.setMaximumSize(200, 50)

        self.province1 = QtWidgets.QComboBox()
        self.province1.setObjectName('province1')
        self.province1.addItem('None')
        self.province1.setMaximumSize(200, 50)
        self.province2 = QtWidgets.QComboBox()
        self.province2.setObjectName('province2')
        self.province2.addItem('None')
        self.province2.setMaximumSize(200, 50)

        self.date1 = QtWidgets.QDateEdit()
        self.date1.setObjectName('date1')
        self.date1.setDate(QtCore.QDate(2020, 1, 11))
        self.date1.setMaximumSize(400, 50)
        self.date2 = QtWidgets.QDateEdit()
        self.date2.setObjectName('date2')
        self.date2.setDate(QtCore.QDate.currentDate())
        self.date2.setMaximumSize(400, 50)

        self.line1 = QtWidgets.QLineEdit()
        self.line1.setObjectName('line1')
        self.line1.setReadOnly(True)
        self.line1.setText('国家1')
        self.line1.setMaximumSize(200, 50)
        self.line2 = QtWidgets.QLineEdit()
        self.line2.setObjectName('line2')
        self.line2.setReadOnly(True)
        self.line2.setText('国家2')
        self.line2.setMaximumSize(200, 50)
        self.line3 = QtWidgets.QLineEdit()
        self.line3.setObjectName('line3')
        self.line3.setReadOnly(True)
        self.line3.setText('日期1')
        self.line3.setMaximumSize(200, 50)
        self.line4 = QtWidgets.QLineEdit()
        self.line4.setObjectName('line4')
        self.line4.setReadOnly(True)
        self.line4.setText('日期2')
        self.line4.setMaximumSize(200, 50)

        self.check1 = QtWidgets.QCheckBox()
        self.check1.setObjectName('check1')
        self.check1.setText('现存确诊数')
        self.check1.setChecked(True)
        self.check2 = QtWidgets.QCheckBox()
        self.check2.setObjectName('check2')
        self.check2.setText('疑似病例数')
        self.check3 = QtWidgets.QCheckBox()
        self.check3.setObjectName('check3')
        self.check3.setText('死亡人数')
        self.check4 = QtWidgets.QCheckBox()
        self.check4.setObjectName('check4')
        self.check4.setText('治愈人数')
        self.check5 = QtWidgets.QCheckBox()
        self.check5.setObjectName('check5')
        self.check5.setText('累计确诊数')
        self.chechs = [self.check1, self.check2, self.check3, self.check4, self.check5]

        self.search = QtWidgets.QPushButton()
        self.search.setObjectName('search')
        self.search.setText('查询')
        self.search.setMaximumSize(200, 50)
        self.search.clicked.connect(self.search_it)


        self.query_layout_1.addWidget(self.line1, 0, 0, 1, 1)
        self.query_layout_1.addWidget(self.country1, 0, 1, 1, 1)
        self.query_layout_1.addWidget(self.province1, 0, 2, 1, 1)
        self.query_layout_1.addWidget(self.line2, 0, 3, 1, 1)
        self.query_layout_1.addWidget(self.country2, 0, 4, 1, 1)
        self.query_layout_1.addWidget(self.province2, 0, 5, 1, 1)

        self.query_layout_1.addWidget(self.line3, 1, 0, 1, 1)
        self.query_layout_1.addWidget(self.date1, 1, 1, 1, 2)
        self.query_layout_1.addWidget(self.line4, 1, 3, 1, 1)
        self.query_layout_1.addWidget(self.date2, 1, 4, 1, 2)

        self.query_layout_1.addWidget(self.check1, 2, 0, 1, 1)
        self.query_layout_1.addWidget(self.check2, 2, 1, 1, 1)
        self.query_layout_1.addWidget(self.check3, 2, 2, 1, 1)
        self.query_layout_1.addWidget(self.check4, 2, 3, 1, 1)
        self.query_layout_1.addWidget(self.check5, 2, 4, 1, 1)
        self.query_layout_1.addWidget(self.search, 2, 5, 1, 1)

        self.query_2 = QtWidgets.QWidget()
        self.query_layout_2 = QtWidgets.QGridLayout()
        self.query_2.setLayout(self.query_layout_2)
        self.query_widget.addTab(self.query_2, '病例热力图')

        self.country3 = QtWidgets.QComboBox()
        self.country3.setObjectName('country1')
        self.country3.addItems(
            ['ALL', 'Brazil', 'Canada', 'China', 'Italy', 'Russia', 'Spain', 'United Kingdom', 'United States'])
        self.country3.currentIndexChanged.connect(self.set_province_3)
        self.country3.setMaximumSize(240, 50)

        self.province3 = QtWidgets.QComboBox()
        self.province3.setObjectName('province3')
        self.province3.addItem('None')
        self.province3.setMaximumSize(240, 50)

        self.date3 = QtWidgets.QDateEdit()
        self.date3.setObjectName('date3')
        self.date3.setDate(QtCore.QDate.currentDate())
        self.date3.setMaximumSize(480, 50)

        self.search_2 = QtWidgets.QPushButton()
        self.search_2.setObjectName('search_2')
        self.search_2.setText('查询')
        self.search_2.setMaximumSize(240, 50)
        self.search_2.clicked.connect(self.search_it_2)


        self.query_layout_2.addWidget(self.country3, 0, 0, 1, 1)
        self.query_layout_2.addWidget(self.province3, 0, 1, 1, 1)
        self.query_layout_2.addWidget(self.date3, 0, 2, 1, 2)
        self.query_layout_2.addWidget(self.search_2, 0, 4, 1, 1)

        self.query_3 = QtWidgets.QWidget()
        self.query_layout_3 = QtWidgets.QVBoxLayout()
        self.query_3.setLayout(self.query_layout_3)
        self.query_widget.addTab(self.query_3, '药物研发情况')

        self.type = QtWidgets.QComboBox()
        self.type.setObjectName('drug_type')
        self.type.addItems(['疫苗', '抗体', '小分子药物'])

        self.date4 = QtWidgets.QDateEdit()
        self.date4.setObjectName('date4')
        self.date4.setDate(QtCore.QDate.currentDate())

        self.search_3 = QtWidgets.QPushButton()
        self.search_3.setObjectName('search_3')
        self.search_3.setText('查询')
        self.search_3.clicked.connect(self.search_it_2)

        self.query_layout_3.addWidget(self.type)
        self.query_layout_3.addWidget(self.date4)
        self.query_layout_3.addWidget(self.search_3)

    def get_demands(self):
        demands = []
        for check in self.chechs:
            if check.isChecked():
                demands.append('')
            else:
                demands.append(check.text())

    def search_it(self):
        date_1 = self.date1.date().toString(QtCore.Qt.ISODate)
        date_2 = self.date2.date().toString(QtCore.Qt.ISODate)
        arguments = [self.country1.currentText(), self.province1.currentText(), self.country2.currentText(), self.province2.currentText(), self.get_demands()]
        generate_line_chart(date_1, date_2, *arguments)
        self.result_widget.load(QtCore.QUrl('D:/曲一鸣文件/大二下数据库技术（宋韶旭）/大作业/1.html'))  # 这里的路径必须写绝对路径
        self.result_widget.show()

    def search_it_2(self):
        date = self.date3.date().toString(QtCore.Qt.ISODate)
        generate_heat_map(date, self.country3.currentText(), self.province3.currentText())
        self.result_widget.load(QtCore.QUrl('D:/曲一鸣文件/大二下数据库技术（宋韶旭）/大作业/2.html'))
        self.result_widget.show()

    def search_it_3(self):
        date = self.date4.date().toString(QtCore.Qt.ISODate)
        generate_drug_map(date, self.type.currentText())
        self.result_widget.load(QtCore.QUrl('D:/曲一鸣文件/大二下数据库技术（宋韶旭）/大作业/3.html'))
        self.result_widget.load()

    def set_province_1(self):
        if self.country1.currentText() == 'China':
            self.province1.clear()
            provinces = ['新疆', '西藏', '青海', '甘肃', '四川', '云南', '宁夏', '陕西', '重庆', '贵州', '广西', '内蒙古',
                         '山西', '河南', '湖北', '湖南', '广东', '澳门', '香港', '海南', '江西', '安徽', '河北', '北京',
                         '天津', '安徽', '江苏', '浙江', '上海', '福建', '山东', '南海诸岛', '台湾', '辽宁', '吉林',
                         '黑龙江', 'ALL']
            self.province1.addItems(sorted(provinces))
        else:
            self.province1.clear()
            self.province1.addItem('ALL')

    def set_province_2(self):
        if self.country2.currentText() == 'China':
            self.province2.clear()
            provinces = ['新疆', '西藏', '青海', '甘肃', '四川', '云南', '宁夏', '陕西', '重庆', '贵州', '广西', '内蒙古',
                         '山西', '河南', '湖北', '湖南', '广东', '澳门', '香港', '海南', '江西', '安徽', '河北', '北京',
                         '天津', '安徽', '江苏', '浙江', '上海', '福建', '山东', '南海诸岛', '台湾', '辽宁', '吉林',
                         '黑龙江', 'ALL']
            self.province2.addItems(sorted(provinces))
        else:
            self.province2.clear()
            self.province2.addItem('ALL')

    def set_province_3(self):
        if self.country3.currentText() == 'China':
            self.province3.clear()
            provinces = ['新疆', '西藏', '青海', '甘肃', '四川', '云南', '宁夏', '陕西', '重庆', '贵州', '广西', '内蒙古',
                         '山西', '河南', '湖北', '湖南', '广东', '澳门', '香港', '海南', '江西', '安徽', '河北', '北京',
                         '天津', '安徽', '江苏', '浙江', '上海', '福建', '山东', '南海诸岛', '台湾', '辽宁', '吉林',
                         '黑龙江', 'ALL']
            self.province3.addItems(sorted(provinces))
        else:
            self.province3.clear()
            self.province3.addItem('ALL')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
