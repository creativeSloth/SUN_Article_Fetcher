# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 110, 981, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(8, 121, 971, 800))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 800))
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setEnabled(True)
        self.tab1.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.load_articles_file_btn = QPushButton(self.tab1)
        self.load_articles_file_btn.setObjectName(u"load_articles_file_btn")
        sizePolicy.setHeightForWidth(self.load_articles_file_btn.sizePolicy().hasHeightForWidth())
        self.load_articles_file_btn.setSizePolicy(sizePolicy)
        self.load_articles_file_btn.setMinimumSize(QSize(0, 40))
        self.load_articles_file_btn.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setUnderline(False)
        self.load_articles_file_btn.setFont(font)
        self.load_articles_file_btn.setCheckable(False)
        self.load_articles_file_btn.setChecked(False)
        self.load_articles_file_btn.setAutoDefault(False)
        self.load_articles_file_btn.setFlat(False)

        self.gridLayout_3.addWidget(self.load_articles_file_btn, 0, 0, 1, 1)

        self.load_articles_db_btn = QPushButton(self.tab1)
        self.load_articles_db_btn.setObjectName(u"load_articles_db_btn")
        self.load_articles_db_btn.setMinimumSize(QSize(0, 40))
        self.load_articles_db_btn.setMaximumSize(QSize(200, 40))
        self.load_articles_db_btn.setFont(font)

        self.gridLayout_3.addWidget(self.load_articles_db_btn, 0, 1, 1, 1)

        self.line_2 = QFrame(self.tab1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 2)

        self.articles_list = QTableWidget(self.tab1)
        if (self.articles_list.columnCount() < 4):
            self.articles_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.articles_list.setObjectName(u"articles_list")
        self.articles_list.setEnabled(True)
        sizePolicy.setHeightForWidth(self.articles_list.sizePolicy().hasHeightForWidth())
        self.articles_list.setSizePolicy(sizePolicy)
        self.articles_list.setMinimumSize(QSize(21213, 300))
        self.articles_list.setMaximumSize(QSize(16777215, 6544566))
        self.articles_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.articles_list.setDragDropOverwriteMode(False)
        self.articles_list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.articles_list.setAlternatingRowColors(True)
        self.articles_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.articles_list.setGridStyle(Qt.SolidLine)
        self.articles_list.setWordWrap(False)
        self.articles_list.setCornerButtonEnabled(True)
        self.articles_list.horizontalHeader().setVisible(True)
        self.articles_list.horizontalHeader().setCascadingSectionResizes(True)
        self.articles_list.horizontalHeader().setMinimumSectionSize(50)
        self.articles_list.horizontalHeader().setDefaultSectionSize(120)
        self.articles_list.horizontalHeader().setHighlightSections(True)
        self.articles_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.articles_list.horizontalHeader().setStretchLastSection(False)
        self.articles_list.verticalHeader().setVisible(False)
        self.articles_list.verticalHeader().setCascadingSectionResizes(False)
        self.articles_list.verticalHeader().setMinimumSectionSize(5)
        self.articles_list.verticalHeader().setHighlightSections(True)
        self.articles_list.verticalHeader().setProperty("showSortIndicator", True)
        self.articles_list.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.articles_list, 2, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.source_path_btn = QPushButton(self.tab1)
        self.source_path_btn.setObjectName(u"source_path_btn")
        sizePolicy.setHeightForWidth(self.source_path_btn.sizePolicy().hasHeightForWidth())
        self.source_path_btn.setSizePolicy(sizePolicy)
        self.source_path_btn.setMinimumSize(QSize(135, 30))
        self.source_path_btn.setMaximumSize(QSize(150, 40))

        self.gridLayout_2.addWidget(self.source_path_btn, 1, 0, 1, 1)

        self.paste_docs_btn = QPushButton(self.tab1)
        self.paste_docs_btn.setObjectName(u"paste_docs_btn")
        sizePolicy.setHeightForWidth(self.paste_docs_btn.sizePolicy().hasHeightForWidth())
        self.paste_docs_btn.setSizePolicy(sizePolicy)
        self.paste_docs_btn.setMinimumSize(QSize(135, 50))
        self.paste_docs_btn.setMaximumSize(QSize(4000000, 100))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        self.paste_docs_btn.setFont(font1)
        self.paste_docs_btn.setAutoDefault(False)
        self.paste_docs_btn.setFlat(False)

        self.gridLayout_2.addWidget(self.paste_docs_btn, 3, 1, 1, 1)

        self.target_path_btn = QPushButton(self.tab1)
        self.target_path_btn.setObjectName(u"target_path_btn")
        sizePolicy.setHeightForWidth(self.target_path_btn.sizePolicy().hasHeightForWidth())
        self.target_path_btn.setSizePolicy(sizePolicy)
        self.target_path_btn.setMinimumSize(QSize(135, 30))
        self.target_path_btn.setMaximumSize(QSize(150, 40))
        self.target_path_btn.setAutoDefault(False)
        self.target_path_btn.setFlat(False)

        self.gridLayout_2.addWidget(self.target_path_btn, 2, 0, 1, 1)

        self.target_path_text = QPlainTextEdit(self.tab1)
        self.target_path_text.setObjectName(u"target_path_text")
        self.target_path_text.setMinimumSize(QSize(0, 30))
        self.target_path_text.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.target_path_text, 2, 1, 1, 1)

        self.source_path_text = QPlainTextEdit(self.tab1)
        self.source_path_text.setObjectName(u"source_path_text")
        sizePolicy.setHeightForWidth(self.source_path_text.sizePolicy().hasHeightForWidth())
        self.source_path_text.setSizePolicy(sizePolicy)
        self.source_path_text.setMinimumSize(QSize(0, 30))
        self.source_path_text.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.source_path_text, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 2)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.load_docu_db_data_btn = QPushButton(self.tab_2)
        self.load_docu_db_data_btn.setObjectName(u"load_docu_db_data_btn")

        self.gridLayout_7.addWidget(self.load_docu_db_data_btn, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -2052, 931, 2820))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.headline_01 = QLabel(self.scrollAreaWidgetContents)
        self.headline_01.setObjectName(u"headline_01")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(False)
        self.headline_01.setFont(font2)
        self.headline_01.setLayoutDirection(Qt.LeftToRight)
        self.headline_01.setAutoFillBackground(False)
        self.headline_01.setFrameShape(QFrame.StyledPanel)
        self.headline_01.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_01)

        self.gridLayout_08 = QGridLayout()
        self.gridLayout_08.setObjectName(u"gridLayout_08")
        self.loc_adress_2_label = QLabel(self.scrollAreaWidgetContents)
        self.loc_adress_2_label.setObjectName(u"loc_adress_2_label")
        self.loc_adress_2_label.setMinimumSize(QSize(0, 30))
        self.loc_adress_2_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.loc_adress_2_label, 3, 3, 1, 1)

        self.loc_adress_3_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.loc_adress_3_text.setObjectName(u"loc_adress_3_text")
        self.loc_adress_3_text.setMinimumSize(QSize(0, 30))
        self.loc_adress_3_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.loc_adress_3_text, 4, 4, 1, 1)

        self.loc_adress_1_label = QLabel(self.scrollAreaWidgetContents)
        self.loc_adress_1_label.setObjectName(u"loc_adress_1_label")
        self.loc_adress_1_label.setMinimumSize(QSize(0, 30))
        self.loc_adress_1_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.loc_adress_1_label, 2, 3, 1, 1)

        self.op_adress_2_label = QLabel(self.scrollAreaWidgetContents)
        self.op_adress_2_label.setObjectName(u"op_adress_2_label")
        self.op_adress_2_label.setMinimumSize(QSize(0, 30))
        self.op_adress_2_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.op_adress_2_label, 3, 0, 1, 1)

        self.loc_adress_2_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.loc_adress_2_text.setObjectName(u"loc_adress_2_text")
        self.loc_adress_2_text.setMinimumSize(QSize(0, 30))
        self.loc_adress_2_text.setMaximumSize(QSize(16777215, 30))
        self.loc_adress_2_text.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_08.addWidget(self.loc_adress_2_text, 3, 4, 1, 1)

        self.loc_head_label = QLabel(self.scrollAreaWidgetContents)
        self.loc_head_label.setObjectName(u"loc_head_label")
        self.loc_head_label.setMinimumSize(QSize(0, 30))
        self.loc_head_label.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setBold(True)
        self.loc_head_label.setFont(font3)

        self.gridLayout_08.addWidget(self.loc_head_label, 1, 3, 1, 1)

        self.op_adress_2_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.op_adress_2_text.setObjectName(u"op_adress_2_text")
        self.op_adress_2_text.setMinimumSize(QSize(0, 30))
        self.op_adress_2_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.op_adress_2_text, 3, 1, 1, 1)

        self.op_adress_3_label = QLabel(self.scrollAreaWidgetContents)
        self.op_adress_3_label.setObjectName(u"op_adress_3_label")
        self.op_adress_3_label.setMinimumSize(QSize(0, 30))
        self.op_adress_3_label.setMaximumSize(QSize(16777209, 30))
        self.op_adress_3_label.setFont(font3)

        self.gridLayout_08.addWidget(self.op_adress_3_label, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_08.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.loc_adress_3_label = QLabel(self.scrollAreaWidgetContents)
        self.loc_adress_3_label.setObjectName(u"loc_adress_3_label")
        self.loc_adress_3_label.setMinimumSize(QSize(0, 30))
        self.loc_adress_3_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.loc_adress_3_label, 4, 3, 1, 1)

        self.loc_adress_1_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.loc_adress_1_text.setObjectName(u"loc_adress_1_text")
        self.loc_adress_1_text.setMinimumSize(QSize(0, 30))
        self.loc_adress_1_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.loc_adress_1_text, 2, 4, 1, 1)

        self.op_adress_3_label_2 = QLabel(self.scrollAreaWidgetContents)
        self.op_adress_3_label_2.setObjectName(u"op_adress_3_label_2")
        self.op_adress_3_label_2.setMinimumSize(QSize(0, 30))
        self.op_adress_3_label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.op_adress_3_label_2, 4, 0, 1, 1)

        self.op_adress_3_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.op_adress_3_text.setObjectName(u"op_adress_3_text")
        self.op_adress_3_text.setMinimumSize(QSize(0, 30))
        self.op_adress_3_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.op_adress_3_text, 4, 1, 1, 1)

        self.op_adress_1_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.op_adress_1_text.setObjectName(u"op_adress_1_text")
        self.op_adress_1_text.setMinimumSize(QSize(0, 30))
        self.op_adress_1_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.op_adress_1_text, 2, 1, 1, 1)

        self.operator_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.operator_text.setObjectName(u"operator_text")
        self.operator_text.setMinimumSize(QSize(0, 30))
        self.operator_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.operator_text, 1, 1, 1, 1)

        self.op_adress_1_label = QLabel(self.scrollAreaWidgetContents)
        self.op_adress_1_label.setObjectName(u"op_adress_1_label")
        self.op_adress_1_label.setMinimumSize(QSize(0, 30))
        self.op_adress_1_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_08.addWidget(self.op_adress_1_label, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_08)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.constr_style_label = QLabel(self.scrollAreaWidgetContents)
        self.constr_style_label.setObjectName(u"constr_style_label")
        self.constr_style_label.setMinimumSize(QSize(0, 30))
        self.constr_style_label.setMaximumSize(QSize(16777215, 30))
        self.constr_style_label.setFont(font3)

        self.gridLayout_10.addWidget(self.constr_style_label, 0, 3, 1, 1)

        self.sys_perf_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.sys_perf_text.setObjectName(u"sys_perf_text")
        self.sys_perf_text.setMinimumSize(QSize(0, 30))
        self.sys_perf_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.sys_perf_text, 0, 1, 1, 1)

        self.constr_style_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.constr_style_text.setObjectName(u"constr_style_text")
        self.constr_style_text.setMinimumSize(QSize(0, 30))
        self.constr_style_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.constr_style_text, 0, 4, 1, 1)

        self.sys_perf_label = QLabel(self.scrollAreaWidgetContents)
        self.sys_perf_label.setObjectName(u"sys_perf_label")
        self.sys_perf_label.setMinimumSize(QSize(0, 30))
        self.sys_perf_label.setMaximumSize(QSize(16777215, 30))
        self.sys_perf_label.setFont(font3)

        self.gridLayout_10.addWidget(self.sys_perf_label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.gridLayout_10.setColumnMinimumWidth(0, 50)
        self.gridLayout_10.setColumnMinimumWidth(1, 50)
        self.gridLayout_10.setColumnMinimumWidth(3, 50)
        self.gridLayout_10.setColumnMinimumWidth(4, 350)

        self.verticalLayout_3.addLayout(self.gridLayout_10)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.azimuth_head_label = QLabel(self.scrollAreaWidgetContents)
        self.azimuth_head_label.setObjectName(u"azimuth_head_label")
        self.azimuth_head_label.setFont(font3)

        self.verticalLayout_4.addWidget(self.azimuth_head_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bool_consist_azimuth_label = QLabel(self.scrollAreaWidgetContents)
        self.bool_consist_azimuth_label.setObjectName(u"bool_consist_azimuth_label")
        self.bool_consist_azimuth_label.setMinimumSize(QSize(0, 30))
        self.bool_consist_azimuth_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.bool_consist_azimuth_label)

        self.bool_consist_azimuth_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bool_consist_azimuth_text.setObjectName(u"bool_consist_azimuth_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bool_consist_azimuth_text.sizePolicy().hasHeightForWidth())
        self.bool_consist_azimuth_text.setSizePolicy(sizePolicy2)
        self.bool_consist_azimuth_text.setMinimumSize(QSize(0, 30))
        self.bool_consist_azimuth_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.bool_consist_azimuth_text)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.maj_tilt_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.maj_tilt_text.setObjectName(u"maj_tilt_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.maj_tilt_text.sizePolicy().hasHeightForWidth())
        self.maj_tilt_text.setSizePolicy(sizePolicy3)
        self.maj_tilt_text.setMinimumSize(QSize(0, 30))
        self.maj_tilt_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.maj_tilt_text, 3, 1, 1, 1)

        self.min_tilt_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.min_tilt_text.setObjectName(u"min_tilt_text")
        sizePolicy3.setHeightForWidth(self.min_tilt_text.sizePolicy().hasHeightForWidth())
        self.min_tilt_text.setSizePolicy(sizePolicy3)
        self.min_tilt_text.setMinimumSize(QSize(0, 30))
        self.min_tilt_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.min_tilt_text, 3, 4, 1, 1)

        self.min_azimuth_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.min_azimuth_text.setObjectName(u"min_azimuth_text")
        self.min_azimuth_text.setMinimumSize(QSize(0, 30))
        self.min_azimuth_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.min_azimuth_text, 1, 1, 1, 1)

        self.min_tilt_label = QLabel(self.scrollAreaWidgetContents)
        self.min_tilt_label.setObjectName(u"min_tilt_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.min_tilt_label.sizePolicy().hasHeightForWidth())
        self.min_tilt_label.setSizePolicy(sizePolicy4)
        self.min_tilt_label.setMinimumSize(QSize(0, 30))
        self.min_tilt_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.min_tilt_label, 3, 3, 1, 1)

        self.maj_azimuth_label = QLabel(self.scrollAreaWidgetContents)
        self.maj_azimuth_label.setObjectName(u"maj_azimuth_label")
        self.maj_azimuth_label.setMinimumSize(QSize(0, 30))
        self.maj_azimuth_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.maj_azimuth_label, 0, 0, 1, 1)

        self.min_card_point_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.min_card_point_text.setObjectName(u"min_card_point_text")
        self.min_card_point_text.setMinimumSize(QSize(0, 30))
        self.min_card_point_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.min_card_point_text, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.maj_tilt_label = QLabel(self.scrollAreaWidgetContents)
        self.maj_tilt_label.setObjectName(u"maj_tilt_label")
        sizePolicy4.setHeightForWidth(self.maj_tilt_label.sizePolicy().hasHeightForWidth())
        self.maj_tilt_label.setSizePolicy(sizePolicy4)
        self.maj_tilt_label.setMinimumSize(QSize(0, 30))
        self.maj_tilt_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.maj_tilt_label, 3, 0, 1, 1)

        self.maj_card_point_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.maj_card_point_text.setObjectName(u"maj_card_point_text")
        self.maj_card_point_text.setMinimumSize(QSize(0, 30))
        self.maj_card_point_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.maj_card_point_text, 0, 4, 1, 1)

        self.maj_card_point_label = QLabel(self.scrollAreaWidgetContents)
        self.maj_card_point_label.setObjectName(u"maj_card_point_label")

        self.gridLayout_12.addWidget(self.maj_card_point_label, 0, 3, 1, 1)

        self.min_card_point_label = QLabel(self.scrollAreaWidgetContents)
        self.min_card_point_label.setObjectName(u"min_card_point_label")

        self.gridLayout_12.addWidget(self.min_card_point_label, 1, 3, 1, 1)

        self.min_azimuth_label = QLabel(self.scrollAreaWidgetContents)
        self.min_azimuth_label.setObjectName(u"min_azimuth_label")
        self.min_azimuth_label.setMinimumSize(QSize(0, 30))
        self.min_azimuth_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.min_azimuth_label, 1, 0, 1, 1)

        self.maj_azimuth_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.maj_azimuth_text.setObjectName(u"maj_azimuth_text")
        self.maj_azimuth_text.setMinimumSize(QSize(0, 30))
        self.maj_azimuth_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.maj_azimuth_text, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_12)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.headline_02 = QLabel(self.scrollAreaWidgetContents)
        self.headline_02.setObjectName(u"headline_02")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.headline_02.setFont(font4)
        self.headline_02.setFrameShape(QFrame.StyledPanel)
        self.headline_02.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_02)

        self.PV_modules_list = QTableWidget(self.scrollAreaWidgetContents)
        if (self.PV_modules_list.columnCount() < 6):
            self.PV_modules_list.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PV_modules_list.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.PV_modules_list.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.PV_modules_list.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.PV_modules_list.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.PV_modules_list.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.PV_modules_list.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.PV_modules_list.setObjectName(u"PV_modules_list")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.PV_modules_list.sizePolicy().hasHeightForWidth())
        self.PV_modules_list.setSizePolicy(sizePolicy5)
        self.PV_modules_list.setMinimumSize(QSize(0, 200))
        self.PV_modules_list.setAutoFillBackground(False)
        self.PV_modules_list.setMidLineWidth(1)
        self.PV_modules_list.setDragDropOverwriteMode(False)
        self.PV_modules_list.setAlternatingRowColors(True)
        self.PV_modules_list.setGridStyle(Qt.DashDotDotLine)
        self.PV_modules_list.setSortingEnabled(True)
        self.PV_modules_list.setWordWrap(True)
        self.PV_modules_list.setCornerButtonEnabled(True)
        self.PV_modules_list.horizontalHeader().setMinimumSectionSize(50)
        self.PV_modules_list.horizontalHeader().setDefaultSectionSize(150)
        self.PV_modules_list.verticalHeader().setVisible(False)
        self.PV_modules_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.PV_modules_list)

        self.move_none_PV_modules_to_blacklist = QPushButton(self.scrollAreaWidgetContents)
        self.move_none_PV_modules_to_blacklist.setObjectName(u"move_none_PV_modules_to_blacklist")

        self.verticalLayout_3.addWidget(self.move_none_PV_modules_to_blacklist)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.module_count_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.module_count_text.setObjectName(u"module_count_text")
        sizePolicy3.setHeightForWidth(self.module_count_text.sizePolicy().hasHeightForWidth())
        self.module_count_text.setSizePolicy(sizePolicy3)
        self.module_count_text.setMinimumSize(QSize(0, 30))
        self.module_count_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.module_count_text, 0, 1, 1, 1)

        self.module_count_label = QLabel(self.scrollAreaWidgetContents)
        self.module_count_label.setObjectName(u"module_count_label")
        sizePolicy4.setHeightForWidth(self.module_count_label.sizePolicy().hasHeightForWidth())
        self.module_count_label.setSizePolicy(sizePolicy4)
        self.module_count_label.setMinimumSize(QSize(0, 30))
        self.module_count_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.module_count_label, 0, 0, 1, 1)

        self.mounting_type_label = QLabel(self.scrollAreaWidgetContents)
        self.mounting_type_label.setObjectName(u"mounting_type_label")
        sizePolicy4.setHeightForWidth(self.mounting_type_label.sizePolicy().hasHeightForWidth())
        self.mounting_type_label.setSizePolicy(sizePolicy4)
        self.mounting_type_label.setMinimumSize(QSize(0, 30))
        self.mounting_type_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.mounting_type_label, 4, 0, 1, 1)

        self.module_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.module_type_text.setObjectName(u"module_type_text")
        sizePolicy3.setHeightForWidth(self.module_type_text.sizePolicy().hasHeightForWidth())
        self.module_type_text.setSizePolicy(sizePolicy3)
        self.module_type_text.setMinimumSize(QSize(0, 30))
        self.module_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.module_type_text, 2, 1, 1, 1)

        self.module_type_label = QLabel(self.scrollAreaWidgetContents)
        self.module_type_label.setObjectName(u"module_type_label")
        sizePolicy4.setHeightForWidth(self.module_type_label.sizePolicy().hasHeightForWidth())
        self.module_type_label.setSizePolicy(sizePolicy4)
        self.module_type_label.setMinimumSize(QSize(0, 30))
        self.module_type_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.module_type_label, 2, 0, 1, 1)

        self.mounting_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.mounting_type_text.setObjectName(u"mounting_type_text")
        sizePolicy3.setHeightForWidth(self.mounting_type_text.sizePolicy().hasHeightForWidth())
        self.mounting_type_text.setSizePolicy(sizePolicy3)
        self.mounting_type_text.setMinimumSize(QSize(0, 30))
        self.mounting_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.mounting_type_text, 4, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_13)

        self.headline_03 = QLabel(self.scrollAreaWidgetContents)
        self.headline_03.setObjectName(u"headline_03")
        self.headline_03.setFont(font4)
        self.headline_03.setFrameShape(QFrame.StyledPanel)
        self.headline_03.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_03)

        self.PV_inverters_list = QTableWidget(self.scrollAreaWidgetContents)
        if (self.PV_inverters_list.columnCount() < 6):
            self.PV_inverters_list.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.PV_inverters_list.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.PV_inverters_list.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.PV_inverters_list.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.PV_inverters_list.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.PV_inverters_list.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.PV_inverters_list.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.PV_inverters_list.setObjectName(u"PV_inverters_list")
        sizePolicy5.setHeightForWidth(self.PV_inverters_list.sizePolicy().hasHeightForWidth())
        self.PV_inverters_list.setSizePolicy(sizePolicy5)
        self.PV_inverters_list.setMinimumSize(QSize(0, 200))
        self.PV_inverters_list.setAutoFillBackground(False)
        self.PV_inverters_list.setMidLineWidth(1)
        self.PV_inverters_list.setDragDropOverwriteMode(False)
        self.PV_inverters_list.setAlternatingRowColors(True)
        self.PV_inverters_list.setGridStyle(Qt.DashDotDotLine)
        self.PV_inverters_list.setSortingEnabled(True)
        self.PV_inverters_list.setWordWrap(True)
        self.PV_inverters_list.setCornerButtonEnabled(True)
        self.PV_inverters_list.horizontalHeader().setMinimumSectionSize(50)
        self.PV_inverters_list.horizontalHeader().setDefaultSectionSize(150)
        self.PV_inverters_list.verticalHeader().setVisible(False)
        self.PV_inverters_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.PV_inverters_list)

        self.move_none_PV_inverters_to_blacklist = QPushButton(self.scrollAreaWidgetContents)
        self.move_none_PV_inverters_to_blacklist.setObjectName(u"move_none_PV_inverters_to_blacklist")

        self.verticalLayout_3.addWidget(self.move_none_PV_inverters_to_blacklist)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hybrid_inverter_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.hybrid_inverter_bool_label.setObjectName(u"hybrid_inverter_bool_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.hybrid_inverter_bool_label.sizePolicy().hasHeightForWidth())
        self.hybrid_inverter_bool_label.setSizePolicy(sizePolicy6)
        self.hybrid_inverter_bool_label.setMinimumSize(QSize(0, 30))
        self.hybrid_inverter_bool_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.hybrid_inverter_bool_label)

        self.hybrid_inverter_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.hybrid_inverter_bool_text.setObjectName(u"hybrid_inverter_bool_text")
        sizePolicy5.setHeightForWidth(self.hybrid_inverter_bool_text.sizePolicy().hasHeightForWidth())
        self.hybrid_inverter_bool_text.setSizePolicy(sizePolicy5)
        self.hybrid_inverter_bool_text.setMinimumSize(QSize(0, 30))
        self.hybrid_inverter_bool_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.hybrid_inverter_bool_text)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.inverter_SN_label = QLabel(self.scrollAreaWidgetContents)
        self.inverter_SN_label.setObjectName(u"inverter_SN_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.inverter_SN_label.sizePolicy().hasHeightForWidth())
        self.inverter_SN_label.setSizePolicy(sizePolicy7)
        self.inverter_SN_label.setMinimumSize(QSize(0, 30))
        self.inverter_SN_label.setMaximumSize(QSize(16777215, 45))

        self.gridLayout_14.addWidget(self.inverter_SN_label, 0, 2, 1, 1)

        self.inverter_SN_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.inverter_SN_text.setObjectName(u"inverter_SN_text")
        sizePolicy5.setHeightForWidth(self.inverter_SN_text.sizePolicy().hasHeightForWidth())
        self.inverter_SN_text.setSizePolicy(sizePolicy5)
        self.inverter_SN_text.setMinimumSize(QSize(0, 30))
        self.inverter_SN_text.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_14.addWidget(self.inverter_SN_text, 0, 3, 1, 1)

        self.inverter_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.inverter_type_text.setObjectName(u"inverter_type_text")
        sizePolicy5.setHeightForWidth(self.inverter_type_text.sizePolicy().hasHeightForWidth())
        self.inverter_type_text.setSizePolicy(sizePolicy5)
        self.inverter_type_text.setMinimumSize(QSize(0, 30))
        self.inverter_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.inverter_type_text, 0, 1, 1, 1)

        self.commiss_date_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.commiss_date_text.setObjectName(u"commiss_date_text")
        sizePolicy5.setHeightForWidth(self.commiss_date_text.sizePolicy().hasHeightForWidth())
        self.commiss_date_text.setSizePolicy(sizePolicy5)
        self.commiss_date_text.setMinimumSize(QSize(0, 30))
        self.commiss_date_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.commiss_date_text, 1, 3, 1, 1)

        self.commiss_date_label = QLabel(self.scrollAreaWidgetContents)
        self.commiss_date_label.setObjectName(u"commiss_date_label")
        sizePolicy6.setHeightForWidth(self.commiss_date_label.sizePolicy().hasHeightForWidth())
        self.commiss_date_label.setSizePolicy(sizePolicy6)
        self.commiss_date_label.setMinimumSize(QSize(0, 30))
        self.commiss_date_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.commiss_date_label, 1, 2, 1, 1)

        self.inverter_power_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.inverter_power_text.setObjectName(u"inverter_power_text")
        sizePolicy5.setHeightForWidth(self.inverter_power_text.sizePolicy().hasHeightForWidth())
        self.inverter_power_text.setSizePolicy(sizePolicy5)
        self.inverter_power_text.setMinimumSize(QSize(0, 30))
        self.inverter_power_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.inverter_power_text, 1, 1, 1, 1)

        self.inverter_power_label = QLabel(self.scrollAreaWidgetContents)
        self.inverter_power_label.setObjectName(u"inverter_power_label")
        sizePolicy6.setHeightForWidth(self.inverter_power_label.sizePolicy().hasHeightForWidth())
        self.inverter_power_label.setSizePolicy(sizePolicy6)
        self.inverter_power_label.setMinimumSize(QSize(0, 30))
        self.inverter_power_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.inverter_power_label, 1, 0, 1, 1)

        self.inverter_type_label = QLabel(self.scrollAreaWidgetContents)
        self.inverter_type_label.setObjectName(u"inverter_type_label")
        sizePolicy6.setHeightForWidth(self.inverter_type_label.sizePolicy().hasHeightForWidth())
        self.inverter_type_label.setSizePolicy(sizePolicy6)
        self.inverter_type_label.setMinimumSize(QSize(0, 30))
        self.inverter_type_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.inverter_type_label, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_14)

        self.headline_04 = QLabel(self.scrollAreaWidgetContents)
        self.headline_04.setObjectName(u"headline_04")
        self.headline_04.setFont(font4)
        self.headline_04.setFrameShape(QFrame.StyledPanel)
        self.headline_04.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_04)

        self.BAT_inverters_list = QTableWidget(self.scrollAreaWidgetContents)
        if (self.BAT_inverters_list.columnCount() < 7):
            self.BAT_inverters_list.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.BAT_inverters_list.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.BAT_inverters_list.setObjectName(u"BAT_inverters_list")
        sizePolicy5.setHeightForWidth(self.BAT_inverters_list.sizePolicy().hasHeightForWidth())
        self.BAT_inverters_list.setSizePolicy(sizePolicy5)
        self.BAT_inverters_list.setMinimumSize(QSize(0, 200))
        self.BAT_inverters_list.setAutoFillBackground(False)
        self.BAT_inverters_list.setMidLineWidth(1)
        self.BAT_inverters_list.setDragDropOverwriteMode(False)
        self.BAT_inverters_list.setAlternatingRowColors(True)
        self.BAT_inverters_list.setGridStyle(Qt.DashDotDotLine)
        self.BAT_inverters_list.setSortingEnabled(True)
        self.BAT_inverters_list.setWordWrap(True)
        self.BAT_inverters_list.setCornerButtonEnabled(True)
        self.BAT_inverters_list.horizontalHeader().setMinimumSectionSize(50)
        self.BAT_inverters_list.horizontalHeader().setDefaultSectionSize(150)
        self.BAT_inverters_list.verticalHeader().setVisible(False)
        self.BAT_inverters_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.BAT_inverters_list)

        self.move_none_BAT_inverters_to_blacklist = QPushButton(self.scrollAreaWidgetContents)
        self.move_none_BAT_inverters_to_blacklist.setObjectName(u"move_none_BAT_inverters_to_blacklist")

        self.verticalLayout_3.addWidget(self.move_none_BAT_inverters_to_blacklist)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.bat_inverter_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_inverter_type_text.setObjectName(u"bat_inverter_type_text")
        sizePolicy5.setHeightForWidth(self.bat_inverter_type_text.sizePolicy().hasHeightForWidth())
        self.bat_inverter_type_text.setSizePolicy(sizePolicy5)
        self.bat_inverter_type_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.bat_inverter_type_text, 0, 1, 1, 1)

        self.bat_inverter_type_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_inverter_type_label.setObjectName(u"bat_inverter_type_label")
        sizePolicy6.setHeightForWidth(self.bat_inverter_type_label.sizePolicy().hasHeightForWidth())
        self.bat_inverter_type_label.setSizePolicy(sizePolicy6)
        self.bat_inverter_type_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.bat_inverter_type_label, 0, 0, 1, 1)

        self.bat_inverter_SN_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_inverter_SN_text.setObjectName(u"bat_inverter_SN_text")
        sizePolicy5.setHeightForWidth(self.bat_inverter_SN_text.sizePolicy().hasHeightForWidth())
        self.bat_inverter_SN_text.setSizePolicy(sizePolicy5)
        self.bat_inverter_SN_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.bat_inverter_SN_text, 0, 3, 1, 1)

        self.coupling_type_label = QLabel(self.scrollAreaWidgetContents)
        self.coupling_type_label.setObjectName(u"coupling_type_label")
        sizePolicy6.setHeightForWidth(self.coupling_type_label.sizePolicy().hasHeightForWidth())
        self.coupling_type_label.setSizePolicy(sizePolicy6)
        self.coupling_type_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.coupling_type_label, 1, 2, 1, 1)

        self.bat_inverter_power_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_inverter_power_label.setObjectName(u"bat_inverter_power_label")
        sizePolicy6.setHeightForWidth(self.bat_inverter_power_label.sizePolicy().hasHeightForWidth())
        self.bat_inverter_power_label.setSizePolicy(sizePolicy6)
        self.bat_inverter_power_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.bat_inverter_power_label, 1, 0, 1, 1)

        self.bat_inverter_power_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_inverter_power_text.setObjectName(u"bat_inverter_power_text")
        sizePolicy5.setHeightForWidth(self.bat_inverter_power_text.sizePolicy().hasHeightForWidth())
        self.bat_inverter_power_text.setSizePolicy(sizePolicy5)
        self.bat_inverter_power_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.bat_inverter_power_text, 1, 1, 1, 1)

        self.bat_inverter_SN_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_inverter_SN_label.setObjectName(u"bat_inverter_SN_label")
        sizePolicy6.setHeightForWidth(self.bat_inverter_SN_label.sizePolicy().hasHeightForWidth())
        self.bat_inverter_SN_label.setSizePolicy(sizePolicy6)
        self.bat_inverter_SN_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.bat_inverter_SN_label, 0, 2, 1, 1)

        self.coupling_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.coupling_type_text.setObjectName(u"coupling_type_text")
        sizePolicy5.setHeightForWidth(self.coupling_type_text.sizePolicy().hasHeightForWidth())
        self.coupling_type_text.setSizePolicy(sizePolicy5)
        self.coupling_type_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_16.addWidget(self.coupling_type_text, 1, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_16)

        self.headline_05 = QLabel(self.scrollAreaWidgetContents)
        self.headline_05.setObjectName(u"headline_05")
        self.headline_05.setFont(font4)
        self.headline_05.setFrameShape(QFrame.StyledPanel)
        self.headline_05.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_05)

        self.BAT_storage_list = QTableWidget(self.scrollAreaWidgetContents)
        if (self.BAT_storage_list.columnCount() < 8):
            self.BAT_storage_list.setColumnCount(8)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.BAT_storage_list.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        self.BAT_storage_list.setObjectName(u"BAT_storage_list")
        sizePolicy5.setHeightForWidth(self.BAT_storage_list.sizePolicy().hasHeightForWidth())
        self.BAT_storage_list.setSizePolicy(sizePolicy5)
        self.BAT_storage_list.setMinimumSize(QSize(0, 200))
        self.BAT_storage_list.setAutoFillBackground(False)
        self.BAT_storage_list.setMidLineWidth(1)
        self.BAT_storage_list.setDragDropOverwriteMode(False)
        self.BAT_storage_list.setAlternatingRowColors(True)
        self.BAT_storage_list.setGridStyle(Qt.DashDotDotLine)
        self.BAT_storage_list.setSortingEnabled(True)
        self.BAT_storage_list.setWordWrap(True)
        self.BAT_storage_list.setCornerButtonEnabled(True)
        self.BAT_storage_list.horizontalHeader().setMinimumSectionSize(50)
        self.BAT_storage_list.horizontalHeader().setDefaultSectionSize(150)
        self.BAT_storage_list.verticalHeader().setVisible(False)
        self.BAT_storage_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.BAT_storage_list)

        self.move_none_BAT_storage_to_blacklist = QPushButton(self.scrollAreaWidgetContents)
        self.move_none_BAT_storage_to_blacklist.setObjectName(u"move_none_BAT_storage_to_blacklist")

        self.verticalLayout_3.addWidget(self.move_none_BAT_storage_to_blacklist)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.bat_storage_SN_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_storage_SN_text.setObjectName(u"bat_storage_SN_text")
        sizePolicy5.setHeightForWidth(self.bat_storage_SN_text.sizePolicy().hasHeightForWidth())
        self.bat_storage_SN_text.setSizePolicy(sizePolicy5)
        self.bat_storage_SN_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_storage_SN_text, 1, 3, 1, 1)

        self.max_discharge_pow_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.max_discharge_pow_text.setObjectName(u"max_discharge_pow_text")
        sizePolicy5.setHeightForWidth(self.max_discharge_pow_text.sizePolicy().hasHeightForWidth())
        self.max_discharge_pow_text.setSizePolicy(sizePolicy5)
        self.max_discharge_pow_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.max_discharge_pow_text, 3, 1, 1, 1)

        self.em_pow_ability_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.em_pow_ability_bool_label.setObjectName(u"em_pow_ability_bool_label")
        sizePolicy6.setHeightForWidth(self.em_pow_ability_bool_label.sizePolicy().hasHeightForWidth())
        self.em_pow_ability_bool_label.setSizePolicy(sizePolicy6)
        self.em_pow_ability_bool_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.em_pow_ability_bool_label, 3, 2, 1, 1)

        self.bat_storage_cap_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_storage_cap_text.setObjectName(u"bat_storage_cap_text")
        sizePolicy5.setHeightForWidth(self.bat_storage_cap_text.sizePolicy().hasHeightForWidth())
        self.bat_storage_cap_text.setSizePolicy(sizePolicy5)
        self.bat_storage_cap_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_storage_cap_text, 2, 1, 1, 1)

        self.energy_storage_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.energy_storage_type_text.setObjectName(u"energy_storage_type_text")
        sizePolicy5.setHeightForWidth(self.energy_storage_type_text.sizePolicy().hasHeightForWidth())
        self.energy_storage_type_text.setSizePolicy(sizePolicy5)
        self.energy_storage_type_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.energy_storage_type_text, 4, 1, 1, 1)

        self.bat_storage_SN_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_storage_SN_label.setObjectName(u"bat_storage_SN_label")
        sizePolicy6.setHeightForWidth(self.bat_storage_SN_label.sizePolicy().hasHeightForWidth())
        self.bat_storage_SN_label.setSizePolicy(sizePolicy6)
        self.bat_storage_SN_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_storage_SN_label, 1, 2, 1, 1)

        self.bat_storage_cap_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_storage_cap_label.setObjectName(u"bat_storage_cap_label")
        sizePolicy6.setHeightForWidth(self.bat_storage_cap_label.sizePolicy().hasHeightForWidth())
        self.bat_storage_cap_label.setSizePolicy(sizePolicy6)
        self.bat_storage_cap_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_storage_cap_label, 2, 0, 1, 1)

        self.bat_storage_type_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_storage_type_label.setObjectName(u"bat_storage_type_label")
        sizePolicy6.setHeightForWidth(self.bat_storage_type_label.sizePolicy().hasHeightForWidth())
        self.bat_storage_type_label.setSizePolicy(sizePolicy6)
        self.bat_storage_type_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_storage_type_label, 1, 0, 1, 1)

        self.bat_technology_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_technology_text.setObjectName(u"bat_technology_text")
        sizePolicy5.setHeightForWidth(self.bat_technology_text.sizePolicy().hasHeightForWidth())
        self.bat_technology_text.setSizePolicy(sizePolicy5)
        self.bat_technology_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_technology_text, 4, 3, 1, 1)

        self.bat_commiss_date_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_commiss_date_text.setObjectName(u"bat_commiss_date_text")
        sizePolicy5.setHeightForWidth(self.bat_commiss_date_text.sizePolicy().hasHeightForWidth())
        self.bat_commiss_date_text.setSizePolicy(sizePolicy5)
        self.bat_commiss_date_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_commiss_date_text, 2, 3, 1, 1)

        self.bat_commiss_date_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_commiss_date_label.setObjectName(u"bat_commiss_date_label")
        sizePolicy6.setHeightForWidth(self.bat_commiss_date_label.sizePolicy().hasHeightForWidth())
        self.bat_commiss_date_label.setSizePolicy(sizePolicy6)
        self.bat_commiss_date_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_commiss_date_label, 2, 2, 1, 1)

        self.energy_storage_type_label = QLabel(self.scrollAreaWidgetContents)
        self.energy_storage_type_label.setObjectName(u"energy_storage_type_label")
        sizePolicy6.setHeightForWidth(self.energy_storage_type_label.sizePolicy().hasHeightForWidth())
        self.energy_storage_type_label.setSizePolicy(sizePolicy6)
        self.energy_storage_type_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.energy_storage_type_label, 4, 0, 1, 1)

        self.bat_technology_label = QLabel(self.scrollAreaWidgetContents)
        self.bat_technology_label.setObjectName(u"bat_technology_label")
        sizePolicy6.setHeightForWidth(self.bat_technology_label.sizePolicy().hasHeightForWidth())
        self.bat_technology_label.setSizePolicy(sizePolicy6)
        self.bat_technology_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_technology_label, 4, 2, 1, 1)

        self.em_pow_ability_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.em_pow_ability_bool_text.setObjectName(u"em_pow_ability_bool_text")
        sizePolicy5.setHeightForWidth(self.em_pow_ability_bool_text.sizePolicy().hasHeightForWidth())
        self.em_pow_ability_bool_text.setSizePolicy(sizePolicy5)
        self.em_pow_ability_bool_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.em_pow_ability_bool_text, 3, 3, 1, 1)

        self.max_discharge_pow_label = QLabel(self.scrollAreaWidgetContents)
        self.max_discharge_pow_label.setObjectName(u"max_discharge_pow_label")
        sizePolicy6.setHeightForWidth(self.max_discharge_pow_label.sizePolicy().hasHeightForWidth())
        self.max_discharge_pow_label.setSizePolicy(sizePolicy6)
        self.max_discharge_pow_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.max_discharge_pow_label, 3, 0, 1, 1)

        self.bat_storage_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.bat_storage_type_text.setObjectName(u"bat_storage_type_text")
        sizePolicy5.setHeightForWidth(self.bat_storage_type_text.sizePolicy().hasHeightForWidth())
        self.bat_storage_type_text.setSizePolicy(sizePolicy5)
        self.bat_storage_type_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_15.addWidget(self.bat_storage_type_text, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_15)

        self.headline_06 = QLabel(self.scrollAreaWidgetContents)
        self.headline_06.setObjectName(u"headline_06")
        self.headline_06.setFont(font4)
        self.headline_06.setFrameShape(QFrame.StyledPanel)
        self.headline_06.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_06)

        self.CHG_point_list = QTableWidget(self.scrollAreaWidgetContents)
        if (self.CHG_point_list.columnCount() < 5):
            self.CHG_point_list.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.CHG_point_list.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.CHG_point_list.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.CHG_point_list.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.CHG_point_list.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.CHG_point_list.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.CHG_point_list.setObjectName(u"CHG_point_list")
        sizePolicy5.setHeightForWidth(self.CHG_point_list.sizePolicy().hasHeightForWidth())
        self.CHG_point_list.setSizePolicy(sizePolicy5)
        self.CHG_point_list.setMinimumSize(QSize(0, 200))
        self.CHG_point_list.setAutoFillBackground(False)
        self.CHG_point_list.setMidLineWidth(1)
        self.CHG_point_list.setDragDropOverwriteMode(False)
        self.CHG_point_list.setAlternatingRowColors(True)
        self.CHG_point_list.setGridStyle(Qt.DashDotDotLine)
        self.CHG_point_list.setSortingEnabled(True)
        self.CHG_point_list.setWordWrap(True)
        self.CHG_point_list.setCornerButtonEnabled(True)
        self.CHG_point_list.horizontalHeader().setMinimumSectionSize(50)
        self.CHG_point_list.horizontalHeader().setDefaultSectionSize(150)
        self.CHG_point_list.verticalHeader().setVisible(False)
        self.CHG_point_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.CHG_point_list)

        self.move_none_CHG_point_to_blacklist = QPushButton(self.scrollAreaWidgetContents)
        self.move_none_CHG_point_to_blacklist.setObjectName(u"move_none_CHG_point_to_blacklist")

        self.verticalLayout_3.addWidget(self.move_none_CHG_point_to_blacklist)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.charging_point_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.charging_point_type_text.setObjectName(u"charging_point_type_text")
        sizePolicy5.setHeightForWidth(self.charging_point_type_text.sizePolicy().hasHeightForWidth())
        self.charging_point_type_text.setSizePolicy(sizePolicy5)
        self.charging_point_type_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.charging_point_type_text, 0, 1, 1, 1)

        self.charging_point_SN_text = QTextEdit(self.scrollAreaWidgetContents)
        self.charging_point_SN_text.setObjectName(u"charging_point_SN_text")
        sizePolicy5.setHeightForWidth(self.charging_point_SN_text.sizePolicy().hasHeightForWidth())
        self.charging_point_SN_text.setSizePolicy(sizePolicy5)
        self.charging_point_SN_text.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.charging_point_SN_text, 0, 3, 1, 1)

        self.charging_point_type_label = QLabel(self.scrollAreaWidgetContents)
        self.charging_point_type_label.setObjectName(u"charging_point_type_label")
        sizePolicy6.setHeightForWidth(self.charging_point_type_label.sizePolicy().hasHeightForWidth())
        self.charging_point_type_label.setSizePolicy(sizePolicy6)
        self.charging_point_type_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.charging_point_type_label, 0, 0, 1, 1)

        self.charging_point_SN_label = QLabel(self.scrollAreaWidgetContents)
        self.charging_point_SN_label.setObjectName(u"charging_point_SN_label")
        sizePolicy6.setHeightForWidth(self.charging_point_SN_label.sizePolicy().hasHeightForWidth())
        self.charging_point_SN_label.setSizePolicy(sizePolicy6)
        self.charging_point_SN_label.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.charging_point_SN_label, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_17)

        self.headline_07 = QLabel(self.scrollAreaWidgetContents)
        self.headline_07.setObjectName(u"headline_07")
        self.headline_07.setFont(font4)
        self.headline_07.setFrameShape(QFrame.StyledPanel)
        self.headline_07.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_07)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.feeding_type_label = QLabel(self.scrollAreaWidgetContents)
        self.feeding_type_label.setObjectName(u"feeding_type_label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.feeding_type_label.sizePolicy().hasHeightForWidth())
        self.feeding_type_label.setSizePolicy(sizePolicy8)
        self.feeding_type_label.setMinimumSize(QSize(0, 30))
        self.feeding_type_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.feeding_type_label, 1, 0, 1, 1)

        self.feeding_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.feeding_type_text.setObjectName(u"feeding_type_text")
        sizePolicy2.setHeightForWidth(self.feeding_type_text.sizePolicy().hasHeightForWidth())
        self.feeding_type_text.setSizePolicy(sizePolicy2)
        self.feeding_type_text.setMinimumSize(QSize(0, 30))
        self.feeding_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.feeding_type_text, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_18)

        self.headline_08 = QLabel(self.scrollAreaWidgetContents)
        self.headline_08.setObjectName(u"headline_08")
        self.headline_08.setFont(font4)
        self.headline_08.setFrameShape(QFrame.StyledPanel)
        self.headline_08.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_08)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setSpacing(10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.rmt_drct_mrktr_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.rmt_drct_mrktr_bool_text.setObjectName(u"rmt_drct_mrktr_bool_text")
        sizePolicy3.setHeightForWidth(self.rmt_drct_mrktr_bool_text.sizePolicy().hasHeightForWidth())
        self.rmt_drct_mrktr_bool_text.setSizePolicy(sizePolicy3)
        self.rmt_drct_mrktr_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.rmt_drct_mrktr_bool_text, 2, 1, 1, 1)

        self.pow_limit_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.pow_limit_bool_label.setObjectName(u"pow_limit_bool_label")
        sizePolicy3.setHeightForWidth(self.pow_limit_bool_label.sizePolicy().hasHeightForWidth())
        self.pow_limit_bool_label.setSizePolicy(sizePolicy3)
        self.pow_limit_bool_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.pow_limit_bool_label, 0, 0, 1, 1)

        self.rmt_drct_mrktr_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.rmt_drct_mrktr_bool_label.setObjectName(u"rmt_drct_mrktr_bool_label")
        sizePolicy3.setHeightForWidth(self.rmt_drct_mrktr_bool_label.sizePolicy().hasHeightForWidth())
        self.rmt_drct_mrktr_bool_label.setSizePolicy(sizePolicy3)
        self.rmt_drct_mrktr_bool_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.rmt_drct_mrktr_bool_label, 2, 0, 1, 1)

        self.pow_limit_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.pow_limit_bool_text.setObjectName(u"pow_limit_bool_text")
        sizePolicy3.setHeightForWidth(self.pow_limit_bool_text.sizePolicy().hasHeightForWidth())
        self.pow_limit_bool_text.setSizePolicy(sizePolicy3)
        self.pow_limit_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.pow_limit_bool_text, 0, 1, 1, 1)

        self.tendering_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.tendering_bool_text.setObjectName(u"tendering_bool_text")
        sizePolicy3.setHeightForWidth(self.tendering_bool_text.sizePolicy().hasHeightForWidth())
        self.tendering_bool_text.setSizePolicy(sizePolicy3)
        self.tendering_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.tendering_bool_text, 6, 1, 1, 1)

        self.prequali_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.prequali_bool_text.setObjectName(u"prequali_bool_text")
        sizePolicy3.setHeightForWidth(self.prequali_bool_text.sizePolicy().hasHeightForWidth())
        self.prequali_bool_text.setSizePolicy(sizePolicy3)
        self.prequali_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.prequali_bool_text, 4, 1, 1, 1)

        self.tendering_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.tendering_bool_label.setObjectName(u"tendering_bool_label")
        sizePolicy3.setHeightForWidth(self.tendering_bool_label.sizePolicy().hasHeightForWidth())
        self.tendering_bool_label.setSizePolicy(sizePolicy3)
        self.tendering_bool_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.tendering_bool_label, 6, 0, 1, 1)

        self.prequali_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.prequali_bool_label.setObjectName(u"prequali_bool_label")
        sizePolicy3.setHeightForWidth(self.prequali_bool_label.sizePolicy().hasHeightForWidth())
        self.prequali_bool_label.setSizePolicy(sizePolicy3)
        self.prequali_bool_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.prequali_bool_label, 4, 0, 1, 1)

        self.rmt_grd_op_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.rmt_grd_op_bool_text.setObjectName(u"rmt_grd_op_bool_text")
        sizePolicy3.setHeightForWidth(self.rmt_grd_op_bool_text.sizePolicy().hasHeightForWidth())
        self.rmt_grd_op_bool_text.setSizePolicy(sizePolicy3)
        self.rmt_grd_op_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.rmt_grd_op_bool_text, 0, 3, 1, 1)

        self.rmt_grd_op_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.rmt_grd_op_bool_label.setObjectName(u"rmt_grd_op_bool_label")

        self.gridLayout_19.addWidget(self.rmt_grd_op_bool_label, 0, 2, 1, 1)

        self.rmt_3rd_prt_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.rmt_3rd_prt_bool_text.setObjectName(u"rmt_3rd_prt_bool_text")
        sizePolicy3.setHeightForWidth(self.rmt_3rd_prt_bool_text.sizePolicy().hasHeightForWidth())
        self.rmt_3rd_prt_bool_text.setSizePolicy(sizePolicy3)
        self.rmt_3rd_prt_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.rmt_3rd_prt_bool_text, 2, 3, 1, 1)

        self.rmt_3rd_prt_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.rmt_3rd_prt_bool_label.setObjectName(u"rmt_3rd_prt_bool_label")
        sizePolicy3.setHeightForWidth(self.rmt_3rd_prt_bool_label.sizePolicy().hasHeightForWidth())
        self.rmt_3rd_prt_bool_label.setSizePolicy(sizePolicy3)
        self.rmt_3rd_prt_bool_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.rmt_3rd_prt_bool_label, 2, 2, 1, 1)

        self.citizen_corp_bool_label = QLabel(self.scrollAreaWidgetContents)
        self.citizen_corp_bool_label.setObjectName(u"citizen_corp_bool_label")
        sizePolicy3.setHeightForWidth(self.citizen_corp_bool_label.sizePolicy().hasHeightForWidth())
        self.citizen_corp_bool_label.setSizePolicy(sizePolicy3)
        self.citizen_corp_bool_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.citizen_corp_bool_label, 4, 2, 1, 1)

        self.citizen_corp_bool_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.citizen_corp_bool_text.setObjectName(u"citizen_corp_bool_text")
        sizePolicy3.setHeightForWidth(self.citizen_corp_bool_text.sizePolicy().hasHeightForWidth())
        self.citizen_corp_bool_text.setSizePolicy(sizePolicy3)
        self.citizen_corp_bool_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.citizen_corp_bool_text, 4, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_19)

        self.headline_09 = QLabel(self.scrollAreaWidgetContents)
        self.headline_09.setObjectName(u"headline_09")
        self.headline_09.setFont(font4)
        self.headline_09.setFrameShape(QFrame.StyledPanel)
        self.headline_09.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_09)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.meter_box_type_label = QLabel(self.scrollAreaWidgetContents)
        self.meter_box_type_label.setObjectName(u"meter_box_type_label")
        sizePolicy4.setHeightForWidth(self.meter_box_type_label.sizePolicy().hasHeightForWidth())
        self.meter_box_type_label.setSizePolicy(sizePolicy4)
        self.meter_box_type_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.meter_box_type_label, 1, 0, 1, 1)

        self.meter_cabinet_label = QLabel(self.scrollAreaWidgetContents)
        self.meter_cabinet_label.setObjectName(u"meter_cabinet_label")
        sizePolicy4.setHeightForWidth(self.meter_cabinet_label.sizePolicy().hasHeightForWidth())
        self.meter_cabinet_label.setSizePolicy(sizePolicy4)
        self.meter_cabinet_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.meter_cabinet_label, 0, 0, 1, 1)

        self.meter_cabinet_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.meter_cabinet_text.setObjectName(u"meter_cabinet_text")
        sizePolicy3.setHeightForWidth(self.meter_cabinet_text.sizePolicy().hasHeightForWidth())
        self.meter_cabinet_text.setSizePolicy(sizePolicy3)
        self.meter_cabinet_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.meter_cabinet_text, 0, 1, 1, 1)

        self.meter_box_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.meter_box_type_text.setObjectName(u"meter_box_type_text")
        sizePolicy3.setHeightForWidth(self.meter_box_type_text.sizePolicy().hasHeightForWidth())
        self.meter_box_type_text.setSizePolicy(sizePolicy3)
        self.meter_box_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.meter_box_type_text, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_20)

        self.headline_10 = QLabel(self.scrollAreaWidgetContents)
        self.headline_10.setObjectName(u"headline_10")
        self.headline_10.setFont(font4)
        self.headline_10.setFrameShape(QFrame.StyledPanel)
        self.headline_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_10)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.dl_connect_ext_label = QLabel(self.scrollAreaWidgetContents)
        self.dl_connect_ext_label.setObjectName(u"dl_connect_ext_label")
        sizePolicy4.setHeightForWidth(self.dl_connect_ext_label.sizePolicy().hasHeightForWidth())
        self.dl_connect_ext_label.setSizePolicy(sizePolicy4)
        self.dl_connect_ext_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_21.addWidget(self.dl_connect_ext_label, 2, 0, 1, 1)

        self.dl_type_label = QLabel(self.scrollAreaWidgetContents)
        self.dl_type_label.setObjectName(u"dl_type_label")
        sizePolicy4.setHeightForWidth(self.dl_type_label.sizePolicy().hasHeightForWidth())
        self.dl_type_label.setSizePolicy(sizePolicy4)
        self.dl_type_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_21.addWidget(self.dl_type_label, 0, 0, 1, 1)

        self.dl_connect_ext_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.dl_connect_ext_text.setObjectName(u"dl_connect_ext_text")
        sizePolicy3.setHeightForWidth(self.dl_connect_ext_text.sizePolicy().hasHeightForWidth())
        self.dl_connect_ext_text.setSizePolicy(sizePolicy3)
        self.dl_connect_ext_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_21.addWidget(self.dl_connect_ext_text, 2, 1, 1, 1)

        self.dl_type_text = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.dl_type_text.setObjectName(u"dl_type_text")
        sizePolicy3.setHeightForWidth(self.dl_type_text.sizePolicy().hasHeightForWidth())
        self.dl_type_text.setSizePolicy(sizePolicy3)
        self.dl_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_21.addWidget(self.dl_type_text, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_21)


        self.gridLayout_5.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.target_path_text_2 = QPlainTextEdit(self.tab_2)
        self.target_path_text_2.setObjectName(u"target_path_text_2")
        self.target_path_text_2.setMinimumSize(QSize(0, 40))
        self.target_path_text_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.target_path_text_2, 5, 2, 1, 1)

        self.source_btn_docu = QPushButton(self.tab_2)
        self.source_btn_docu.setObjectName(u"source_btn_docu")
        self.source_btn_docu.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.source_btn_docu, 3, 0, 1, 1)

        self.source_path_text_docu = QPlainTextEdit(self.tab_2)
        self.source_path_text_docu.setObjectName(u"source_path_text_docu")
        self.source_path_text_docu.setMinimumSize(QSize(0, 40))
        self.source_path_text_docu.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.source_path_text_docu, 3, 2, 1, 1)

        self.source_path_text_matstr = QPlainTextEdit(self.tab_2)
        self.source_path_text_matstr.setObjectName(u"source_path_text_matstr")
        self.source_path_text_matstr.setMinimumSize(QSize(0, 40))
        self.source_path_text_matstr.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.source_path_text_matstr, 1, 2, 1, 1)

        self.target_path_btn_2 = QPushButton(self.tab_2)
        self.target_path_btn_2.setObjectName(u"target_path_btn_2")
        sizePolicy.setHeightForWidth(self.target_path_btn_2.sizePolicy().hasHeightForWidth())
        self.target_path_btn_2.setSizePolicy(sizePolicy)
        self.target_path_btn_2.setMinimumSize(QSize(135, 40))
        self.target_path_btn_2.setMaximumSize(QSize(150, 40))
        self.target_path_btn_2.setAutoDefault(False)
        self.target_path_btn_2.setFlat(False)

        self.gridLayout_6.addWidget(self.target_path_btn_2, 5, 0, 1, 1)

        self.source_btn_matstr = QPushButton(self.tab_2)
        self.source_btn_matstr.setObjectName(u"source_btn_matstr")
        self.source_btn_matstr.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.source_btn_matstr, 1, 0, 1, 1)

        self.create_docs_btn = QPushButton(self.tab_2)
        self.create_docs_btn.setObjectName(u"create_docs_btn")
        sizePolicy.setHeightForWidth(self.create_docs_btn.sizePolicy().hasHeightForWidth())
        self.create_docs_btn.setSizePolicy(sizePolicy)
        self.create_docs_btn.setMinimumSize(QSize(500, 50))
        self.create_docs_btn.setMaximumSize(QSize(400000, 100))
        self.create_docs_btn.setFont(font1)

        self.gridLayout_6.addWidget(self.create_docs_btn, 6, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_6)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.load_data_to_device_lists = QPushButton(self.tab_2)
        self.load_data_to_device_lists.setObjectName(u"load_data_to_device_lists")

        self.gridLayout_7.addWidget(self.load_data_to_device_lists, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab0 = QWidget()
        self.tab0.setObjectName(u"tab0")
        self.tab0.setMaximumSize(QSize(16777215, 500))
        self.tab0.setSizeIncrement(QSize(0, 0))
        self.gridLayout_8 = QGridLayout(self.tab0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_2 = QScrollArea(self.tab0)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 947, 480))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.server_sttings_headline_label = QLabel(self.scrollAreaWidgetContents_2)
        self.server_sttings_headline_label.setObjectName(u"server_sttings_headline_label")
        sizePolicy.setHeightForWidth(self.server_sttings_headline_label.sizePolicy().hasHeightForWidth())
        self.server_sttings_headline_label.setSizePolicy(sizePolicy)
        self.server_sttings_headline_label.setMinimumSize(QSize(250, 30))
        self.server_sttings_headline_label.setMaximumSize(QSize(16777215, 25))
        self.server_sttings_headline_label.setSizeIncrement(QSize(5, 0))
        self.server_sttings_headline_label.setFont(font4)
        self.server_sttings_headline_label.setFrameShape(QFrame.StyledPanel)
        self.server_sttings_headline_label.setFrameShadow(QFrame.Sunken)
        self.server_sttings_headline_label.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.server_sttings_headline_label)

        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.db_type = QComboBox(self.scrollAreaWidgetContents_2)
        self.db_type.addItem("")
        self.db_type.addItem("")
        self.db_type.setObjectName(u"db_type")
        self.db_type.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.db_type)

        self.db_name_label = QLabel(self.scrollAreaWidgetContents_2)
        self.db_name_label.setObjectName(u"db_name_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.db_name_label)

        self.db_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.db_name.setObjectName(u"db_name")
        self.db_name.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.db_name)

        self.db_server_label = QLabel(self.scrollAreaWidgetContents_2)
        self.db_server_label.setObjectName(u"db_server_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.db_server_label)

        self.db_server = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.db_server.setObjectName(u"db_server")
        self.db_server.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.db_server)

        self.user_label = QLabel(self.scrollAreaWidgetContents_2)
        self.user_label.setObjectName(u"user_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.user_label)

        self.user = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.user.setObjectName(u"user")
        self.user.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.user)

        self.pw_label = QLabel(self.scrollAreaWidgetContents_2)
        self.pw_label.setObjectName(u"pw_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.pw_label)

        self.pw = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.pw.setObjectName(u"pw")
        self.pw.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pw)

        self.server_sttings_headline_label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.server_sttings_headline_label_2.setObjectName(u"server_sttings_headline_label_2")
        sizePolicy.setHeightForWidth(self.server_sttings_headline_label_2.sizePolicy().hasHeightForWidth())
        self.server_sttings_headline_label_2.setSizePolicy(sizePolicy)
        self.server_sttings_headline_label_2.setMinimumSize(QSize(250, 30))
        self.server_sttings_headline_label_2.setMaximumSize(QSize(16777215, 0))
        self.server_sttings_headline_label_2.setSizeIncrement(QSize(5, 0))
        self.server_sttings_headline_label_2.setFont(font4)
        self.server_sttings_headline_label_2.setFrameShape(QFrame.StyledPanel)
        self.server_sttings_headline_label_2.setFrameShadow(QFrame.Sunken)
        self.server_sttings_headline_label_2.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.server_sttings_headline_label_2)

        self.sql_query_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.sql_query_btn.setObjectName(u"sql_query_btn")
        self.sql_query_btn.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.sql_query_btn)

        self.query_input = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.query_input.setObjectName(u"query_input")
        self.query_input.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.query_input.sizePolicy().hasHeightForWidth())
        self.query_input.setSizePolicy(sizePolicy9)
        self.query_input.setMinimumSize(QSize(0, 10))
        self.query_input.setMaximumSize(QSize(16777215, 60))
        self.query_input.setSizeIncrement(QSize(0, 500))
        self.query_input.setAutoFillBackground(True)
        self.query_input.setFrameShadow(QFrame.Raised)
        self.query_input.setTabChangesFocus(False)
        self.query_input.setUndoRedoEnabled(True)
        self.query_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.query_input)

        self.sql_query_2_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.sql_query_2_btn.setObjectName(u"sql_query_2_btn")
        self.sql_query_2_btn.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.sql_query_2_btn)

        self.query_2_input = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.query_2_input.setObjectName(u"query_2_input")
        self.query_2_input.setEnabled(True)
        self.query_2_input.setMinimumSize(QSize(0, 40))
        self.query_2_input.setMaximumSize(QSize(16777215, 50))
        self.query_2_input.setSizeIncrement(QSize(0, 500))
        self.query_2_input.setAutoFillBackground(True)
        self.query_2_input.setFrameShadow(QFrame.Raised)
        self.query_2_input.setTabChangesFocus(False)
        self.query_2_input.setUndoRedoEnabled(True)
        self.query_2_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.query_2_input)


        self.gridLayout_9.addLayout(self.formLayout, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_8.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab0, "")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 971, 111))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_4.addWidget(self.textEdit, 3, 1, 1, 1)

        self.project_label = QLabel(self.gridLayoutWidget)
        self.project_label.setObjectName(u"project_label")
        sizePolicy.setHeightForWidth(self.project_label.sizePolicy().hasHeightForWidth())
        self.project_label.setSizePolicy(sizePolicy)
        self.project_label.setMinimumSize(QSize(150, 30))
        self.project_label.setMaximumSize(QSize(200, 25))
        self.project_label.setSizeIncrement(QSize(0, 0))
        self.project_label.setFont(font4)

        self.gridLayout_4.addWidget(self.project_label, 0, 0, 1, 1)

        self.project_name_label = QLabel(self.gridLayoutWidget)
        self.project_name_label.setObjectName(u"project_name_label")
        sizePolicy.setHeightForWidth(self.project_name_label.sizePolicy().hasHeightForWidth())
        self.project_name_label.setSizePolicy(sizePolicy)
        self.project_name_label.setMinimumSize(QSize(150, 30))
        self.project_name_label.setMaximumSize(QSize(150, 25))
        self.project_name_label.setSizeIncrement(QSize(0, 0))
        self.project_name_label.setFont(font4)

        self.gridLayout_4.addWidget(self.project_name_label, 3, 0, 1, 1)

        self.project = QPlainTextEdit(self.gridLayoutWidget)
        self.project.setObjectName(u"project")
        sizePolicy.setHeightForWidth(self.project.sizePolicy().hasHeightForWidth())
        self.project.setSizePolicy(sizePolicy)
        self.project.setMinimumSize(QSize(0, 30))
        self.project.setMaximumSize(QSize(150, 30))
        self.project.setSizeIncrement(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(12)
        self.project.setFont(font5)
        self.project.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.gridLayout_4.addWidget(self.project, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy10)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.load_articles_file_btn.setDefault(True)
        self.load_articles_db_btn.setDefault(True)
        self.source_path_btn.setDefault(True)
        self.paste_docs_btn.setDefault(True)
        self.target_path_btn.setDefault(True)
        self.target_path_btn_2.setDefault(True)
        self.create_docs_btn.setDefault(True)
        self.sql_query_btn.setDefault(True)
        self.sql_query_2_btn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_articles_file_btn.setText(QCoreApplication.translate("MainWindow", u"Lade Artikelliste aus Datei", None))
        self.load_articles_db_btn.setText(QCoreApplication.translate("MainWindow", u"Lade Artikelliste aus DB", None))
        ___qtablewidgetitem = self.articles_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem1 = self.articles_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem2 = self.articles_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Artikelbezeichnung", None));
        ___qtablewidgetitem3 = self.articles_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Anzahl", None));
        self.source_path_btn.setText(QCoreApplication.translate("MainWindow", u"Quellpfad festlegen", None))
        self.paste_docs_btn.setText(QCoreApplication.translate("MainWindow", u"Dokumente \u00fcbertragen", None))
        self.target_path_btn.setText(QCoreApplication.translate("MainWindow", u"Zielpfad festlegen", None))
        self.source_path_text.setPlainText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u00dcbertragung von Dokumenten", None))
        self.load_docu_db_data_btn.setText(QCoreApplication.translate("MainWindow", u"2. F\u00fclle Datenfelder", None))
        self.headline_01.setText(QCoreApplication.translate("MainWindow", u"Anlagen\u00fcbersicht", None))
        self.loc_adress_2_label.setText(QCoreApplication.translate("MainWindow", u"PLZ:", None))
        self.loc_adress_1_label.setText(QCoreApplication.translate("MainWindow", u"Stra\u00dfe:", None))
        self.op_adress_2_label.setText(QCoreApplication.translate("MainWindow", u"PLZ:", None))
        self.loc_head_label.setText(QCoreApplication.translate("MainWindow", u"Standort:", None))
        self.op_adress_3_label.setText(QCoreApplication.translate("MainWindow", u"Anlagenbetreiber:", None))
        self.loc_adress_3_label.setText(QCoreApplication.translate("MainWindow", u"Ort:", None))
        self.op_adress_3_label_2.setText(QCoreApplication.translate("MainWindow", u"Ort:", None))
        self.op_adress_1_label.setText(QCoreApplication.translate("MainWindow", u"Stra\u00dfe:", None))
        self.constr_style_label.setText(QCoreApplication.translate("MainWindow", u"Errichtungsort:", None))
        self.constr_style_text.setPlainText(QCoreApplication.translate("MainWindow", u"Bauliche Anlage (Hausdach)", None))
        self.sys_perf_label.setText(QCoreApplication.translate("MainWindow", u"Bruttoleistung PV [kWp]:", None))
        self.azimuth_head_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung:", None))
        self.bool_consist_azimuth_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung einheitlich?", None))
        self.bool_consist_azimuth_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ja", None))
        self.min_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Neigungswinkel weitere:", None))
        self.maj_azimuth_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung \u00fcberwiegend:", None))
        self.min_card_point_text.setPlainText(QCoreApplication.translate("MainWindow", u"West", None))
        self.maj_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Neigungswinkel \u00fcberwiegend:", None))
        self.maj_card_point_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ost", None))
        self.maj_card_point_label.setText(QCoreApplication.translate("MainWindow", u"\u00dcberwiegend:", None))
        self.min_card_point_label.setText(QCoreApplication.translate("MainWindow", u"Weitere:", None))
        self.min_azimuth_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung weitere:", None))
        self.headline_02.setText(QCoreApplication.translate("MainWindow", u"Solargenerator", None))
        ___qtablewidgetitem4 = self.PV_modules_list.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem5 = self.PV_modules_list.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem6 = self.PV_modules_list.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Modul-Typ", None));
        ___qtablewidgetitem7 = self.PV_modules_list.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Anzahl [Stk.]", None));
        ___qtablewidgetitem8 = self.PV_modules_list.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem9 = self.PV_modules_list.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Modulleistung [kWp]", None));
        self.move_none_PV_modules_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.module_count_label.setText(QCoreApplication.translate("MainWindow", u"Anzahl der Module:", None))
        self.mounting_type_label.setText(QCoreApplication.translate("MainWindow", u"Montagesystem:", None))
        self.module_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.mounting_type_text.setPlainText(QCoreApplication.translate("MainWindow", u"PMT EVO 2.0 Ost-West", None))
        self.headline_03.setText(QCoreApplication.translate("MainWindow", u"PV-Wechselrichter", None))
        ___qtablewidgetitem10 = self.PV_inverters_list.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem11 = self.PV_inverters_list.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem12 = self.PV_inverters_list.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Wechselrichter-Typ", None));
        ___qtablewidgetitem13 = self.PV_inverters_list.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Anzahl [Stk.]", None));
        ___qtablewidgetitem14 = self.PV_inverters_list.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem15 = self.PV_inverters_list.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete \n"
"WR-Leistung [kW]", None));
        self.move_none_PV_inverters_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.hybrid_inverter_bool_label.setText(QCoreApplication.translate("MainWindow", u"Gemeinsamer PV-Batterie-\n"
"Wechselricher:", None))
        self.hybrid_inverter_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ja/Nein", None))
        self.inverter_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.commiss_date_label.setText(QCoreApplication.translate("MainWindow", u"Datum erstmalige\n"
"Inbetriebnahme:", None))
        self.inverter_power_label.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete\n"
