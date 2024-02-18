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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 609)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
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
        self.gridLayout_3.setHorizontalSpacing(50)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.load_articles_db_btn = QPushButton(self.tab1)
        self.load_articles_db_btn.setObjectName(u"load_articles_db_btn")
        self.load_articles_db_btn.setMinimumSize(QSize(0, 40))
        self.load_articles_db_btn.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setUnderline(False)
        self.load_articles_db_btn.setFont(font)

        self.gridLayout_4.addWidget(self.load_articles_db_btn, 0, 3, 1, 1)

        self.load_articles_file_btn = QPushButton(self.tab1)
        self.load_articles_file_btn.setObjectName(u"load_articles_file_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.load_articles_file_btn.sizePolicy().hasHeightForWidth())
        self.load_articles_file_btn.setSizePolicy(sizePolicy1)
        self.load_articles_file_btn.setMinimumSize(QSize(0, 40))
        self.load_articles_file_btn.setMaximumSize(QSize(150, 40))
        self.load_articles_file_btn.setFont(font)
        self.load_articles_file_btn.setCheckable(False)
        self.load_articles_file_btn.setChecked(False)
        self.load_articles_file_btn.setAutoDefault(False)
        self.load_articles_file_btn.setFlat(False)

        self.gridLayout_4.addWidget(self.load_articles_file_btn, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.line_2 = QFrame(self.tab1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.articles_list = QTableWidget(self.tab1)
        if (self.articles_list.columnCount() < 3):
            self.articles_list.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.articles_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.articles_list.setObjectName(u"articles_list")
        self.articles_list.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.articles_list.sizePolicy().hasHeightForWidth())
        self.articles_list.setSizePolicy(sizePolicy2)
        self.articles_list.setMinimumSize(QSize(0, 150))
        self.articles_list.setCornerButtonEnabled(True)
        self.articles_list.horizontalHeader().setVisible(True)
        self.articles_list.horizontalHeader().setCascadingSectionResizes(True)
        self.articles_list.horizontalHeader().setMinimumSectionSize(10)
        self.articles_list.horizontalHeader().setDefaultSectionSize(50)
        self.articles_list.horizontalHeader().setHighlightSections(False)
        self.articles_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.articles_list.horizontalHeader().setStretchLastSection(True)
        self.articles_list.verticalHeader().setVisible(False)
        self.articles_list.verticalHeader().setCascadingSectionResizes(False)
        self.articles_list.verticalHeader().setMinimumSectionSize(5)
        self.articles_list.verticalHeader().setProperty("showSortIndicator", False)
        self.articles_list.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.articles_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.db_type = QComboBox(self.tab1)
        self.db_type.addItem("")
        self.db_type.addItem("")
        self.db_type.setObjectName(u"db_type")

        self.horizontalLayout_2.addWidget(self.db_type)

        self.db_server_label = QLabel(self.tab1)
        self.db_server_label.setObjectName(u"db_server_label")

        self.horizontalLayout_2.addWidget(self.db_server_label)

        self.db_server = QPlainTextEdit(self.tab1)
        self.db_server.setObjectName(u"db_server")
        self.db_server.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.db_server)

        self.user_label = QLabel(self.tab1)
        self.user_label.setObjectName(u"user_label")

        self.horizontalLayout_2.addWidget(self.user_label)

        self.user = QPlainTextEdit(self.tab1)
        self.user.setObjectName(u"user")
        self.user.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.user)

        self.pw_label = QLabel(self.tab1)
        self.pw_label.setObjectName(u"pw_label")

        self.horizontalLayout_2.addWidget(self.pw_label)

        self.pw = QPlainTextEdit(self.tab1)
        self.pw.setObjectName(u"pw")
        self.pw.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.pw)

        self.db_name_label = QLabel(self.tab1)
        self.db_name_label.setObjectName(u"db_name_label")

        self.horizontalLayout_2.addWidget(self.db_name_label)

        self.db_name = QPlainTextEdit(self.tab1)
        self.db_name.setObjectName(u"db_name")
        self.db_name.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.db_name)

        self.horizontalLayout_2.setStretch(0, 50)
        self.horizontalLayout_2.setStretch(1, 30)
        self.horizontalLayout_2.setStretch(2, 80)
        self.horizontalLayout_2.setStretch(4, 10)
        self.horizontalLayout_2.setStretch(5, 10)
        self.horizontalLayout_2.setStretch(6, 50)
        self.horizontalLayout_2.setStretch(8, 50)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.sql_query_btn = QPushButton(self.tab1)
        self.sql_query_btn.setObjectName(u"sql_query_btn")
        self.sql_query_btn.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.sql_query_btn)

        self.query_input = QPlainTextEdit(self.tab1)
        self.query_input.setObjectName(u"query_input")
        self.query_input.setEnabled(True)
        self.query_input.setMinimumSize(QSize(0, 10))
        self.query_input.setSizeIncrement(QSize(0, 500))
        self.query_input.setAutoFillBackground(True)
        self.query_input.setFrameShadow(QFrame.Raised)
        self.query_input.setTabChangesFocus(False)
        self.query_input.setUndoRedoEnabled(True)
        self.query_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout.addWidget(self.query_input)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.target_path_btn = QPushButton(self.tab1)
        self.target_path_btn.setObjectName(u"target_path_btn")
        sizePolicy1.setHeightForWidth(self.target_path_btn.sizePolicy().hasHeightForWidth())
        self.target_path_btn.setSizePolicy(sizePolicy1)
        self.target_path_btn.setMinimumSize(QSize(135, 30))
        self.target_path_btn.setMaximumSize(QSize(150, 40))
        self.target_path_btn.setAutoDefault(False)
        self.target_path_btn.setFlat(False)

        self.gridLayout_2.addWidget(self.target_path_btn, 3, 0, 1, 1)

        self.target_path_text = QPlainTextEdit(self.tab1)
        self.target_path_text.setObjectName(u"target_path_text")
        self.target_path_text.setMinimumSize(QSize(0, 30))
        self.target_path_text.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.target_path_text, 3, 1, 1, 1)

        self.source_path_btn = QPushButton(self.tab1)
        self.source_path_btn.setObjectName(u"source_path_btn")
        sizePolicy1.setHeightForWidth(self.source_path_btn.sizePolicy().hasHeightForWidth())
        self.source_path_btn.setSizePolicy(sizePolicy1)
        self.source_path_btn.setMinimumSize(QSize(135, 30))
        self.source_path_btn.setMaximumSize(QSize(150, 40))

        self.gridLayout_2.addWidget(self.source_path_btn, 2, 0, 1, 1)

        self.paste_docs_btn = QPushButton(self.tab1)
        self.paste_docs_btn.setObjectName(u"paste_docs_btn")
        sizePolicy1.setHeightForWidth(self.paste_docs_btn.sizePolicy().hasHeightForWidth())
        self.paste_docs_btn.setSizePolicy(sizePolicy1)
        self.paste_docs_btn.setMinimumSize(QSize(135, 50))
        self.paste_docs_btn.setMaximumSize(QSize(150, 100))

        self.gridLayout_2.addWidget(self.paste_docs_btn, 4, 0, 1, 1)

        self.source_path_text = QPlainTextEdit(self.tab1)
        self.source_path_text.setObjectName(u"source_path_text")
        sizePolicy1.setHeightForWidth(self.source_path_text.sizePolicy().hasHeightForWidth())
        self.source_path_text.setSizePolicy(sizePolicy1)
        self.source_path_text.setMinimumSize(QSize(0, 30))
        self.source_path_text.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.source_path_text, 2, 1, 1, 1)

        self.line_3 = QFrame(self.tab1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 50)
        self.verticalLayout.setStretch(2, 10)

        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_4 = QFrame(self.tab_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.sql_query_2_btn = QPushButton(self.tab_2)
        self.sql_query_2_btn.setObjectName(u"sql_query_2_btn")
        self.sql_query_2_btn.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.sql_query_2_btn)

        self.query_2_input = QPlainTextEdit(self.tab_2)
        self.query_2_input.setObjectName(u"query_2_input")
        self.query_2_input.setEnabled(True)
        self.query_2_input.setMinimumSize(QSize(0, 10))
        self.query_2_input.setSizeIncrement(QSize(0, 500))
        self.query_2_input.setAutoFillBackground(True)
        self.query_2_input.setFrameShadow(QFrame.Raised)
        self.query_2_input.setTabChangesFocus(False)
        self.query_2_input.setUndoRedoEnabled(True)
        self.query_2_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_2.addWidget(self.query_2_input)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.creat_doc_1 = QPushButton(self.tab_2)
        self.creat_doc_1.setObjectName(u"creat_doc_1")
        sizePolicy1.setHeightForWidth(self.creat_doc_1.sizePolicy().hasHeightForWidth())
        self.creat_doc_1.setSizePolicy(sizePolicy1)
        self.creat_doc_1.setMinimumSize(QSize(135, 50))
        self.creat_doc_1.setMaximumSize(QSize(150, 100))

        self.gridLayout_6.addWidget(self.creat_doc_1, 3, 0, 1, 1)

        self.target_path_btn_2 = QPushButton(self.tab_2)
        self.target_path_btn_2.setObjectName(u"target_path_btn_2")
        sizePolicy1.setHeightForWidth(self.target_path_btn_2.sizePolicy().hasHeightForWidth())
        self.target_path_btn_2.setSizePolicy(sizePolicy1)
        self.target_path_btn_2.setMinimumSize(QSize(135, 30))
        self.target_path_btn_2.setMaximumSize(QSize(150, 40))
        self.target_path_btn_2.setAutoDefault(False)
        self.target_path_btn_2.setFlat(False)

        self.gridLayout_6.addWidget(self.target_path_btn_2, 2, 0, 1, 1)

        self.target_path_text_2 = QPlainTextEdit(self.tab_2)
        self.target_path_text_2.setObjectName(u"target_path_text_2")
        self.target_path_text_2.setMinimumSize(QSize(0, 30))
        self.target_path_text_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.target_path_text_2, 2, 1, 1, 1)

        self.line_5 = QFrame(self.tab_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_5, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_6)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.project_label = QLabel(self.centralwidget)
        self.project_label.setObjectName(u"project_label")
        sizePolicy1.setHeightForWidth(self.project_label.sizePolicy().hasHeightForWidth())
        self.project_label.setSizePolicy(sizePolicy1)
        self.project_label.setMinimumSize(QSize(0, 0))
        self.project_label.setMaximumSize(QSize(2245, 25))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.project_label.setFont(font1)

        self.horizontalLayout.addWidget(self.project_label)

        self.project = QPlainTextEdit(self.centralwidget)
        self.project.setObjectName(u"project")
        sizePolicy1.setHeightForWidth(self.project.sizePolicy().hasHeightForWidth())
        self.project.setSizePolicy(sizePolicy1)
        self.project.setMinimumSize(QSize(0, 0))
        self.project.setMaximumSize(QSize(16777215, 25))
        self.project.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(12)
        self.project.setFont(font2)
        self.project.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.horizontalLayout.addWidget(self.project)

        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 100)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.load_articles_db_btn.setDefault(True)
        self.load_articles_file_btn.setDefault(True)
        self.sql_query_btn.setDefault(True)
        self.target_path_btn.setDefault(True)
        self.source_path_btn.setDefault(True)
        self.paste_docs_btn.setDefault(True)
        self.sql_query_2_btn.setDefault(True)
        self.creat_doc_1.setDefault(True)
        self.target_path_btn_2.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_articles_db_btn.setText(QCoreApplication.translate("MainWindow", u"Lade Artikelliste f\u00fcr \n"
"das Projekt (aus DB)", None))
        self.load_articles_file_btn.setText(QCoreApplication.translate("MainWindow", u"Lade Artikelliste f\u00fcr\n"
"das Projekt aus Datei", None))
        ___qtablewidgetitem = self.articles_list.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Artikel", None));
        ___qtablewidgetitem1 = self.articles_list.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.db_type.setItemText(0, QCoreApplication.translate("MainWindow", u"PostgreSQL", None))
        self.db_type.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL", None))

        self.db_server_label.setText(QCoreApplication.translate("MainWindow", u"Server (Port)", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.pw_label.setText(QCoreApplication.translate("MainWindow", u"Passwort:", None))
        self.db_name_label.setText(QCoreApplication.translate("MainWindow", u"Datenbankname:", None))
        self.sql_query_btn.setText(QCoreApplication.translate("MainWindow", u"SQL-Query zur DB-Abfrage eingeben", None))
        self.query_input.setPlainText("")
        self.target_path_btn.setText(QCoreApplication.translate("MainWindow", u"Zielpfad festlegen", None))
        self.source_path_btn.setText(QCoreApplication.translate("MainWindow", u"Quellpfad festlegen", None))
        self.paste_docs_btn.setText(QCoreApplication.translate("MainWindow", u"Dokumente \u00fcbertragen", None))
        self.source_path_text.setPlainText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u00dcbertragung von Dokumenten", None))
        self.sql_query_2_btn.setText(QCoreApplication.translate("MainWindow", u"SQL-Query zur DB-Abfrage eingeben", None))
        self.query_2_input.setPlainText("")
        self.creat_doc_1.setText(QCoreApplication.translate("MainWindow", u"Doku gem\u00e4\u00df\n"
"MaStR erzeugen", None))
        self.target_path_btn_2.setText(QCoreApplication.translate("MainWindow", u"Zielpfad festlegen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Doku gem. MatStR", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Projektname:", None))
        self.project.setPlainText(QCoreApplication.translate("MainWindow", u"SUN 24-001", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