"Wechselrichterleistung [kW]:", None))
        self.inverter_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.headline_04.setText(QCoreApplication.translate("MainWindow", u"Batteriewechselrichter", None))
        ___qtablewidgetitem16 = self.BAT_inverters_list.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem17 = self.BAT_inverters_list.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem18 = self.BAT_inverters_list.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Wechselrichter-Typ", None));
        ___qtablewidgetitem19 = self.BAT_inverters_list.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Anzahl [Stk.]", None));
        ___qtablewidgetitem20 = self.BAT_inverters_list.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem21 = self.BAT_inverters_list.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete \n"
"WR-Leistung [kW]", None));
        ___qtablewidgetitem22 = self.BAT_inverters_list.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Art der Kopplung", None));
        self.move_none_BAT_inverters_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.bat_inverter_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.coupling_type_label.setText(QCoreApplication.translate("MainWindow", u"Art der Kopplung:", None))
        self.bat_inverter_power_label.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete\n"
"Wechselrichterleistung [kW]:", None))
        self.bat_inverter_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.coupling_type_text.setPlainText(QCoreApplication.translate("MainWindow", u"AC gekoppeltes System", None))
        self.headline_05.setText(QCoreApplication.translate("MainWindow", u"Speicher", None))
        ___qtablewidgetitem23 = self.BAT_storage_list.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem24 = self.BAT_storage_list.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem25 = self.BAT_storage_list.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Speicher-Typ", None));
        ___qtablewidgetitem26 = self.BAT_storage_list.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Anzahl [Stk.]", None));
        ___qtablewidgetitem27 = self.BAT_storage_list.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem28 = self.BAT_storage_list.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Nutzbare \n"
"Speicherkapazit\u00e4t\n"
"[kWh]", None));
        ___qtablewidgetitem29 = self.BAT_storage_list.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Max. Entladeleistung\n"
"im Dauerbetrieb", None));
        ___qtablewidgetitem30 = self.BAT_storage_list.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Batterietechnologie", None));
        self.move_none_BAT_storage_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.em_pow_ability_bool_label.setText(QCoreApplication.translate("MainWindow", u"Notstromf\u00e4higkeit\n"
"bei Netzst\u00f6rungen: ", None))
        self.bat_storage_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.bat_storage_cap_label.setText(QCoreApplication.translate("MainWindow", u"Nutzbare\n"
"Speicherkapazit\u00e4t:", None))
        self.bat_storage_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.bat_commiss_date_label.setText(QCoreApplication.translate("MainWindow", u"Datum erstmalige\n"
"Inbetriebnahme:", None))
        self.energy_storage_type_label.setText(QCoreApplication.translate("MainWindow", u"Technologie der \n"
"Stromspeicherung:", None))
        self.bat_technology_label.setText(QCoreApplication.translate("MainWindow", u"Batterietechnologie:", None))
        self.em_pow_ability_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ja/Nein", None))
        self.max_discharge_pow_label.setText(QCoreApplication.translate("MainWindow", u"Maximale Entladeleistung \n"
"im Dauerbetrieb:", None))
        self.headline_06.setText(QCoreApplication.translate("MainWindow", u"Ladestation", None))
        ___qtablewidgetitem31 = self.CHG_point_list.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem32 = self.CHG_point_list.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem33 = self.CHG_point_list.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Ladestations-Typ", None));
        ___qtablewidgetitem34 = self.CHG_point_list.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Anzahl [Stk.]", None));
        ___qtablewidgetitem35 = self.CHG_point_list.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        self.move_none_CHG_point_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.charging_point_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.charging_point_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.headline_07.setText(QCoreApplication.translate("MainWindow", u"Anschlussart", None))
        self.feeding_type_label.setText(QCoreApplication.translate("MainWindow", u"Einspeisung:", None))
        self.feeding_type_text.setPlainText(QCoreApplication.translate("MainWindow", u"Volleinspeisung / Teileinspeisung (einschlie\u00dflich Eigenverbrauch) ", None))
        self.headline_08.setText(QCoreApplication.translate("MainWindow", u"Weitere Anlageneigenschaften", None))
        self.rmt_drct_mrktr_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.pow_limit_bool_label.setText(QCoreApplication.translate("MainWindow", u"Leistungsbegrenzung:", None))
        self.rmt_drct_mrktr_bool_label.setText(QCoreApplication.translate("MainWindow", u"Fernsteuerbarkeit\n"
"durch Direktvermarkter:", None))
        self.pow_limit_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.tendering_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.prequali_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.tendering_bool_label.setText(QCoreApplication.translate("MainWindow", u"Erlangung der PV-Anlage \u00fcber \n"
"Zuschlag in einer Ausschreibung:", None))
        self.prequali_bool_label.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e4qualifikation\n"
"f\u00fcr Regelenergie:", None))
        self.rmt_grd_op_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.rmt_grd_op_bool_label.setText(QCoreApplication.translate("MainWindow", u"Fernsteuerbarkeit\n"
"durch Netzbetreiber:", None))
        self.rmt_3rd_prt_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.rmt_3rd_prt_bool_label.setText(QCoreApplication.translate("MainWindow", u"Fernsteuerbarkeit\n"
"durch Dritte:", None))
        self.citizen_corp_bool_label.setText(QCoreApplication.translate("MainWindow", u"Anlagenbetreiber ist eine \n"
"B\u00fcrgerenergiegesellschaft:", None))
        self.citizen_corp_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.headline_09.setText(QCoreApplication.translate("MainWindow", u"AC-seitige Komponenten", None))
        self.meter_box_type_label.setText(QCoreApplication.translate("MainWindow", u"Energiez\u00e4hler:", None))
        self.meter_cabinet_label.setText(QCoreApplication.translate("MainWindow", u"Z\u00e4hlerschrank:", None))
        self.headline_10.setText(QCoreApplication.translate("MainWindow", u"Kommunikation und Anlagen\u00fcberwachung", None))
        self.dl_connect_ext_label.setText(QCoreApplication.translate("MainWindow", u"Externer Zugriff:", None))
        self.dl_type_label.setText(QCoreApplication.translate("MainWindow", u"Datenlogger:", None))
        self.source_btn_docu.setText(QCoreApplication.translate("MainWindow", u"Template Dokumentation", None))
        self.target_path_btn_2.setText(QCoreApplication.translate("MainWindow", u"Ablagepfad f\u00fcr \n"
"Dokumente ausw\u00e4hlen", None))
        self.source_btn_matstr.setText(QCoreApplication.translate("MainWindow", u"Template gem. MatStR", None))
        self.create_docs_btn.setText(QCoreApplication.translate("MainWindow", u"Doku gem\u00e4\u00df\n"
"MaStR erzeugen", None))
        self.load_data_to_device_lists.setText(QCoreApplication.translate("MainWindow", u"1. F\u00fclle Ger\u00e4telisten (WR-, BWR-, Batterie- und Ladestationsliste)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Doku gem. MatStR", None))
        self.server_sttings_headline_label.setText(QCoreApplication.translate("MainWindow", u"Servereinstellungen", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datenbanktyp:", None))
        self.db_type.setItemText(0, QCoreApplication.translate("MainWindow", u"PostgreSQL", None))
        self.db_type.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL", None))

        self.db_name_label.setText(QCoreApplication.translate("MainWindow", u"Datenbankname:", None))
        self.db_server_label.setText(QCoreApplication.translate("MainWindow", u"Server:Port:", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.pw_label.setText(QCoreApplication.translate("MainWindow", u"Passwort:", None))
        self.server_sttings_headline_label_2.setText(QCoreApplication.translate("MainWindow", u"Queries zur Abfrage von Datenbank", None))
        self.sql_query_btn.setText(QCoreApplication.translate("MainWindow", u"Datenbank-Abfrage eingeben (\u00dcbertragung von Doklumenten)", None))
        self.query_input.setPlainText("")
        self.sql_query_2_btn.setText(QCoreApplication.translate("MainWindow", u"Datenbank-Abfrage eingeben (Doku gem. MatStR)", None))
        self.query_2_input.setPlainText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Projektnummer:", None))
        self.project_name_label.setText(QCoreApplication.translate("MainWindow", u"Projektname:", None))
        self.project.setPlainText(QCoreApplication.translate("MainWindow", u"SUN 24-001", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

