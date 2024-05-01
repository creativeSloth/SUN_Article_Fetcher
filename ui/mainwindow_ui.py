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
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1890, 952)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"/* Allgemeine Stile */\n"
"\n"
"/* Setzt die Standardschrift f\u00fcr alle Elemente */\n"
"* {\n"
"    font: 12pt \"Sitka Heading\";\n"
"}\n"
"\n"
"/* Stil f\u00fcr verschiedene Elemente */\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    padding-left: 10px;\n"
"    color: #13213b; /* Textfarbe */\n"
"    background-color: none; /* Hintergrundfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"}\n"
"\n"
"/* QTextEdit */\n"
"QTextEdit {\n"
"    color: #13213b; /* Textfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"    background-color: rgb(255, 255, 255); /* Hintergrundfarbe */\n"
"    font: 12pt \"Sitka Heading\"; /* Schriftart */\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    color: #13213b; /* Textfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"    background-color: rgb(255, 255, 255); /* Hintergrundfarbe */\n"
"    font: 12pt \"Sitka Heading\"; /* Schriftart */\n"
"	text-align: left;\n"
"}\n"
"\n"
"/* Deaktivierte QTextEdit */\n"
"QPlainTextEdit::disa"
                        "bled {\n"
"    color: #13213b; /* Textfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"    background-color: rgb(144, 216, 216); /* Hintergrundfarbe */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #e21839; /* Hintergrundfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"}\n"
"\n"
"/* QPushButton beim \u00dcberfahren mit der Maus */\n"
"QPushButton::hover {\n"
"    background-color: rgb(170, 18, 43); /* Hintergrundfarbe */\n"
"    color: rgb(71, 71, 71); /* Textfarbe */\n"
"}\n"
"\n"
"/* QPushButton beim Klicken */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 170, 255); /* Hintergrundfarbe */\n"
"    color: white; /* Textfarbe */\n"
"}\n"
"\n"
"/* QFrame und QTabWidget-Panels (Inhalt) */\n"
"\n"
"QFrame#frame0\n"
"{\n"
"    background-color: #13213b; /* Hintergrundfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame#frame010,\n"
"QFrame#frame011\n"
"{\n"
"    background-color: rgb(170, 255, 255); "
                        "/* Hintergrundfarbe */\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"}\n"
"\n"
"QTabWidget,\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: rgb(170, 255, 255); /* Hintergrundfarbe */\n"
"    border-top-right-radius: 5px; /* Abgerundete Ecken */\n"
"    border-bottom-left-radius: 5px; /* Abgerundete Ecken */\n"
"    border-bottom-right-radius: 5px; /* Abgerundete Ecken */\n"
"}\n"
"\n"
"/* Registerkarten im TabBar und deren Ableitungen */\n"
"QTabBar::tab,\n"
"QTabBar::tab:selected,\n"
"QTabBar:tab:!selected {\n"
"    margin: 0.5px; /* Margin */\n"
"    width: 30px; /* Breite */\n"
"    min-height: 50px; /* Mindesth\u00f6he */\n"
"    max-height: 250px; /* Maximale H\u00f6he */\n"
"    padding-top: 10px; /* Padding nur oben */\n"
"    padding-bottom: 10px; /* Padding nur unten */\n"
"    border-top-left-radius: 5px; /* Obere linke Ecke abgerundet */\n"
"    border-bottom-left-radius: 5px; /* Untere linke Ecke abgerundet */\n"
"}\n"
"\n"
"/* Ausgew\u00e4hlte Registerkarten */\n"
"QTabBar::tab:sel"
                        "ected {\n"
"    background-color: rgb(0, 170, 255); /* Hintergrundfarbe */\n"
"    color: rgb(0, 0, 0); /* Textfarbe */\n"
"}\n"
"\n"
"/* Nicht ausgew\u00e4hlte Registerkarten */\n"
"QTabBar:tab:!selected {\n"
"    background-color: rgb(210, 255, 255); /* Hintergrundfarbe */\n"
"    color: rgb(170, 170, 255); /* Textfarbe */\n"
"}\n"
"\n"
"/* Hover-Effekt f\u00fcr nicht ausgew\u00e4hlte Registerkarten */\n"
"QTabBar:tab:!selected::hover {\n"
"    alignment: top; \n"
"    background-color: rgb(0, 255, 255); \n"
"    color: rgb(0, 85, 255); \n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(220, 255, 255);\n"
"    border-radius: 5px; /* Abgerundete Ecken */\n"
"}\n"
"\n"
"QTableWidget::item:alternate {\n"
"    background-color: rgb(240, 255, 255); /* Beispielhintergrundfarbe f\u00fcr alternative Zeilen */\n"
"}\n"
"\n"
"QTableWidget::item:alternate::selected {\n"
"    background-color: rgb(200, 255, 255); /* Beispielhintergrundfarbe f\u00fcr alternative Zeilen */\n"
"	color: #13213b;\n"
"}\n"
"\n"
"QTableW"
                        "idget::item::selected {\n"
"    background-color: rgb(200, 255, 255); /* Beispielhintergrundfarbe f\u00fcr alternative Zeilen */\n"
"	color: #13213b;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(220, 255, 255);\n"
"}\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_3 = QFormLayout(self.centralwidget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.frame0 = QFrame(self.centralwidget)
        self.frame0.setObjectName(u"frame0")
        sizePolicy.setHeightForWidth(self.frame0.sizePolicy().hasHeightForWidth())
        self.frame0.setSizePolicy(sizePolicy)
        self.frame0.setStyleSheet(u"")
        self.frame0.setFrameShape(QFrame.StyledPanel)
        self.frame0.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame0)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.frame01 = QFrame(self.frame0)
        self.frame01.setObjectName(u"frame01")
        sizePolicy.setHeightForWidth(self.frame01.sizePolicy().hasHeightForWidth())
        self.frame01.setSizePolicy(sizePolicy)
        self.frame01.setMaximumSize(QSize(16777215, 60))
        self.frame01.setFrameShape(QFrame.StyledPanel)
        self.frame01.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame01)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame010 = QFrame(self.frame01)
        self.frame010.setObjectName(u"frame010")
        sizePolicy.setHeightForWidth(self.frame010.sizePolicy().hasHeightForWidth())
        self.frame010.setSizePolicy(sizePolicy)
        self.frame010.setMinimumSize(QSize(200, 40))
        self.frame010.setMaximumSize(QSize(400, 40))
        self.frame010.setFrameShape(QFrame.StyledPanel)
        self.frame010.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame010)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.project_label = QLabel(self.frame010)
        self.project_label.setObjectName(u"project_label")
        sizePolicy.setHeightForWidth(self.project_label.sizePolicy().hasHeightForWidth())
        self.project_label.setSizePolicy(sizePolicy)
        self.project_label.setMinimumSize(QSize(100, 30))
        self.project_label.setMaximumSize(QSize(150, 30))
        self.project_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Sitka Heading"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.project_label.setFont(font)
        self.project_label.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.project_label)

        self.project = QPlainTextEdit(self.frame010)
        self.project.setObjectName(u"project")
        self.project.setMinimumSize(QSize(150, 30))
        self.project.setMaximumSize(QSize(200, 30))
        self.project.setFont(font)
        self.project.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.project.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.project.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.project.setTabChangesFocus(False)

        self.horizontalLayout_5.addWidget(self.project)


        self.horizontalLayout_10.addWidget(self.frame010)

        self.frame011 = QFrame(self.frame01)
        self.frame011.setObjectName(u"frame011")
        self.frame011.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame011.sizePolicy().hasHeightForWidth())
        self.frame011.setSizePolicy(sizePolicy1)
        self.frame011.setMinimumSize(QSize(150, 40))
        self.frame011.setMaximumSize(QSize(16777215, 40))
        self.frame011.setFrameShape(QFrame.StyledPanel)
        self.frame011.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame011)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.project_name_label = QLabel(self.frame011)
        self.project_name_label.setObjectName(u"project_name_label")
        sizePolicy.setHeightForWidth(self.project_name_label.sizePolicy().hasHeightForWidth())
        self.project_name_label.setSizePolicy(sizePolicy)
        self.project_name_label.setMinimumSize(QSize(0, 0))
        self.project_name_label.setMaximumSize(QSize(200, 30))
        self.project_name_label.setSizeIncrement(QSize(0, 0))
        self.project_name_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.project_name_label, 0, Qt.AlignVCenter)

        self.project_name = QPlainTextEdit(self.frame011)
        self.project_name.setObjectName(u"project_name")
        self.project_name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.project_name.sizePolicy().hasHeightForWidth())
        self.project_name.setSizePolicy(sizePolicy)
        self.project_name.setMinimumSize(QSize(1200, 30))
        self.project_name.setMaximumSize(QSize(16777215, 30))
        self.project_name.setFont(font)
        self.project_name.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.project_name.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.project_name.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.horizontalLayout_6.addWidget(self.project_name, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.frame011)


        self.gridLayout_4.addWidget(self.frame01, 0, 0, 1, 1)

        self.frame02 = QFrame(self.frame0)
        self.frame02.setObjectName(u"frame02")
        sizePolicy.setHeightForWidth(self.frame02.sizePolicy().hasHeightForWidth())
        self.frame02.setSizePolicy(sizePolicy)
        self.frame02.setFrameShape(QFrame.StyledPanel)
        self.frame02.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame02)
        self.gridLayout_22.setSpacing(5)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.frame02)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(1850, 800))
        self.tabWidget.setMaximumSize(QSize(1850, 16777215))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.West)
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
        self.frame021 = QFrame(self.tab1)
        self.frame021.setObjectName(u"frame021")
        sizePolicy.setHeightForWidth(self.frame021.sizePolicy().hasHeightForWidth())
        self.frame021.setSizePolicy(sizePolicy)
        self.frame021.setFrameShape(QFrame.StyledPanel)
        self.frame021.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame021)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame021)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.load_articles_db_btn = QPushButton(self.frame_6)
        self.load_articles_db_btn.setObjectName(u"load_articles_db_btn")
        self.load_articles_db_btn.setMinimumSize(QSize(300, 40))
        self.load_articles_db_btn.setMaximumSize(QSize(300, 40))
        font1 = QFont()
        font1.setFamilies([u"Sitka Heading"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.load_articles_db_btn.setFont(font1)
        self.load_articles_db_btn.setStyleSheet(u"")
        self.load_articles_db_btn.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.load_articles_db_btn)

        self.load_articles_file_btn = QPushButton(self.frame_6)
        self.load_articles_file_btn.setObjectName(u"load_articles_file_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.load_articles_file_btn.sizePolicy().hasHeightForWidth())
        self.load_articles_file_btn.setSizePolicy(sizePolicy2)
        self.load_articles_file_btn.setMinimumSize(QSize(300, 40))
        self.load_articles_file_btn.setMaximumSize(QSize(300, 40))
        self.load_articles_file_btn.setFont(font1)
        self.load_articles_file_btn.setCheckable(False)
        self.load_articles_file_btn.setChecked(False)
        self.load_articles_file_btn.setAutoDefault(False)
        self.load_articles_file_btn.setFlat(False)

        self.horizontalLayout_7.addWidget(self.load_articles_file_btn)


        self.verticalLayout_7.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.articles_list = QTableWidget(self.frame021)
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
        self.articles_list.setMinimumSize(QSize(1000, 100))
        self.articles_list.setMaximumSize(QSize(16777215, 550))
        self.articles_list.setAutoFillBackground(True)
        self.articles_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.articles_list.setDragDropOverwriteMode(False)
        self.articles_list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.articles_list.setAlternatingRowColors(True)
        self.articles_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.articles_list.setGridStyle(Qt.SolidLine)
        self.articles_list.setSortingEnabled(True)
        self.articles_list.setWordWrap(False)
        self.articles_list.setCornerButtonEnabled(True)
        self.articles_list.horizontalHeader().setVisible(True)
        self.articles_list.horizontalHeader().setCascadingSectionResizes(True)
        self.articles_list.horizontalHeader().setMinimumSectionSize(60)
        self.articles_list.horizontalHeader().setDefaultSectionSize(180)
        self.articles_list.horizontalHeader().setHighlightSections(True)
        self.articles_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.articles_list.horizontalHeader().setStretchLastSection(False)
        self.articles_list.verticalHeader().setVisible(False)
        self.articles_list.verticalHeader().setCascadingSectionResizes(False)
        self.articles_list.verticalHeader().setMinimumSectionSize(5)
        self.articles_list.verticalHeader().setHighlightSections(True)
        self.articles_list.verticalHeader().setProperty("showSortIndicator", True)
        self.articles_list.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.articles_list)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.frame = QFrame(self.frame021)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 120))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.source_path_btn = QPushButton(self.frame_2)
        self.source_path_btn.setObjectName(u"source_path_btn")
        sizePolicy2.setHeightForWidth(self.source_path_btn.sizePolicy().hasHeightForWidth())
        self.source_path_btn.setSizePolicy(sizePolicy2)
        self.source_path_btn.setMinimumSize(QSize(135, 30))
        self.source_path_btn.setMaximumSize(QSize(300, 40))
        self.source_path_btn.setAutoDefault(False)

        self.horizontalLayout_8.addWidget(self.source_path_btn)

        self.source_path_text = QPlainTextEdit(self.frame_2)
        self.source_path_text.setObjectName(u"source_path_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.source_path_text.sizePolicy().hasHeightForWidth())
        self.source_path_text.setSizePolicy(sizePolicy3)
        self.source_path_text.setMinimumSize(QSize(0, 30))
        self.source_path_text.setMaximumSize(QSize(4556, 40))

        self.horizontalLayout_8.addWidget(self.source_path_text)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.target_path_btn = QPushButton(self.frame_3)
        self.target_path_btn.setObjectName(u"target_path_btn")
        sizePolicy2.setHeightForWidth(self.target_path_btn.sizePolicy().hasHeightForWidth())
        self.target_path_btn.setSizePolicy(sizePolicy2)
        self.target_path_btn.setMinimumSize(QSize(135, 30))
        self.target_path_btn.setMaximumSize(QSize(300, 40))
        self.target_path_btn.setAutoDefault(False)
        self.target_path_btn.setFlat(False)

        self.horizontalLayout_9.addWidget(self.target_path_btn)

        self.target_path_text = QPlainTextEdit(self.frame_3)
        self.target_path_text.setObjectName(u"target_path_text")
        sizePolicy3.setHeightForWidth(self.target_path_text.sizePolicy().hasHeightForWidth())
        self.target_path_text.setSizePolicy(sizePolicy3)
        self.target_path_text.setMinimumSize(QSize(0, 30))
        self.target_path_text.setMaximumSize(QSize(4556, 40))

        self.horizontalLayout_9.addWidget(self.target_path_text)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.paste_docs_btn = QPushButton(self.frame)
        self.paste_docs_btn.setObjectName(u"paste_docs_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(200)
        sizePolicy4.setVerticalStretch(200)
        sizePolicy4.setHeightForWidth(self.paste_docs_btn.sizePolicy().hasHeightForWidth())
        self.paste_docs_btn.setSizePolicy(sizePolicy4)
        self.paste_docs_btn.setMinimumSize(QSize(135, 50))
        self.paste_docs_btn.setMaximumSize(QSize(500, 60))
        font2 = QFont()
        font2.setFamilies([u"Sitka Heading"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.paste_docs_btn.setFont(font2)
        self.paste_docs_btn.setAutoDefault(False)
        self.paste_docs_btn.setFlat(False)

        self.verticalLayout_6.addWidget(self.paste_docs_btn)


        self.verticalLayout_7.addWidget(self.frame)


        self.gridLayout_3.addWidget(self.frame021, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), u"\u00dcbertragung von Dokumenten")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tab2.setMinimumSize(QSize(1200, 0))
        self.layoutWidget = QWidget(self.tab2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1802, 826))
        self.frame0220 = QVBoxLayout(self.layoutWidget)
        self.frame0220.setSpacing(10)
        self.frame0220.setObjectName(u"frame0220")
        self.frame0220.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.layoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(1800, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -411, 1781, 4892))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame0221 = QFrame(self.scrollAreaWidgetContents)
        self.frame0221.setObjectName(u"frame0221")
        self.frame0221.setFrameShape(QFrame.StyledPanel)
        self.frame0221.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame0221)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.headline_01 = QLabel(self.frame0221)
        self.headline_01.setObjectName(u"headline_01")
        self.headline_01.setMinimumSize(QSize(250, 50))
        self.headline_01.setFont(font1)
        self.headline_01.setLayoutDirection(Qt.LeftToRight)
        self.headline_01.setAutoFillBackground(False)
        self.headline_01.setFrameShape(QFrame.StyledPanel)
        self.headline_01.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_01)

        self.frame1 = QFrame(self.frame0221)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.frame1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.op_adress_3_label = QLabel(self.frame_8)
        self.op_adress_3_label.setObjectName(u"op_adress_3_label")
        self.op_adress_3_label.setMinimumSize(QSize(0, 30))
        self.op_adress_3_label.setMaximumSize(QSize(16777209, 30))
        self.op_adress_3_label.setFont(font)

        self.gridLayout_11.addWidget(self.op_adress_3_label, 0, 0, 1, 1)

        self.operator_text = QPlainTextEdit(self.frame_8)
        self.operator_text.setObjectName(u"operator_text")
        self.operator_text.setMinimumSize(QSize(0, 30))
        self.operator_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.operator_text, 0, 1, 1, 1)

        self.op_adress_1_label = QLabel(self.frame_8)
        self.op_adress_1_label.setObjectName(u"op_adress_1_label")
        self.op_adress_1_label.setMinimumSize(QSize(0, 30))
        self.op_adress_1_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.op_adress_1_label, 1, 0, 1, 1)

        self.op_adress_1_text = QPlainTextEdit(self.frame_8)
        self.op_adress_1_text.setObjectName(u"op_adress_1_text")
        self.op_adress_1_text.setMinimumSize(QSize(0, 30))
        self.op_adress_1_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.op_adress_1_text, 1, 1, 1, 1)

        self.op_adress_2_label = QLabel(self.frame_8)
        self.op_adress_2_label.setObjectName(u"op_adress_2_label")
        self.op_adress_2_label.setMinimumSize(QSize(0, 30))
        self.op_adress_2_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.op_adress_2_label, 2, 0, 1, 1)

        self.op_adress_3_text = QPlainTextEdit(self.frame_8)
        self.op_adress_3_text.setObjectName(u"op_adress_3_text")
        self.op_adress_3_text.setMinimumSize(QSize(0, 30))
        self.op_adress_3_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.op_adress_3_text, 2, 1, 1, 1)

        self.op_adress_3_label_2 = QLabel(self.frame_8)
        self.op_adress_3_label_2.setObjectName(u"op_adress_3_label_2")
        self.op_adress_3_label_2.setMinimumSize(QSize(0, 30))
        self.op_adress_3_label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.op_adress_3_label_2, 3, 0, 1, 1)

        self.op_adress_2_text = QPlainTextEdit(self.frame_8)
        self.op_adress_2_text.setObjectName(u"op_adress_2_text")
        self.op_adress_2_text.setMinimumSize(QSize(0, 30))
        self.op_adress_2_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.op_adress_2_text, 3, 1, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.frame_8)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_5)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.loc_head_label = QLabel(self.frame_5)
        self.loc_head_label.setObjectName(u"loc_head_label")
        self.loc_head_label.setMinimumSize(QSize(0, 30))
        self.loc_head_label.setMaximumSize(QSize(16777215, 30))
        self.loc_head_label.setFont(font)

        self.gridLayout_23.addWidget(self.loc_head_label, 0, 0, 1, 1)

        self.loc_adress_1_label = QLabel(self.frame_5)
        self.loc_adress_1_label.setObjectName(u"loc_adress_1_label")
        self.loc_adress_1_label.setMinimumSize(QSize(0, 30))
        self.loc_adress_1_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.loc_adress_1_label, 1, 0, 1, 1)

        self.loc_adress_1_text = QPlainTextEdit(self.frame_5)
        self.loc_adress_1_text.setObjectName(u"loc_adress_1_text")
        self.loc_adress_1_text.setMinimumSize(QSize(0, 30))
        self.loc_adress_1_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.loc_adress_1_text, 1, 1, 1, 1)

        self.loc_adress_2_label = QLabel(self.frame_5)
        self.loc_adress_2_label.setObjectName(u"loc_adress_2_label")
        self.loc_adress_2_label.setMinimumSize(QSize(0, 30))
        self.loc_adress_2_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.loc_adress_2_label, 2, 0, 1, 1)

        self.loc_adress_2_text = QPlainTextEdit(self.frame_5)
        self.loc_adress_2_text.setObjectName(u"loc_adress_2_text")
        self.loc_adress_2_text.setMinimumSize(QSize(0, 30))
        self.loc_adress_2_text.setMaximumSize(QSize(16777215, 30))
        self.loc_adress_2_text.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_23.addWidget(self.loc_adress_2_text, 2, 1, 1, 1)

        self.loc_adress_3_label = QLabel(self.frame_5)
        self.loc_adress_3_label.setObjectName(u"loc_adress_3_label")
        self.loc_adress_3_label.setMinimumSize(QSize(0, 30))
        self.loc_adress_3_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.loc_adress_3_label, 3, 0, 1, 1)

        self.loc_adress_3_text = QPlainTextEdit(self.frame_5)
        self.loc_adress_3_text.setObjectName(u"loc_adress_3_text")
        self.loc_adress_3_text.setMinimumSize(QSize(0, 30))
        self.loc_adress_3_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.loc_adress_3_text, 3, 1, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame_5)


        self.gridLayout_2.addWidget(self.frame_7, 2, 0, 2, 1)

        self.frame_13 = QFrame(self.frame1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sys_perf_label = QLabel(self.frame_12)
        self.sys_perf_label.setObjectName(u"sys_perf_label")
        self.sys_perf_label.setMinimumSize(QSize(0, 30))
        self.sys_perf_label.setMaximumSize(QSize(16777215, 30))
        self.sys_perf_label.setFont(font)

        self.horizontalLayout_12.addWidget(self.sys_perf_label)

        self.sys_perf_text = QPlainTextEdit(self.frame_12)
        self.sys_perf_text.setObjectName(u"sys_perf_text")
        self.sys_perf_text.setMinimumSize(QSize(0, 30))
        self.sys_perf_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_12.addWidget(self.sys_perf_text)


        self.horizontalLayout_13.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.constr_style_label = QLabel(self.frame_11)
        self.constr_style_label.setObjectName(u"constr_style_label")
        self.constr_style_label.setMinimumSize(QSize(0, 30))
        self.constr_style_label.setMaximumSize(QSize(16777215, 30))
        self.constr_style_label.setFont(font)

        self.horizontalLayout_11.addWidget(self.constr_style_label)

        self.constr_style_text = QPlainTextEdit(self.frame_11)
        self.constr_style_text.setObjectName(u"constr_style_text")
        self.constr_style_text.setMinimumSize(QSize(0, 30))
        self.constr_style_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_11.addWidget(self.constr_style_text)


        self.horizontalLayout_13.addWidget(self.frame_11)


        self.gridLayout_2.addWidget(self.frame_13, 4, 0, 1, 1)

        self.frame_9 = QFrame(self.frame1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.azimuth_head_label = QLabel(self.frame_9)
        self.azimuth_head_label.setObjectName(u"azimuth_head_label")
        self.azimuth_head_label.setFont(font)

        self.verticalLayout_2.addWidget(self.azimuth_head_label)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.bool_consist_azimuth_label = QLabel(self.frame_14)
        self.bool_consist_azimuth_label.setObjectName(u"bool_consist_azimuth_label")
        self.bool_consist_azimuth_label.setMinimumSize(QSize(0, 30))
        self.bool_consist_azimuth_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_14.addWidget(self.bool_consist_azimuth_label)

        self.bool_consist_azimuth_text = QPlainTextEdit(self.frame_14)
        self.bool_consist_azimuth_text.setObjectName(u"bool_consist_azimuth_text")
        sizePolicy.setHeightForWidth(self.bool_consist_azimuth_text.sizePolicy().hasHeightForWidth())
        self.bool_consist_azimuth_text.setSizePolicy(sizePolicy)
        self.bool_consist_azimuth_text.setMinimumSize(QSize(0, 30))
        self.bool_consist_azimuth_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_14.addWidget(self.bool_consist_azimuth_text)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_15)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.min_tilt_text = QPlainTextEdit(self.frame_15)
        self.min_tilt_text.setObjectName(u"min_tilt_text")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.min_tilt_text.sizePolicy().hasHeightForWidth())
        self.min_tilt_text.setSizePolicy(sizePolicy5)
        self.min_tilt_text.setMinimumSize(QSize(0, 30))
        self.min_tilt_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.min_tilt_text, 2, 4, 1, 1)

        self.maj_card_point_label = QLabel(self.frame_15)
        self.maj_card_point_label.setObjectName(u"maj_card_point_label")

        self.gridLayout_7.addWidget(self.maj_card_point_label, 0, 3, 1, 1)

        self.min_azimuth_label = QLabel(self.frame_15)
        self.min_azimuth_label.setObjectName(u"min_azimuth_label")
        self.min_azimuth_label.setMinimumSize(QSize(0, 30))
        self.min_azimuth_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.min_azimuth_label, 1, 0, 1, 1)

        self.min_tilt_label = QLabel(self.frame_15)
        self.min_tilt_label.setObjectName(u"min_tilt_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.min_tilt_label.sizePolicy().hasHeightForWidth())
        self.min_tilt_label.setSizePolicy(sizePolicy6)
        self.min_tilt_label.setMinimumSize(QSize(0, 30))
        self.min_tilt_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.min_tilt_label, 2, 3, 1, 1)

        self.maj_tilt_text = QPlainTextEdit(self.frame_15)
        self.maj_tilt_text.setObjectName(u"maj_tilt_text")
        sizePolicy5.setHeightForWidth(self.maj_tilt_text.sizePolicy().hasHeightForWidth())
        self.maj_tilt_text.setSizePolicy(sizePolicy5)
        self.maj_tilt_text.setMinimumSize(QSize(0, 30))
        self.maj_tilt_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.maj_tilt_text, 2, 2, 1, 1)

        self.min_card_point_text = QPlainTextEdit(self.frame_15)
        self.min_card_point_text.setObjectName(u"min_card_point_text")
        self.min_card_point_text.setMinimumSize(QSize(0, 30))
        self.min_card_point_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.min_card_point_text, 1, 4, 1, 1)

        self.min_card_point_label = QLabel(self.frame_15)
        self.min_card_point_label.setObjectName(u"min_card_point_label")

        self.gridLayout_7.addWidget(self.min_card_point_label, 1, 3, 1, 1)

        self.maj_azimuth_text = QPlainTextEdit(self.frame_15)
        self.maj_azimuth_text.setObjectName(u"maj_azimuth_text")
        self.maj_azimuth_text.setMinimumSize(QSize(0, 30))
        self.maj_azimuth_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.maj_azimuth_text, 0, 2, 1, 1)

        self.maj_azimuth_label = QLabel(self.frame_15)
        self.maj_azimuth_label.setObjectName(u"maj_azimuth_label")
        self.maj_azimuth_label.setMinimumSize(QSize(0, 30))
        self.maj_azimuth_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.maj_azimuth_label, 0, 0, 1, 1)

        self.min_azimuth_text = QPlainTextEdit(self.frame_15)
        self.min_azimuth_text.setObjectName(u"min_azimuth_text")
        self.min_azimuth_text.setMinimumSize(QSize(0, 30))
        self.min_azimuth_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.min_azimuth_text, 1, 2, 1, 1)

        self.maj_card_point_text = QPlainTextEdit(self.frame_15)
        self.maj_card_point_text.setObjectName(u"maj_card_point_text")
        self.maj_card_point_text.setMinimumSize(QSize(0, 30))
        self.maj_card_point_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.maj_card_point_text, 0, 4, 1, 1)

        self.maj_tilt_label = QLabel(self.frame_15)
        self.maj_tilt_label.setObjectName(u"maj_tilt_label")
        sizePolicy6.setHeightForWidth(self.maj_tilt_label.sizePolicy().hasHeightForWidth())
        self.maj_tilt_label.setSizePolicy(sizePolicy6)
        self.maj_tilt_label.setMinimumSize(QSize(0, 30))
        self.maj_tilt_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.maj_tilt_label, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.gridLayout_2.addWidget(self.frame_9, 5, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame1)

        self.headline_02 = QLabel(self.frame0221)
        self.headline_02.setObjectName(u"headline_02")
        self.headline_02.setMinimumSize(QSize(250, 50))
        self.headline_02.setFont(font)
        self.headline_02.setFrameShape(QFrame.StyledPanel)
        self.headline_02.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_02)

        self.PV_modules_list = QTableWidget(self.frame0221)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.PV_modules_list.sizePolicy().hasHeightForWidth())
        self.PV_modules_list.setSizePolicy(sizePolicy7)
        self.PV_modules_list.setMinimumSize(QSize(0, 400))
        self.PV_modules_list.setMaximumSize(QSize(1800, 16777215))
        self.PV_modules_list.setAutoFillBackground(False)
        self.PV_modules_list.setFrameShape(QFrame.StyledPanel)
        self.PV_modules_list.setMidLineWidth(1)
        self.PV_modules_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.PV_modules_list.setDragDropOverwriteMode(False)
        self.PV_modules_list.setAlternatingRowColors(True)
        self.PV_modules_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PV_modules_list.setGridStyle(Qt.DashDotDotLine)
        self.PV_modules_list.setSortingEnabled(True)
        self.PV_modules_list.setWordWrap(False)
        self.PV_modules_list.setCornerButtonEnabled(False)
        self.PV_modules_list.horizontalHeader().setMinimumSectionSize(50)
        self.PV_modules_list.horizontalHeader().setDefaultSectionSize(150)
        self.PV_modules_list.verticalHeader().setVisible(False)
        self.PV_modules_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.PV_modules_list)

        self.frame_4 = QFrame(self.frame0221)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.move_none_PV_modules_to_blacklist = QPushButton(self.frame_4)
        self.move_none_PV_modules_to_blacklist.setObjectName(u"move_none_PV_modules_to_blacklist")
        self.move_none_PV_modules_to_blacklist.setMinimumSize(QSize(100, 30))

        self.verticalLayout_8.addWidget(self.move_none_PV_modules_to_blacklist)

        self.frame_16 = QFrame(self.frame_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.module_count_label = QLabel(self.frame_16)
        self.module_count_label.setObjectName(u"module_count_label")
        sizePolicy6.setHeightForWidth(self.module_count_label.sizePolicy().hasHeightForWidth())
        self.module_count_label.setSizePolicy(sizePolicy6)
        self.module_count_label.setMinimumSize(QSize(150, 30))
        self.module_count_label.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_3.addWidget(self.module_count_label)

        self.module_count_text = QPlainTextEdit(self.frame_16)
        self.module_count_text.setObjectName(u"module_count_text")
        sizePolicy.setHeightForWidth(self.module_count_text.sizePolicy().hasHeightForWidth())
        self.module_count_text.setSizePolicy(sizePolicy)
        self.module_count_text.setMinimumSize(QSize(0, 30))
        self.module_count_text.setMaximumSize(QSize(75, 30))

        self.horizontalLayout_3.addWidget(self.module_count_text)

        self.module_type_label = QLabel(self.frame_16)
        self.module_type_label.setObjectName(u"module_type_label")
        sizePolicy6.setHeightForWidth(self.module_type_label.sizePolicy().hasHeightForWidth())
        self.module_type_label.setSizePolicy(sizePolicy6)
        self.module_type_label.setMinimumSize(QSize(0, 30))
        self.module_type_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.module_type_label)

        self.module_type_text = QPlainTextEdit(self.frame_16)
        self.module_type_text.setObjectName(u"module_type_text")
        sizePolicy5.setHeightForWidth(self.module_type_text.sizePolicy().hasHeightForWidth())
        self.module_type_text.setSizePolicy(sizePolicy5)
        self.module_type_text.setMinimumSize(QSize(0, 30))
        self.module_type_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.module_type_text)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.mounting_type_label = QLabel(self.frame_17)
        self.mounting_type_label.setObjectName(u"mounting_type_label")
        sizePolicy6.setHeightForWidth(self.mounting_type_label.sizePolicy().hasHeightForWidth())
        self.mounting_type_label.setSizePolicy(sizePolicy6)
        self.mounting_type_label.setMinimumSize(QSize(0, 30))
        self.mounting_type_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_16.addWidget(self.mounting_type_label)

        self.mounting_type_text = QPlainTextEdit(self.frame_17)
        self.mounting_type_text.setObjectName(u"mounting_type_text")
        sizePolicy5.setHeightForWidth(self.mounting_type_text.sizePolicy().hasHeightForWidth())
        self.mounting_type_text.setSizePolicy(sizePolicy5)
        self.mounting_type_text.setMinimumSize(QSize(0, 30))
        self.mounting_type_text.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_16.addWidget(self.mounting_type_text)


        self.verticalLayout_8.addWidget(self.frame_17)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.headline_03 = QLabel(self.frame0221)
        self.headline_03.setObjectName(u"headline_03")
        self.headline_03.setMinimumSize(QSize(250, 50))
        self.headline_03.setFont(font)
        self.headline_03.setFrameShape(QFrame.StyledPanel)
        self.headline_03.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_03)

        self.PV_inverters_list = QTableWidget(self.frame0221)
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
        sizePolicy7.setHeightForWidth(self.PV_inverters_list.sizePolicy().hasHeightForWidth())
        self.PV_inverters_list.setSizePolicy(sizePolicy7)
        self.PV_inverters_list.setMinimumSize(QSize(0, 400))
        self.PV_inverters_list.setMaximumSize(QSize(1800, 16777215))
        self.PV_inverters_list.setAutoFillBackground(False)
        self.PV_inverters_list.setFrameShape(QFrame.StyledPanel)
        self.PV_inverters_list.setMidLineWidth(1)
        self.PV_inverters_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.PV_inverters_list.setDragDropOverwriteMode(False)
        self.PV_inverters_list.setAlternatingRowColors(True)
        self.PV_inverters_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PV_inverters_list.setGridStyle(Qt.DashDotDotLine)
        self.PV_inverters_list.setSortingEnabled(True)
        self.PV_inverters_list.setWordWrap(False)
        self.PV_inverters_list.setCornerButtonEnabled(False)
        self.PV_inverters_list.horizontalHeader().setMinimumSectionSize(50)
        self.PV_inverters_list.horizontalHeader().setDefaultSectionSize(150)
        self.PV_inverters_list.verticalHeader().setVisible(False)
        self.PV_inverters_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.PV_inverters_list)

        self.frame_18 = QFrame(self.frame0221)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.move_none_PV_inverters_to_blacklist = QPushButton(self.frame_18)
        self.move_none_PV_inverters_to_blacklist.setObjectName(u"move_none_PV_inverters_to_blacklist")
        self.move_none_PV_inverters_to_blacklist.setMinimumSize(QSize(100, 30))

        self.verticalLayout_9.addWidget(self.move_none_PV_inverters_to_blacklist)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.splitter = QSplitter(self.frame_19)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.hybrid_inverter_bool_label = QLabel(self.splitter)
        self.hybrid_inverter_bool_label.setObjectName(u"hybrid_inverter_bool_label")
        sizePolicy.setHeightForWidth(self.hybrid_inverter_bool_label.sizePolicy().hasHeightForWidth())
        self.hybrid_inverter_bool_label.setSizePolicy(sizePolicy)
        self.hybrid_inverter_bool_label.setMinimumSize(QSize(250, 30))
        self.hybrid_inverter_bool_label.setMaximumSize(QSize(350, 30))
        self.splitter.addWidget(self.hybrid_inverter_bool_label)
        self.hybrid_inverter_bool_text = QPlainTextEdit(self.splitter)
        self.hybrid_inverter_bool_text.setObjectName(u"hybrid_inverter_bool_text")
        sizePolicy7.setHeightForWidth(self.hybrid_inverter_bool_text.sizePolicy().hasHeightForWidth())
        self.hybrid_inverter_bool_text.setSizePolicy(sizePolicy7)
        self.hybrid_inverter_bool_text.setMinimumSize(QSize(0, 30))
        self.hybrid_inverter_bool_text.setMaximumSize(QSize(100, 30))
        self.splitter.addWidget(self.hybrid_inverter_bool_text)

        self.horizontalLayout_15.addWidget(self.splitter)


        self.verticalLayout_9.addWidget(self.frame_19, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_20)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.inverter_SN_text = QPlainTextEdit(self.frame_20)
        self.inverter_SN_text.setObjectName(u"inverter_SN_text")
        sizePolicy1.setHeightForWidth(self.inverter_SN_text.sizePolicy().hasHeightForWidth())
        self.inverter_SN_text.setSizePolicy(sizePolicy1)
        self.inverter_SN_text.setMinimumSize(QSize(150, 30))
        self.inverter_SN_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.inverter_SN_text, 0, 5, 1, 1)

        self.commiss_date_label = QLabel(self.frame_20)
        self.commiss_date_label.setObjectName(u"commiss_date_label")
        sizePolicy.setHeightForWidth(self.commiss_date_label.sizePolicy().hasHeightForWidth())
        self.commiss_date_label.setSizePolicy(sizePolicy)
        self.commiss_date_label.setMinimumSize(QSize(150, 30))
        self.commiss_date_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.commiss_date_label, 1, 4, 1, 1)

        self.commiss_date_text = QPlainTextEdit(self.frame_20)
        self.commiss_date_text.setObjectName(u"commiss_date_text")
        sizePolicy1.setHeightForWidth(self.commiss_date_text.sizePolicy().hasHeightForWidth())
        self.commiss_date_text.setSizePolicy(sizePolicy1)
        self.commiss_date_text.setMinimumSize(QSize(150, 30))
        self.commiss_date_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.commiss_date_text, 1, 5, 1, 1)

        self.inverter_SN_label = QLabel(self.frame_20)
        self.inverter_SN_label.setObjectName(u"inverter_SN_label")
        sizePolicy3.setHeightForWidth(self.inverter_SN_label.sizePolicy().hasHeightForWidth())
        self.inverter_SN_label.setSizePolicy(sizePolicy3)
        self.inverter_SN_label.setMinimumSize(QSize(150, 30))
        self.inverter_SN_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.inverter_SN_label, 0, 4, 1, 1)

        self.inverter_type_text = QPlainTextEdit(self.frame_20)
        self.inverter_type_text.setObjectName(u"inverter_type_text")
        sizePolicy1.setHeightForWidth(self.inverter_type_text.sizePolicy().hasHeightForWidth())
        self.inverter_type_text.setSizePolicy(sizePolicy1)
        self.inverter_type_text.setMinimumSize(QSize(150, 30))
        self.inverter_type_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.inverter_type_text, 0, 1, 1, 1)

        self.inverter_power_label = QLabel(self.frame_20)
        self.inverter_power_label.setObjectName(u"inverter_power_label")
        sizePolicy.setHeightForWidth(self.inverter_power_label.sizePolicy().hasHeightForWidth())
        self.inverter_power_label.setSizePolicy(sizePolicy)
        self.inverter_power_label.setMinimumSize(QSize(150, 30))
        self.inverter_power_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.inverter_power_label, 1, 0, 1, 1)

        self.inverter_power_text = QPlainTextEdit(self.frame_20)
        self.inverter_power_text.setObjectName(u"inverter_power_text")
        sizePolicy1.setHeightForWidth(self.inverter_power_text.sizePolicy().hasHeightForWidth())
        self.inverter_power_text.setSizePolicy(sizePolicy1)
        self.inverter_power_text.setMinimumSize(QSize(150, 30))
        self.inverter_power_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.inverter_power_text, 1, 1, 1, 1)

        self.inverter_type_label = QLabel(self.frame_20)
        self.inverter_type_label.setObjectName(u"inverter_type_label")
        sizePolicy.setHeightForWidth(self.inverter_type_label.sizePolicy().hasHeightForWidth())
        self.inverter_type_label.setSizePolicy(sizePolicy)
        self.inverter_type_label.setMinimumSize(QSize(150, 30))
        self.inverter_type_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_10.addWidget(self.inverter_type_label, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_20, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.headline_04 = QLabel(self.frame0221)
        self.headline_04.setObjectName(u"headline_04")
        self.headline_04.setMinimumSize(QSize(250, 50))
        self.headline_04.setFont(font)
        self.headline_04.setFrameShape(QFrame.StyledPanel)
        self.headline_04.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_04)

        self.BAT_inverters_list = QTableWidget(self.frame0221)
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
        sizePolicy7.setHeightForWidth(self.BAT_inverters_list.sizePolicy().hasHeightForWidth())
        self.BAT_inverters_list.setSizePolicy(sizePolicy7)
        self.BAT_inverters_list.setMinimumSize(QSize(0, 400))
        self.BAT_inverters_list.setMaximumSize(QSize(1800, 16777215))
        self.BAT_inverters_list.setAutoFillBackground(False)
        self.BAT_inverters_list.setFrameShape(QFrame.StyledPanel)
        self.BAT_inverters_list.setMidLineWidth(1)
        self.BAT_inverters_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.BAT_inverters_list.setDragDropOverwriteMode(False)
        self.BAT_inverters_list.setAlternatingRowColors(True)
        self.BAT_inverters_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.BAT_inverters_list.setGridStyle(Qt.DashDotDotLine)
        self.BAT_inverters_list.setSortingEnabled(True)
        self.BAT_inverters_list.setWordWrap(False)
        self.BAT_inverters_list.setCornerButtonEnabled(False)
        self.BAT_inverters_list.horizontalHeader().setMinimumSectionSize(50)
        self.BAT_inverters_list.horizontalHeader().setDefaultSectionSize(150)
        self.BAT_inverters_list.verticalHeader().setVisible(False)
        self.BAT_inverters_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.BAT_inverters_list)

        self.frame_21 = QFrame(self.frame0221)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.move_none_BAT_inverters_to_blacklist = QPushButton(self.frame_21)
        self.move_none_BAT_inverters_to_blacklist.setObjectName(u"move_none_BAT_inverters_to_blacklist")
        self.move_none_BAT_inverters_to_blacklist.setMinimumSize(QSize(100, 30))

        self.verticalLayout_10.addWidget(self.move_none_BAT_inverters_to_blacklist)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_22)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.bat_inverter_type_label = QLabel(self.frame_22)
        self.bat_inverter_type_label.setObjectName(u"bat_inverter_type_label")
        sizePolicy.setHeightForWidth(self.bat_inverter_type_label.sizePolicy().hasHeightForWidth())
        self.bat_inverter_type_label.setSizePolicy(sizePolicy)
        self.bat_inverter_type_label.setMinimumSize(QSize(100, 30))
        self.bat_inverter_type_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.bat_inverter_type_label, 0, 0, 1, 1)

        self.bat_inverter_type_text = QPlainTextEdit(self.frame_22)
        self.bat_inverter_type_text.setObjectName(u"bat_inverter_type_text")
        sizePolicy.setHeightForWidth(self.bat_inverter_type_text.sizePolicy().hasHeightForWidth())
        self.bat_inverter_type_text.setSizePolicy(sizePolicy)
        self.bat_inverter_type_text.setMinimumSize(QSize(100, 30))
        self.bat_inverter_type_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.bat_inverter_type_text, 0, 1, 1, 1)

        self.bat_inverter_SN_label = QLabel(self.frame_22)
        self.bat_inverter_SN_label.setObjectName(u"bat_inverter_SN_label")
        sizePolicy.setHeightForWidth(self.bat_inverter_SN_label.sizePolicy().hasHeightForWidth())
        self.bat_inverter_SN_label.setSizePolicy(sizePolicy)
        self.bat_inverter_SN_label.setMinimumSize(QSize(100, 30))
        self.bat_inverter_SN_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.bat_inverter_SN_label, 0, 2, 1, 1)

        self.bat_inverter_SN_text = QPlainTextEdit(self.frame_22)
        self.bat_inverter_SN_text.setObjectName(u"bat_inverter_SN_text")
        sizePolicy.setHeightForWidth(self.bat_inverter_SN_text.sizePolicy().hasHeightForWidth())
        self.bat_inverter_SN_text.setSizePolicy(sizePolicy)
        self.bat_inverter_SN_text.setMinimumSize(QSize(100, 30))
        self.bat_inverter_SN_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.bat_inverter_SN_text, 0, 3, 1, 1)

        self.bat_inverter_power_label = QLabel(self.frame_22)
        self.bat_inverter_power_label.setObjectName(u"bat_inverter_power_label")
        sizePolicy.setHeightForWidth(self.bat_inverter_power_label.sizePolicy().hasHeightForWidth())
        self.bat_inverter_power_label.setSizePolicy(sizePolicy)
        self.bat_inverter_power_label.setMinimumSize(QSize(100, 30))
        self.bat_inverter_power_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.bat_inverter_power_label, 1, 0, 1, 1)

        self.bat_inverter_power_text = QPlainTextEdit(self.frame_22)
        self.bat_inverter_power_text.setObjectName(u"bat_inverter_power_text")
        sizePolicy.setHeightForWidth(self.bat_inverter_power_text.sizePolicy().hasHeightForWidth())
        self.bat_inverter_power_text.setSizePolicy(sizePolicy)
        self.bat_inverter_power_text.setMinimumSize(QSize(100, 30))
        self.bat_inverter_power_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.bat_inverter_power_text, 1, 1, 1, 1)

        self.coupling_type_label = QLabel(self.frame_22)
        self.coupling_type_label.setObjectName(u"coupling_type_label")
        sizePolicy.setHeightForWidth(self.coupling_type_label.sizePolicy().hasHeightForWidth())
        self.coupling_type_label.setSizePolicy(sizePolicy)
        self.coupling_type_label.setMinimumSize(QSize(100, 30))
        self.coupling_type_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_12.addWidget(self.coupling_type_label, 1, 2, 1, 1)

        self.coupling_type_text = QPlainTextEdit(self.frame_22)
        self.coupling_type_text.setObjectName(u"coupling_type_text")
        sizePolicy.setHeightForWidth(self.coupling_type_text.sizePolicy().hasHeightForWidth())
        self.coupling_type_text.setSizePolicy(sizePolicy)
        self.coupling_type_text.setMinimumSize(QSize(100, 30))
        self.coupling_type_text.setMaximumSize(QSize(300, 60))
        self.coupling_type_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_12.addWidget(self.coupling_type_text, 1, 3, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_22)


        self.verticalLayout_3.addWidget(self.frame_21)

        self.headline_05 = QLabel(self.frame0221)
        self.headline_05.setObjectName(u"headline_05")
        self.headline_05.setMinimumSize(QSize(250, 50))
        self.headline_05.setFont(font)
        self.headline_05.setFrameShape(QFrame.StyledPanel)
        self.headline_05.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_05)

        self.BAT_storage_list = QTableWidget(self.frame0221)
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
        sizePolicy7.setHeightForWidth(self.BAT_storage_list.sizePolicy().hasHeightForWidth())
        self.BAT_storage_list.setSizePolicy(sizePolicy7)
        self.BAT_storage_list.setMinimumSize(QSize(0, 400))
        self.BAT_storage_list.setMaximumSize(QSize(1800, 16777215))
        self.BAT_storage_list.setAutoFillBackground(False)
        self.BAT_storage_list.setFrameShape(QFrame.StyledPanel)
        self.BAT_storage_list.setMidLineWidth(1)
        self.BAT_storage_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.BAT_storage_list.setDragDropOverwriteMode(False)
        self.BAT_storage_list.setAlternatingRowColors(True)
        self.BAT_storage_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.BAT_storage_list.setGridStyle(Qt.DashDotDotLine)
        self.BAT_storage_list.setSortingEnabled(True)
        self.BAT_storage_list.setWordWrap(False)
        self.BAT_storage_list.setCornerButtonEnabled(False)
        self.BAT_storage_list.horizontalHeader().setMinimumSectionSize(50)
        self.BAT_storage_list.horizontalHeader().setDefaultSectionSize(150)
        self.BAT_storage_list.verticalHeader().setVisible(False)
        self.BAT_storage_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.BAT_storage_list)

        self.frame_24 = QFrame(self.frame0221)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_24)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.move_none_BAT_storage_to_blacklist = QPushButton(self.frame_24)
        self.move_none_BAT_storage_to_blacklist.setObjectName(u"move_none_BAT_storage_to_blacklist")
        self.move_none_BAT_storage_to_blacklist.setMinimumSize(QSize(100, 30))

        self.verticalLayout_11.addWidget(self.move_none_BAT_storage_to_blacklist)

        self.frame_23 = QFrame(self.frame_24)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_23)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.bat_storage_type_label = QLabel(self.frame_23)
        self.bat_storage_type_label.setObjectName(u"bat_storage_type_label")
        sizePolicy.setHeightForWidth(self.bat_storage_type_label.sizePolicy().hasHeightForWidth())
        self.bat_storage_type_label.setSizePolicy(sizePolicy)
        self.bat_storage_type_label.setMinimumSize(QSize(150, 30))
        self.bat_storage_type_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_storage_type_label, 0, 0, 1, 1)

        self.bat_storage_type_text = QPlainTextEdit(self.frame_23)
        self.bat_storage_type_text.setObjectName(u"bat_storage_type_text")
        sizePolicy.setHeightForWidth(self.bat_storage_type_text.sizePolicy().hasHeightForWidth())
        self.bat_storage_type_text.setSizePolicy(sizePolicy)
        self.bat_storage_type_text.setMinimumSize(QSize(150, 30))
        self.bat_storage_type_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_storage_type_text, 0, 1, 1, 1)

        self.bat_storage_SN_label = QLabel(self.frame_23)
        self.bat_storage_SN_label.setObjectName(u"bat_storage_SN_label")
        sizePolicy.setHeightForWidth(self.bat_storage_SN_label.sizePolicy().hasHeightForWidth())
        self.bat_storage_SN_label.setSizePolicy(sizePolicy)
        self.bat_storage_SN_label.setMinimumSize(QSize(150, 30))
        self.bat_storage_SN_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_storage_SN_label, 0, 2, 1, 1)

        self.bat_storage_SN_text = QPlainTextEdit(self.frame_23)
        self.bat_storage_SN_text.setObjectName(u"bat_storage_SN_text")
        sizePolicy.setHeightForWidth(self.bat_storage_SN_text.sizePolicy().hasHeightForWidth())
        self.bat_storage_SN_text.setSizePolicy(sizePolicy)
        self.bat_storage_SN_text.setMinimumSize(QSize(150, 30))
        self.bat_storage_SN_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_storage_SN_text, 0, 3, 1, 1)

        self.bat_storage_cap_label = QLabel(self.frame_23)
        self.bat_storage_cap_label.setObjectName(u"bat_storage_cap_label")
        sizePolicy.setHeightForWidth(self.bat_storage_cap_label.sizePolicy().hasHeightForWidth())
        self.bat_storage_cap_label.setSizePolicy(sizePolicy)
        self.bat_storage_cap_label.setMinimumSize(QSize(150, 30))
        self.bat_storage_cap_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_storage_cap_label, 1, 0, 1, 1)

        self.bat_storage_cap_text = QPlainTextEdit(self.frame_23)
        self.bat_storage_cap_text.setObjectName(u"bat_storage_cap_text")
        sizePolicy.setHeightForWidth(self.bat_storage_cap_text.sizePolicy().hasHeightForWidth())
        self.bat_storage_cap_text.setSizePolicy(sizePolicy)
        self.bat_storage_cap_text.setMinimumSize(QSize(150, 30))
        self.bat_storage_cap_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_storage_cap_text, 1, 1, 1, 1)

        self.bat_commiss_date_label = QLabel(self.frame_23)
        self.bat_commiss_date_label.setObjectName(u"bat_commiss_date_label")
        sizePolicy.setHeightForWidth(self.bat_commiss_date_label.sizePolicy().hasHeightForWidth())
        self.bat_commiss_date_label.setSizePolicy(sizePolicy)
        self.bat_commiss_date_label.setMinimumSize(QSize(150, 30))
        self.bat_commiss_date_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_commiss_date_label, 1, 2, 1, 1)

        self.bat_commiss_date_text = QPlainTextEdit(self.frame_23)
        self.bat_commiss_date_text.setObjectName(u"bat_commiss_date_text")
        sizePolicy.setHeightForWidth(self.bat_commiss_date_text.sizePolicy().hasHeightForWidth())
        self.bat_commiss_date_text.setSizePolicy(sizePolicy)
        self.bat_commiss_date_text.setMinimumSize(QSize(150, 30))
        self.bat_commiss_date_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_commiss_date_text, 1, 3, 1, 1)

        self.max_discharge_pow_label = QLabel(self.frame_23)
        self.max_discharge_pow_label.setObjectName(u"max_discharge_pow_label")
        sizePolicy.setHeightForWidth(self.max_discharge_pow_label.sizePolicy().hasHeightForWidth())
        self.max_discharge_pow_label.setSizePolicy(sizePolicy)
        self.max_discharge_pow_label.setMinimumSize(QSize(150, 30))
        self.max_discharge_pow_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.max_discharge_pow_label, 2, 0, 1, 1)

        self.max_discharge_pow_text = QPlainTextEdit(self.frame_23)
        self.max_discharge_pow_text.setObjectName(u"max_discharge_pow_text")
        sizePolicy.setHeightForWidth(self.max_discharge_pow_text.sizePolicy().hasHeightForWidth())
        self.max_discharge_pow_text.setSizePolicy(sizePolicy)
        self.max_discharge_pow_text.setMinimumSize(QSize(150, 30))
        self.max_discharge_pow_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.max_discharge_pow_text, 2, 1, 1, 1)

        self.em_pow_ability_bool_label = QLabel(self.frame_23)
        self.em_pow_ability_bool_label.setObjectName(u"em_pow_ability_bool_label")
        sizePolicy.setHeightForWidth(self.em_pow_ability_bool_label.sizePolicy().hasHeightForWidth())
        self.em_pow_ability_bool_label.setSizePolicy(sizePolicy)
        self.em_pow_ability_bool_label.setMinimumSize(QSize(150, 30))
        self.em_pow_ability_bool_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.em_pow_ability_bool_label, 2, 2, 1, 1)

        self.em_pow_ability_bool_text = QPlainTextEdit(self.frame_23)
        self.em_pow_ability_bool_text.setObjectName(u"em_pow_ability_bool_text")
        sizePolicy.setHeightForWidth(self.em_pow_ability_bool_text.sizePolicy().hasHeightForWidth())
        self.em_pow_ability_bool_text.setSizePolicy(sizePolicy)
        self.em_pow_ability_bool_text.setMinimumSize(QSize(150, 30))
        self.em_pow_ability_bool_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.em_pow_ability_bool_text, 2, 3, 1, 1)

        self.energy_storage_type_label = QLabel(self.frame_23)
        self.energy_storage_type_label.setObjectName(u"energy_storage_type_label")
        sizePolicy.setHeightForWidth(self.energy_storage_type_label.sizePolicy().hasHeightForWidth())
        self.energy_storage_type_label.setSizePolicy(sizePolicy)
        self.energy_storage_type_label.setMinimumSize(QSize(150, 30))
        self.energy_storage_type_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.energy_storage_type_label, 3, 0, 1, 1)

        self.energy_storage_type_text = QPlainTextEdit(self.frame_23)
        self.energy_storage_type_text.setObjectName(u"energy_storage_type_text")
        sizePolicy.setHeightForWidth(self.energy_storage_type_text.sizePolicy().hasHeightForWidth())
        self.energy_storage_type_text.setSizePolicy(sizePolicy)
        self.energy_storage_type_text.setMinimumSize(QSize(150, 30))
        self.energy_storage_type_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.energy_storage_type_text, 3, 1, 1, 1)

        self.bat_technology_label = QLabel(self.frame_23)
        self.bat_technology_label.setObjectName(u"bat_technology_label")
        sizePolicy.setHeightForWidth(self.bat_technology_label.sizePolicy().hasHeightForWidth())
        self.bat_technology_label.setSizePolicy(sizePolicy)
        self.bat_technology_label.setMinimumSize(QSize(150, 30))
        self.bat_technology_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_technology_label, 3, 2, 1, 1)

        self.bat_technology_text = QPlainTextEdit(self.frame_23)
        self.bat_technology_text.setObjectName(u"bat_technology_text")
        sizePolicy.setHeightForWidth(self.bat_technology_text.sizePolicy().hasHeightForWidth())
        self.bat_technology_text.setSizePolicy(sizePolicy)
        self.bat_technology_text.setMinimumSize(QSize(150, 30))
        self.bat_technology_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_13.addWidget(self.bat_technology_text, 3, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_23)


        self.verticalLayout_3.addWidget(self.frame_24)

        self.headline_06 = QLabel(self.frame0221)
        self.headline_06.setObjectName(u"headline_06")
        self.headline_06.setMinimumSize(QSize(250, 50))
        self.headline_06.setFont(font)
        self.headline_06.setFrameShape(QFrame.StyledPanel)
        self.headline_06.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_06)

        self.CHG_point_list = QTableWidget(self.frame0221)
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
        sizePolicy7.setHeightForWidth(self.CHG_point_list.sizePolicy().hasHeightForWidth())
        self.CHG_point_list.setSizePolicy(sizePolicy7)
        self.CHG_point_list.setMinimumSize(QSize(0, 400))
        self.CHG_point_list.setMaximumSize(QSize(1800, 16777215))
        self.CHG_point_list.setAutoFillBackground(False)
        self.CHG_point_list.setFrameShape(QFrame.StyledPanel)
        self.CHG_point_list.setMidLineWidth(1)
        self.CHG_point_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.CHG_point_list.setDragDropOverwriteMode(False)
        self.CHG_point_list.setAlternatingRowColors(True)
        self.CHG_point_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.CHG_point_list.setGridStyle(Qt.DashDotDotLine)
        self.CHG_point_list.setSortingEnabled(True)
        self.CHG_point_list.setWordWrap(False)
        self.CHG_point_list.setCornerButtonEnabled(False)
        self.CHG_point_list.horizontalHeader().setMinimumSectionSize(50)
        self.CHG_point_list.horizontalHeader().setDefaultSectionSize(150)
        self.CHG_point_list.verticalHeader().setVisible(False)
        self.CHG_point_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.CHG_point_list)

        self.frame_26 = QFrame(self.frame0221)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_26)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.move_none_CHG_point_to_blacklist = QPushButton(self.frame_26)
        self.move_none_CHG_point_to_blacklist.setObjectName(u"move_none_CHG_point_to_blacklist")
        self.move_none_CHG_point_to_blacklist.setMinimumSize(QSize(100, 30))

        self.verticalLayout_12.addWidget(self.move_none_CHG_point_to_blacklist)

        self.frame_25 = QFrame(self.frame_26)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_25)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.charging_point_type_label = QLabel(self.frame_25)
        self.charging_point_type_label.setObjectName(u"charging_point_type_label")
        sizePolicy.setHeightForWidth(self.charging_point_type_label.sizePolicy().hasHeightForWidth())
        self.charging_point_type_label.setSizePolicy(sizePolicy)
        self.charging_point_type_label.setMinimumSize(QSize(150, 30))
        self.charging_point_type_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_14.addWidget(self.charging_point_type_label, 0, 0, 1, 1)

        self.charging_point_type_text = QPlainTextEdit(self.frame_25)
        self.charging_point_type_text.setObjectName(u"charging_point_type_text")
        sizePolicy.setHeightForWidth(self.charging_point_type_text.sizePolicy().hasHeightForWidth())
        self.charging_point_type_text.setSizePolicy(sizePolicy)
        self.charging_point_type_text.setMinimumSize(QSize(150, 30))
        self.charging_point_type_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_14.addWidget(self.charging_point_type_text, 0, 1, 1, 1)

        self.charging_point_SN_label = QLabel(self.frame_25)
        self.charging_point_SN_label.setObjectName(u"charging_point_SN_label")
        sizePolicy.setHeightForWidth(self.charging_point_SN_label.sizePolicy().hasHeightForWidth())
        self.charging_point_SN_label.setSizePolicy(sizePolicy)
        self.charging_point_SN_label.setMinimumSize(QSize(150, 30))
        self.charging_point_SN_label.setMaximumSize(QSize(300, 60))

        self.gridLayout_14.addWidget(self.charging_point_SN_label, 0, 2, 1, 1)

        self.charging_point_SN_text = QTextEdit(self.frame_25)
        self.charging_point_SN_text.setObjectName(u"charging_point_SN_text")
        sizePolicy.setHeightForWidth(self.charging_point_SN_text.sizePolicy().hasHeightForWidth())
        self.charging_point_SN_text.setSizePolicy(sizePolicy)
        self.charging_point_SN_text.setMinimumSize(QSize(150, 30))
        self.charging_point_SN_text.setMaximumSize(QSize(300, 60))

        self.gridLayout_14.addWidget(self.charging_point_SN_text, 0, 3, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_25)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.headline_07 = QLabel(self.frame0221)
        self.headline_07.setObjectName(u"headline_07")
        sizePolicy.setHeightForWidth(self.headline_07.sizePolicy().hasHeightForWidth())
        self.headline_07.setSizePolicy(sizePolicy)
        self.headline_07.setMinimumSize(QSize(250, 50))
        self.headline_07.setFont(font)
        self.headline_07.setFrameShape(QFrame.StyledPanel)
        self.headline_07.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_07)

        self.frame_27 = QFrame(self.frame0221)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_27)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.feeding_type_label = QLabel(self.frame_27)
        self.feeding_type_label.setObjectName(u"feeding_type_label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(30)
        sizePolicy8.setHeightForWidth(self.feeding_type_label.sizePolicy().hasHeightForWidth())
        self.feeding_type_label.setSizePolicy(sizePolicy8)
        self.feeding_type_label.setMinimumSize(QSize(200, 60))
        self.feeding_type_label.setMaximumSize(QSize(400, 30))

        self.gridLayout_15.addWidget(self.feeding_type_label, 0, 0, 1, 1)

        self.feeding_type_text = QPlainTextEdit(self.frame_27)
        self.feeding_type_text.setObjectName(u"feeding_type_text")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(30)
        sizePolicy9.setHeightForWidth(self.feeding_type_text.sizePolicy().hasHeightForWidth())
        self.feeding_type_text.setSizePolicy(sizePolicy9)
        self.feeding_type_text.setMinimumSize(QSize(400, 60))
        self.feeding_type_text.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.feeding_type_text, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_27)

        self.headline_08 = QLabel(self.frame0221)
        self.headline_08.setObjectName(u"headline_08")
        self.headline_08.setMinimumSize(QSize(250, 50))
        self.headline_08.setFont(font)
        self.headline_08.setFrameShape(QFrame.StyledPanel)
        self.headline_08.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_08)

        self.frame_28 = QFrame(self.frame0221)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_28)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pow_limit_bool_label = QLabel(self.frame_28)
        self.pow_limit_bool_label.setObjectName(u"pow_limit_bool_label")
        sizePolicy.setHeightForWidth(self.pow_limit_bool_label.sizePolicy().hasHeightForWidth())
        self.pow_limit_bool_label.setSizePolicy(sizePolicy)
        self.pow_limit_bool_label.setMinimumSize(QSize(100, 30))
        self.pow_limit_bool_label.setMaximumSize(QSize(300, 90))

        self.gridLayout_16.addWidget(self.pow_limit_bool_label, 0, 0, 1, 1)

        self.pow_limit_bool_text = QPlainTextEdit(self.frame_28)
        self.pow_limit_bool_text.setObjectName(u"pow_limit_bool_text")
        sizePolicy.setHeightForWidth(self.pow_limit_bool_text.sizePolicy().hasHeightForWidth())
        self.pow_limit_bool_text.setSizePolicy(sizePolicy)
        self.pow_limit_bool_text.setMinimumSize(QSize(50, 30))
        self.pow_limit_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.pow_limit_bool_text, 0, 1, 1, 1)

        self.rmt_grd_op_bool_label = QLabel(self.frame_28)
        self.rmt_grd_op_bool_label.setObjectName(u"rmt_grd_op_bool_label")
        sizePolicy3.setHeightForWidth(self.rmt_grd_op_bool_label.sizePolicy().hasHeightForWidth())
        self.rmt_grd_op_bool_label.setSizePolicy(sizePolicy3)
        self.rmt_grd_op_bool_label.setMinimumSize(QSize(100, 30))
        self.rmt_grd_op_bool_label.setMaximumSize(QSize(300, 90))

        self.gridLayout_16.addWidget(self.rmt_grd_op_bool_label, 0, 2, 1, 1)

        self.rmt_grd_op_bool_text = QPlainTextEdit(self.frame_28)
        self.rmt_grd_op_bool_text.setObjectName(u"rmt_grd_op_bool_text")
        sizePolicy.setHeightForWidth(self.rmt_grd_op_bool_text.sizePolicy().hasHeightForWidth())
        self.rmt_grd_op_bool_text.setSizePolicy(sizePolicy)
        self.rmt_grd_op_bool_text.setMinimumSize(QSize(50, 30))
        self.rmt_grd_op_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.rmt_grd_op_bool_text, 0, 3, 1, 1)

        self.rmt_drct_mrktr_bool_label = QLabel(self.frame_28)
        self.rmt_drct_mrktr_bool_label.setObjectName(u"rmt_drct_mrktr_bool_label")
        sizePolicy.setHeightForWidth(self.rmt_drct_mrktr_bool_label.sizePolicy().hasHeightForWidth())
        self.rmt_drct_mrktr_bool_label.setSizePolicy(sizePolicy)
        self.rmt_drct_mrktr_bool_label.setMinimumSize(QSize(100, 30))
        self.rmt_drct_mrktr_bool_label.setMaximumSize(QSize(300, 90))
        self.rmt_drct_mrktr_bool_label.setMouseTracking(False)

        self.gridLayout_16.addWidget(self.rmt_drct_mrktr_bool_label, 1, 0, 1, 1)

        self.rmt_drct_mrktr_bool_text = QPlainTextEdit(self.frame_28)
        self.rmt_drct_mrktr_bool_text.setObjectName(u"rmt_drct_mrktr_bool_text")
        sizePolicy.setHeightForWidth(self.rmt_drct_mrktr_bool_text.sizePolicy().hasHeightForWidth())
        self.rmt_drct_mrktr_bool_text.setSizePolicy(sizePolicy)
        self.rmt_drct_mrktr_bool_text.setMinimumSize(QSize(50, 30))
        self.rmt_drct_mrktr_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.rmt_drct_mrktr_bool_text, 1, 1, 1, 1)

        self.rmt_3rd_prt_bool_label = QLabel(self.frame_28)
        self.rmt_3rd_prt_bool_label.setObjectName(u"rmt_3rd_prt_bool_label")
        sizePolicy.setHeightForWidth(self.rmt_3rd_prt_bool_label.sizePolicy().hasHeightForWidth())
        self.rmt_3rd_prt_bool_label.setSizePolicy(sizePolicy)
        self.rmt_3rd_prt_bool_label.setMinimumSize(QSize(100, 30))
        self.rmt_3rd_prt_bool_label.setMaximumSize(QSize(300, 90))

        self.gridLayout_16.addWidget(self.rmt_3rd_prt_bool_label, 1, 2, 1, 1)

        self.rmt_3rd_prt_bool_text = QPlainTextEdit(self.frame_28)
        self.rmt_3rd_prt_bool_text.setObjectName(u"rmt_3rd_prt_bool_text")
        sizePolicy.setHeightForWidth(self.rmt_3rd_prt_bool_text.sizePolicy().hasHeightForWidth())
        self.rmt_3rd_prt_bool_text.setSizePolicy(sizePolicy)
        self.rmt_3rd_prt_bool_text.setMinimumSize(QSize(50, 30))
        self.rmt_3rd_prt_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.rmt_3rd_prt_bool_text, 1, 3, 1, 1)

        self.prequali_bool_label = QLabel(self.frame_28)
        self.prequali_bool_label.setObjectName(u"prequali_bool_label")
        sizePolicy.setHeightForWidth(self.prequali_bool_label.sizePolicy().hasHeightForWidth())
        self.prequali_bool_label.setSizePolicy(sizePolicy)
        self.prequali_bool_label.setMinimumSize(QSize(100, 30))
        self.prequali_bool_label.setMaximumSize(QSize(300, 90))

        self.gridLayout_16.addWidget(self.prequali_bool_label, 2, 0, 1, 1)

        self.prequali_bool_text = QPlainTextEdit(self.frame_28)
        self.prequali_bool_text.setObjectName(u"prequali_bool_text")
        sizePolicy.setHeightForWidth(self.prequali_bool_text.sizePolicy().hasHeightForWidth())
        self.prequali_bool_text.setSizePolicy(sizePolicy)
        self.prequali_bool_text.setMinimumSize(QSize(50, 30))
        self.prequali_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.prequali_bool_text, 2, 1, 1, 1)

        self.citizen_corp_bool_label = QLabel(self.frame_28)
        self.citizen_corp_bool_label.setObjectName(u"citizen_corp_bool_label")
        sizePolicy.setHeightForWidth(self.citizen_corp_bool_label.sizePolicy().hasHeightForWidth())
        self.citizen_corp_bool_label.setSizePolicy(sizePolicy)
        self.citizen_corp_bool_label.setMinimumSize(QSize(100, 30))
        self.citizen_corp_bool_label.setMaximumSize(QSize(300, 90))

        self.gridLayout_16.addWidget(self.citizen_corp_bool_label, 2, 2, 1, 1)

        self.citizen_corp_bool_text = QPlainTextEdit(self.frame_28)
        self.citizen_corp_bool_text.setObjectName(u"citizen_corp_bool_text")
        sizePolicy.setHeightForWidth(self.citizen_corp_bool_text.sizePolicy().hasHeightForWidth())
        self.citizen_corp_bool_text.setSizePolicy(sizePolicy)
        self.citizen_corp_bool_text.setMinimumSize(QSize(50, 30))
        self.citizen_corp_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.citizen_corp_bool_text, 2, 3, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.tendering_bool_label = QLabel(self.frame_28)
        self.tendering_bool_label.setObjectName(u"tendering_bool_label")
        sizePolicy.setHeightForWidth(self.tendering_bool_label.sizePolicy().hasHeightForWidth())
        self.tendering_bool_label.setSizePolicy(sizePolicy)
        self.tendering_bool_label.setMinimumSize(QSize(100, 30))
        self.tendering_bool_label.setMaximumSize(QSize(300, 90))

        self.gridLayout_16.addWidget(self.tendering_bool_label, 3, 0, 1, 1)

        self.tendering_bool_text = QPlainTextEdit(self.frame_28)
        self.tendering_bool_text.setObjectName(u"tendering_bool_text")
        sizePolicy.setHeightForWidth(self.tendering_bool_text.sizePolicy().hasHeightForWidth())
        self.tendering_bool_text.setSizePolicy(sizePolicy)
        self.tendering_bool_text.setMinimumSize(QSize(50, 30))
        self.tendering_bool_text.setMaximumSize(QSize(75, 30))

        self.gridLayout_16.addWidget(self.tendering_bool_text, 3, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_28)

        self.headline_09 = QLabel(self.frame0221)
        self.headline_09.setObjectName(u"headline_09")
        self.headline_09.setMinimumSize(QSize(250, 50))
        self.headline_09.setFont(font)
        self.headline_09.setFrameShape(QFrame.StyledPanel)
        self.headline_09.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_09)

        self.frame_29 = QFrame(self.frame0221)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_29)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.meter_cabinet_text = QPlainTextEdit(self.frame_29)
        self.meter_cabinet_text.setObjectName(u"meter_cabinet_text")
        sizePolicy.setHeightForWidth(self.meter_cabinet_text.sizePolicy().hasHeightForWidth())
        self.meter_cabinet_text.setSizePolicy(sizePolicy)
        self.meter_cabinet_text.setMinimumSize(QSize(0, 30))
        self.meter_cabinet_text.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_17.addWidget(self.meter_cabinet_text, 0, 1, 1, 1)

        self.meter_box_type_label = QLabel(self.frame_29)
        self.meter_box_type_label.setObjectName(u"meter_box_type_label")
        sizePolicy.setHeightForWidth(self.meter_box_type_label.sizePolicy().hasHeightForWidth())
        self.meter_box_type_label.setSizePolicy(sizePolicy)
        self.meter_box_type_label.setMinimumSize(QSize(100, 30))
        self.meter_box_type_label.setMaximumSize(QSize(200, 60))

        self.gridLayout_17.addWidget(self.meter_box_type_label, 1, 0, 1, 1)

        self.meter_box_type_text = QPlainTextEdit(self.frame_29)
        self.meter_box_type_text.setObjectName(u"meter_box_type_text")
        sizePolicy.setHeightForWidth(self.meter_box_type_text.sizePolicy().hasHeightForWidth())
        self.meter_box_type_text.setSizePolicy(sizePolicy)
        self.meter_box_type_text.setMinimumSize(QSize(0, 30))
        self.meter_box_type_text.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_17.addWidget(self.meter_box_type_text, 1, 1, 1, 1)

        self.meter_cabinet_label = QLabel(self.frame_29)
        self.meter_cabinet_label.setObjectName(u"meter_cabinet_label")
        sizePolicy.setHeightForWidth(self.meter_cabinet_label.sizePolicy().hasHeightForWidth())
        self.meter_cabinet_label.setSizePolicy(sizePolicy)
        self.meter_cabinet_label.setMinimumSize(QSize(100, 30))
        self.meter_cabinet_label.setMaximumSize(QSize(200, 60))

        self.gridLayout_17.addWidget(self.meter_cabinet_label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.frame0221)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_31)
        self.gridLayout_19.setObjectName(u"gridLayout_19")

        self.verticalLayout_3.addWidget(self.frame_31)

        self.headline_10 = QLabel(self.frame0221)
        self.headline_10.setObjectName(u"headline_10")
        self.headline_10.setMinimumSize(QSize(250, 50))
        self.headline_10.setFont(font)
        self.headline_10.setFrameShape(QFrame.StyledPanel)
        self.headline_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.headline_10)

        self.frame_30 = QFrame(self.frame0221)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_30)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.dl_connect_ext_text = QPlainTextEdit(self.frame_30)
        self.dl_connect_ext_text.setObjectName(u"dl_connect_ext_text")
        sizePolicy.setHeightForWidth(self.dl_connect_ext_text.sizePolicy().hasHeightForWidth())
        self.dl_connect_ext_text.setSizePolicy(sizePolicy)
        self.dl_connect_ext_text.setMinimumSize(QSize(200, 30))
        self.dl_connect_ext_text.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_18.addWidget(self.dl_connect_ext_text, 2, 1, 1, 1)

        self.dl_type_label = QLabel(self.frame_30)
        self.dl_type_label.setObjectName(u"dl_type_label")
        sizePolicy.setHeightForWidth(self.dl_type_label.sizePolicy().hasHeightForWidth())
        self.dl_type_label.setSizePolicy(sizePolicy)
        self.dl_type_label.setMinimumSize(QSize(150, 30))
        self.dl_type_label.setMaximumSize(QSize(200, 60))
        self.dl_type_label.setIndent(-1)

        self.gridLayout_18.addWidget(self.dl_type_label, 0, 0, 1, 1)

        self.dl_type_text = QPlainTextEdit(self.frame_30)
        self.dl_type_text.setObjectName(u"dl_type_text")
        sizePolicy.setHeightForWidth(self.dl_type_text.sizePolicy().hasHeightForWidth())
        self.dl_type_text.setSizePolicy(sizePolicy)
        self.dl_type_text.setMinimumSize(QSize(200, 30))
        self.dl_type_text.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_18.addWidget(self.dl_type_text, 0, 1, 1, 1)

        self.dl_connect_ext_label = QLabel(self.frame_30)
        self.dl_connect_ext_label.setObjectName(u"dl_connect_ext_label")
        sizePolicy.setHeightForWidth(self.dl_connect_ext_label.sizePolicy().hasHeightForWidth())
        self.dl_connect_ext_label.setSizePolicy(sizePolicy)
        self.dl_connect_ext_label.setMinimumSize(QSize(150, 30))
        self.dl_connect_ext_label.setMaximumSize(QSize(200, 60))

        self.gridLayout_18.addWidget(self.dl_connect_ext_label, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_30)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout_5.addWidget(self.frame0221, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.frame0220.addWidget(self.scrollArea)

        self.frame_32 = QFrame(self.layoutWidget)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_32)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.load_data_to_device_lists_btn = QPushButton(self.frame_34)
        self.load_data_to_device_lists_btn.setObjectName(u"load_data_to_device_lists_btn")
        self.load_data_to_device_lists_btn.setMinimumSize(QSize(200, 40))
        self.load_data_to_device_lists_btn.setMaximumSize(QSize(350, 16777215))
        self.load_data_to_device_lists_btn.setMouseTracking(True)
        self.load_data_to_device_lists_btn.setFocusPolicy(Qt.StrongFocus)
        self.load_data_to_device_lists_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.load_data_to_device_lists_btn.setAcceptDrops(False)
        self.load_data_to_device_lists_btn.setToolTipDuration(3)
        self.load_data_to_device_lists_btn.setCheckable(False)
        self.load_data_to_device_lists_btn.setChecked(False)

        self.horizontalLayout_4.addWidget(self.load_data_to_device_lists_btn)

        self.fill_fields_btn = QPushButton(self.frame_34)
        self.fill_fields_btn.setObjectName(u"fill_fields_btn")
        self.fill_fields_btn.setMinimumSize(QSize(200, 40))
        self.fill_fields_btn.setMaximumSize(QSize(350, 16777215))
        self.fill_fields_btn.setMouseTracking(True)
        self.fill_fields_btn.setFocusPolicy(Qt.StrongFocus)
        self.fill_fields_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.fill_fields_btn.setAcceptDrops(False)
        self.fill_fields_btn.setLayoutDirection(Qt.LeftToRight)
        self.fill_fields_btn.setCheckable(False)
        self.fill_fields_btn.setChecked(False)
        self.fill_fields_btn.setAutoDefault(False)
        self.fill_fields_btn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.fill_fields_btn)

        self.store_device_specs_btn = QPushButton(self.frame_34)
        self.store_device_specs_btn.setObjectName(u"store_device_specs_btn")
        self.store_device_specs_btn.setMinimumSize(QSize(200, 40))
        self.store_device_specs_btn.setMaximumSize(QSize(350, 16777215))
        self.store_device_specs_btn.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.store_device_specs_btn)


        self.verticalLayout_13.addWidget(self.frame_34, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_33)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.source_path_text_docu = QPlainTextEdit(self.frame_33)
        self.source_path_text_docu.setObjectName(u"source_path_text_docu")
        self.source_path_text_docu.setMinimumSize(QSize(0, 30))
        self.source_path_text_docu.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.source_path_text_docu, 1, 1, 1, 1)

        self.source_btn_docu = QPushButton(self.frame_33)
        self.source_btn_docu.setObjectName(u"source_btn_docu")
        sizePolicy.setHeightForWidth(self.source_btn_docu.sizePolicy().hasHeightForWidth())
        self.source_btn_docu.setSizePolicy(sizePolicy)
        self.source_btn_docu.setMinimumSize(QSize(250, 40))
        self.source_btn_docu.setMaximumSize(QSize(300, 30))

        self.gridLayout_20.addWidget(self.source_btn_docu, 1, 0, 1, 1, Qt.AlignVCenter)

        self.source_btn_matstr = QPushButton(self.frame_33)
        self.source_btn_matstr.setObjectName(u"source_btn_matstr")
        sizePolicy.setHeightForWidth(self.source_btn_matstr.sizePolicy().hasHeightForWidth())
        self.source_btn_matstr.setSizePolicy(sizePolicy)
        self.source_btn_matstr.setMinimumSize(QSize(250, 40))
        self.source_btn_matstr.setMaximumSize(QSize(300, 30))

        self.gridLayout_20.addWidget(self.source_btn_matstr, 0, 0, 1, 1, Qt.AlignVCenter)

        self.target_path_text_2 = QPlainTextEdit(self.frame_33)
        self.target_path_text_2.setObjectName(u"target_path_text_2")
        self.target_path_text_2.setMinimumSize(QSize(0, 30))
        self.target_path_text_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.target_path_text_2, 2, 1, 1, 1)

        self.target_path_btn_2 = QPushButton(self.frame_33)
        self.target_path_btn_2.setObjectName(u"target_path_btn_2")
        sizePolicy.setHeightForWidth(self.target_path_btn_2.sizePolicy().hasHeightForWidth())
        self.target_path_btn_2.setSizePolicy(sizePolicy)
        self.target_path_btn_2.setMinimumSize(QSize(250, 40))
        self.target_path_btn_2.setMaximumSize(QSize(300, 30))
        self.target_path_btn_2.setAutoDefault(False)
        self.target_path_btn_2.setFlat(False)

        self.gridLayout_20.addWidget(self.target_path_btn_2, 2, 0, 1, 1, Qt.AlignVCenter)

        self.source_path_text_matstr = QPlainTextEdit(self.frame_33)
        self.source_path_text_matstr.setObjectName(u"source_path_text_matstr")
        self.source_path_text_matstr.setMinimumSize(QSize(0, 30))
        self.source_path_text_matstr.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.source_path_text_matstr, 0, 1, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_33, 0, Qt.AlignVCenter)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.create_doc1_btn = QPushButton(self.frame_35)
        self.create_doc1_btn.setObjectName(u"create_doc1_btn")
        sizePolicy2.setHeightForWidth(self.create_doc1_btn.sizePolicy().hasHeightForWidth())
        self.create_doc1_btn.setSizePolicy(sizePolicy2)
        self.create_doc1_btn.setMinimumSize(QSize(250, 50))
        self.create_doc1_btn.setMaximumSize(QSize(400, 100))
        self.create_doc1_btn.setFont(font2)
        self.create_doc1_btn.setAutoDefault(True)
        self.create_doc1_btn.setFlat(False)

        self.horizontalLayout_17.addWidget(self.create_doc1_btn)

        self.create_doc2_btn = QPushButton(self.frame_35)
        self.create_doc2_btn.setObjectName(u"create_doc2_btn")
        sizePolicy2.setHeightForWidth(self.create_doc2_btn.sizePolicy().hasHeightForWidth())
        self.create_doc2_btn.setSizePolicy(sizePolicy2)
        self.create_doc2_btn.setMinimumSize(QSize(250, 50))
        self.create_doc2_btn.setMaximumSize(QSize(400, 100))
        self.create_doc2_btn.setFont(font2)
        self.create_doc2_btn.setAutoDefault(True)
        self.create_doc2_btn.setFlat(False)

        self.horizontalLayout_17.addWidget(self.create_doc2_btn)


        self.verticalLayout_13.addWidget(self.frame_35)


        self.frame0220.addWidget(self.frame_32)

        self.tabWidget.addTab(self.tab2, "")
        self.tab0 = QWidget()
        self.tab0.setObjectName(u"tab0")
        self.tab0.setMaximumSize(QSize(16777215, 500))
        self.tab0.setSizeIncrement(QSize(0, 0))
        self.gridLayout_8 = QGridLayout(self.tab0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_2 = QScrollArea(self.tab0)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents2 = QWidget()
        self.scrollAreaWidgetContents2.setObjectName(u"scrollAreaWidgetContents2")
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 1798, 480))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.server_sttings_headline_label = QLabel(self.scrollAreaWidgetContents2)
        self.server_sttings_headline_label.setObjectName(u"server_sttings_headline_label")
        sizePolicy2.setHeightForWidth(self.server_sttings_headline_label.sizePolicy().hasHeightForWidth())
        self.server_sttings_headline_label.setSizePolicy(sizePolicy2)
        self.server_sttings_headline_label.setMinimumSize(QSize(250, 30))
        self.server_sttings_headline_label.setMaximumSize(QSize(16777215, 25))
        self.server_sttings_headline_label.setSizeIncrement(QSize(5, 0))
        self.server_sttings_headline_label.setFont(font)
        self.server_sttings_headline_label.setFrameShape(QFrame.StyledPanel)
        self.server_sttings_headline_label.setFrameShadow(QFrame.Sunken)
        self.server_sttings_headline_label.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.server_sttings_headline_label)

        self.label = QLabel(self.scrollAreaWidgetContents2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.db_type = QComboBox(self.scrollAreaWidgetContents2)
        self.db_type.addItem("")
        self.db_type.addItem("")
        self.db_type.setObjectName(u"db_type")
        self.db_type.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.db_type)

        self.db_name_label = QLabel(self.scrollAreaWidgetContents2)
        self.db_name_label.setObjectName(u"db_name_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.db_name_label)

        self.db_name = QPlainTextEdit(self.scrollAreaWidgetContents2)
        self.db_name.setObjectName(u"db_name")
        self.db_name.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.db_name)

        self.db_server_label = QLabel(self.scrollAreaWidgetContents2)
        self.db_server_label.setObjectName(u"db_server_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.db_server_label)

        self.db_server = QPlainTextEdit(self.scrollAreaWidgetContents2)
        self.db_server.setObjectName(u"db_server")
        self.db_server.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.db_server)

        self.user_label = QLabel(self.scrollAreaWidgetContents2)
        self.user_label.setObjectName(u"user_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.user_label)

        self.user = QPlainTextEdit(self.scrollAreaWidgetContents2)
        self.user.setObjectName(u"user")
        self.user.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.user)

        self.pw_label = QLabel(self.scrollAreaWidgetContents2)
        self.pw_label.setObjectName(u"pw_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.pw_label)

        self.pw = QPlainTextEdit(self.scrollAreaWidgetContents2)
        self.pw.setObjectName(u"pw")
        self.pw.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pw)

        self.server_sttings_headline_label_2 = QLabel(self.scrollAreaWidgetContents2)
        self.server_sttings_headline_label_2.setObjectName(u"server_sttings_headline_label_2")
        sizePolicy2.setHeightForWidth(self.server_sttings_headline_label_2.sizePolicy().hasHeightForWidth())
        self.server_sttings_headline_label_2.setSizePolicy(sizePolicy2)
        self.server_sttings_headline_label_2.setMinimumSize(QSize(250, 30))
        self.server_sttings_headline_label_2.setMaximumSize(QSize(16777215, 0))
        self.server_sttings_headline_label_2.setSizeIncrement(QSize(5, 0))
        self.server_sttings_headline_label_2.setFont(font)
        self.server_sttings_headline_label_2.setFrameShape(QFrame.StyledPanel)
        self.server_sttings_headline_label_2.setFrameShadow(QFrame.Sunken)
        self.server_sttings_headline_label_2.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.server_sttings_headline_label_2)

        self.sql_query_btn = QPushButton(self.scrollAreaWidgetContents2)
        self.sql_query_btn.setObjectName(u"sql_query_btn")
        self.sql_query_btn.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.sql_query_btn)

        self.query_input = QPlainTextEdit(self.scrollAreaWidgetContents2)
        self.query_input.setObjectName(u"query_input")
        self.query_input.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.query_input.sizePolicy().hasHeightForWidth())
        self.query_input.setSizePolicy(sizePolicy10)
        self.query_input.setMinimumSize(QSize(0, 10))
        self.query_input.setMaximumSize(QSize(16777215, 60))
        self.query_input.setSizeIncrement(QSize(0, 500))
        self.query_input.setAutoFillBackground(True)
        self.query_input.setFrameShadow(QFrame.Raised)
        self.query_input.setTabChangesFocus(False)
        self.query_input.setUndoRedoEnabled(True)
        self.query_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.query_input)

        self.sql_query_2_btn = QPushButton(self.scrollAreaWidgetContents2)
        self.sql_query_2_btn.setObjectName(u"sql_query_2_btn")
        self.sql_query_2_btn.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.sql_query_2_btn)

        self.query_2_input = QPlainTextEdit(self.scrollAreaWidgetContents2)
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

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.query_2_input)


        self.gridLayout_9.addLayout(self.formLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_btn = QPushButton(self.scrollAreaWidgetContents2)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy11)
        self.save_btn.setMinimumSize(QSize(0, 0))
        self.save_btn.setMaximumSize(QSize(150, 30))

        self.horizontalLayout.addWidget(self.save_btn)

        self.load_btn = QPushButton(self.scrollAreaWidgetContents2)
        self.load_btn.setObjectName(u"load_btn")
        sizePolicy11.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy11)
        self.load_btn.setMinimumSize(QSize(0, 0))
        self.load_btn.setMaximumSize(QSize(150, 30))

        self.horizontalLayout.addWidget(self.load_btn)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout_9.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents2)

        self.gridLayout_8.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab0, "")

        self.gridLayout_22.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame02, 1, 0, 1, 1)


        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.frame0)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1890, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy12 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy12)
        self.toolBar.setStyleSheet(u"")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.load_articles_db_btn.setDefault(True)
        self.load_articles_file_btn.setDefault(True)
        self.source_path_btn.setDefault(True)
        self.target_path_btn.setDefault(True)
        self.paste_docs_btn.setDefault(True)
        self.fill_fields_btn.setDefault(False)
        self.target_path_btn_2.setDefault(False)
        self.create_doc1_btn.setDefault(False)
        self.create_doc2_btn.setDefault(False)
        self.sql_query_btn.setDefault(True)
        self.sql_query_2_btn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Projektnummer:", None))
        self.project.setPlainText(QCoreApplication.translate("MainWindow", u"SUN 20-000", None))
        self.project_name_label.setText(QCoreApplication.translate("MainWindow", u"Projektname:", None))
        self.project_name.setPlainText("")
        self.load_articles_db_btn.setText(QCoreApplication.translate("MainWindow", u"Lade Artikelliste aus DB", None))
        self.load_articles_file_btn.setText(QCoreApplication.translate("MainWindow", u"Lade Artikelliste aus Datei", None))
        ___qtablewidgetitem = self.articles_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem1 = self.articles_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem2 = self.articles_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Artikelbezeichnung", None));
        ___qtablewidgetitem3 = self.articles_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Menge verbraucht [Stk.]", None));
        self.source_path_btn.setText(QCoreApplication.translate("MainWindow", u"Quellpfad festlegen", None))
        self.source_path_text.setPlainText("")
        self.target_path_btn.setText(QCoreApplication.translate("MainWindow", u"Zielpfad festlegen", None))
        self.paste_docs_btn.setText(QCoreApplication.translate("MainWindow", u"Dokumente \u00fcbertragen", None))
        self.headline_01.setText(QCoreApplication.translate("MainWindow", u"Anlagen\u00fcbersicht", None))
        self.op_adress_3_label.setText(QCoreApplication.translate("MainWindow", u"Anlagenbetreiber:", None))
        self.op_adress_1_label.setText(QCoreApplication.translate("MainWindow", u"Stra\u00dfe:", None))
        self.op_adress_2_label.setText(QCoreApplication.translate("MainWindow", u"PLZ:", None))
        self.op_adress_3_label_2.setText(QCoreApplication.translate("MainWindow", u"Ort:", None))
        self.loc_head_label.setText(QCoreApplication.translate("MainWindow", u"Standort:", None))
        self.loc_adress_1_label.setText(QCoreApplication.translate("MainWindow", u"Stra\u00dfe:", None))
        self.loc_adress_2_label.setText(QCoreApplication.translate("MainWindow", u"PLZ:", None))
        self.loc_adress_3_label.setText(QCoreApplication.translate("MainWindow", u"Ort:", None))
        self.sys_perf_label.setText(QCoreApplication.translate("MainWindow", u"Bruttoleistung PV [kWp]:", None))
        self.constr_style_label.setText(QCoreApplication.translate("MainWindow", u"Errichtungsort:", None))
        self.constr_style_text.setPlainText(QCoreApplication.translate("MainWindow", u"Bauliche Anlage (Hausdach)", None))
        self.azimuth_head_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung:", None))
        self.bool_consist_azimuth_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung einheitlich?", None))
        self.bool_consist_azimuth_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ja", None))
        self.maj_card_point_label.setText(QCoreApplication.translate("MainWindow", u"\u00dcberwiegend:", None))
        self.min_azimuth_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung weitere:", None))
        self.min_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Neigungswinkel weitere:", None))
        self.min_card_point_text.setPlainText(QCoreApplication.translate("MainWindow", u"West", None))
        self.min_card_point_label.setText(QCoreApplication.translate("MainWindow", u"Weitere:", None))
        self.maj_azimuth_label.setText(QCoreApplication.translate("MainWindow", u"Ausrichtung \u00fcberwiegend:", None))
        self.maj_card_point_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ost", None))
        self.maj_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Neigungswinkel \u00fcberwiegend:", None))
        self.headline_02.setText(QCoreApplication.translate("MainWindow", u"Solargenerator", None))
        ___qtablewidgetitem4 = self.PV_modules_list.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem5 = self.PV_modules_list.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem6 = self.PV_modules_list.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Modul-Typ", None));
        ___qtablewidgetitem7 = self.PV_modules_list.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Menge verbraucht [Stk.]", None));
        ___qtablewidgetitem8 = self.PV_modules_list.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem9 = self.PV_modules_list.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Modulleistung [kWp]", None));
        self.move_none_PV_modules_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.module_count_label.setText(QCoreApplication.translate("MainWindow", u"Anzahl der Module:", None))
        self.module_count_text.setPlainText("")
        self.module_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.mounting_type_label.setText(QCoreApplication.translate("MainWindow", u"Montagesystem:", None))
        self.mounting_type_text.setPlainText(QCoreApplication.translate("MainWindow", u"PMT EVO 2.0 Ost-West", None))
        self.headline_03.setText(QCoreApplication.translate("MainWindow", u"PV-Wechselrichter", None))
        ___qtablewidgetitem10 = self.PV_inverters_list.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem11 = self.PV_inverters_list.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem12 = self.PV_inverters_list.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Wechselrichter-Typ", None));
        ___qtablewidgetitem13 = self.PV_inverters_list.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Menge verbraucht [Stk.]", None));
        ___qtablewidgetitem14 = self.PV_inverters_list.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem15 = self.PV_inverters_list.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete \n"
"WR-Leistung [kW]", None));
        self.move_none_PV_inverters_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.hybrid_inverter_bool_label.setText(QCoreApplication.translate("MainWindow", u"Gemeinsamer PV-Batterie-Wechselricher:", None))
        self.hybrid_inverter_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ja/Nein", None))
        self.commiss_date_label.setText(QCoreApplication.translate("MainWindow", u"Datum erstmalige\n"
"Inbetriebnahme:", None))
        self.inverter_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
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
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Menge verbraucht [Stk.]", None));
        ___qtablewidgetitem20 = self.BAT_inverters_list.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        ___qtablewidgetitem21 = self.BAT_inverters_list.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete \n"
"WR-Leistung [kW]", None));
        ___qtablewidgetitem22 = self.BAT_inverters_list.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Art der Kopplung", None));
        self.move_none_BAT_inverters_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.bat_inverter_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.bat_inverter_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.bat_inverter_power_label.setText(QCoreApplication.translate("MainWindow", u"Zugeordnete\n"
"Wechselrichterleistung [kW]:", None))
        self.coupling_type_label.setText(QCoreApplication.translate("MainWindow", u"Art der Kopplung:", None))
        self.coupling_type_text.setPlainText(QCoreApplication.translate("MainWindow", u"AC gekoppeltes System", None))
        self.headline_05.setText(QCoreApplication.translate("MainWindow", u"Speicher", None))
        ___qtablewidgetitem23 = self.BAT_storage_list.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem24 = self.BAT_storage_list.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem25 = self.BAT_storage_list.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Speicher-Typ", None));
        ___qtablewidgetitem26 = self.BAT_storage_list.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Menge verbraucht [Stk.]", None));
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
        self.bat_storage_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.bat_storage_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.bat_storage_cap_label.setText(QCoreApplication.translate("MainWindow", u"Nutzbare\n"
"Speicherkapazit\u00e4t:", None))
        self.bat_commiss_date_label.setText(QCoreApplication.translate("MainWindow", u"Datum erstmalige\n"
"Inbetriebnahme:", None))
        self.max_discharge_pow_label.setText(QCoreApplication.translate("MainWindow", u"Maximale Entladeleistung \n"
"im Dauerbetrieb:", None))
        self.em_pow_ability_bool_label.setText(QCoreApplication.translate("MainWindow", u"Notstromf\u00e4higkeit\n"
"bei Netzst\u00f6rungen: ", None))
        self.em_pow_ability_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Ja/Nein", None))
        self.energy_storage_type_label.setText(QCoreApplication.translate("MainWindow", u"Technologie der \n"
"Stromspeicherung:", None))
        self.bat_technology_label.setText(QCoreApplication.translate("MainWindow", u"Batterietechnologie:", None))
        self.headline_06.setText(QCoreApplication.translate("MainWindow", u"Ladestation", None))
        ___qtablewidgetitem31 = self.CHG_point_list.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"<>", None));
        ___qtablewidgetitem32 = self.CHG_point_list.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Artikelnummer", None));
        ___qtablewidgetitem33 = self.CHG_point_list.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Ladestations-Typ", None));
        ___qtablewidgetitem34 = self.CHG_point_list.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Menge verbraucht [Stk.]", None));
        ___qtablewidgetitem35 = self.CHG_point_list.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Seriennummer", None));
        self.move_none_CHG_point_to_blacklist.setText(QCoreApplication.translate("MainWindow", u"Entferne die markierten Artikel", None))
        self.charging_point_type_label.setText(QCoreApplication.translate("MainWindow", u"Typ:", None))
        self.charging_point_SN_label.setText(QCoreApplication.translate("MainWindow", u"Seriennummer:", None))
        self.headline_07.setText(QCoreApplication.translate("MainWindow", u"Anschlussart", None))
        self.feeding_type_label.setText(QCoreApplication.translate("MainWindow", u"Einspeisung:", None))
        self.feeding_type_text.setPlainText(QCoreApplication.translate("MainWindow", u"Volleinspeisung / Teileinspeisung (einschlie\u00dflich Eigenverbrauch) ", None))
        self.headline_08.setText(QCoreApplication.translate("MainWindow", u"Weitere Anlageneigenschaften", None))
        self.pow_limit_bool_label.setText(QCoreApplication.translate("MainWindow", u"Leistungsbegrenzung:", None))
        self.pow_limit_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.rmt_grd_op_bool_label.setText(QCoreApplication.translate("MainWindow", u"Fernsteuerbarkeit\n"
"durch Netzbetreiber:", None))
        self.rmt_grd_op_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.rmt_drct_mrktr_bool_label.setText(QCoreApplication.translate("MainWindow", u"Fernsteuerbarkeit\n"
"durch Direktvermarkter:", None))
        self.rmt_drct_mrktr_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.rmt_3rd_prt_bool_label.setText(QCoreApplication.translate("MainWindow", u"Fernsteuerbarkeit\n"
"durch Dritte:", None))
        self.rmt_3rd_prt_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.prequali_bool_label.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e4qualifikation\n"
"f\u00fcr Regelenergie:", None))
        self.prequali_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.citizen_corp_bool_label.setText(QCoreApplication.translate("MainWindow", u"Anlagenbetreiber ist eine \n"
"B\u00fcrgerenergiegesellschaft:", None))
        self.citizen_corp_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.tendering_bool_label.setText(QCoreApplication.translate("MainWindow", u"Erlangung der PV-Anlage \u00fcber \n"
"Zuschlag in einer Ausschreibung:", None))
        self.tendering_bool_text.setPlainText(QCoreApplication.translate("MainWindow", u"Nein", None))
        self.headline_09.setText(QCoreApplication.translate("MainWindow", u"AC-seitige Komponenten", None))
        self.meter_box_type_label.setText(QCoreApplication.translate("MainWindow", u"Energiez\u00e4hler:", None))
        self.meter_cabinet_label.setText(QCoreApplication.translate("MainWindow", u"Z\u00e4hlerschrank:", None))
        self.headline_10.setText(QCoreApplication.translate("MainWindow", u"Kommunikation und Anlagen\u00fcberwachung", None))
        self.dl_type_label.setText(QCoreApplication.translate("MainWindow", u"Datenlogger:", None))
        self.dl_connect_ext_label.setText(QCoreApplication.translate("MainWindow", u"Externer Zugriff:", None))
#if QT_CONFIG(tooltip)
        self.load_data_to_device_lists_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Module, Wechselrichter, </p><p>Batteriewechselrichter, Speicher, Ladestation</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.load_data_to_device_lists_btn.setText(QCoreApplication.translate("MainWindow", u"1. Lade Ger\u00e4telisten", None))
        self.fill_fields_btn.setText(QCoreApplication.translate("MainWindow", u"2. F\u00fclle  Formularfelder", None))
        self.store_device_specs_btn.setText(QCoreApplication.translate("MainWindow", u"Hinterlege technische Daten", None))
        self.source_btn_docu.setText(QCoreApplication.translate("MainWindow", u"Template Dokumentation", None))
        self.source_btn_matstr.setText(QCoreApplication.translate("MainWindow", u"Template gem. MatStR", None))
        self.target_path_btn_2.setText(QCoreApplication.translate("MainWindow", u"Ablagepfad f\u00fcr Dokumente ausw\u00e4hlen", None))
        self.create_doc1_btn.setText(QCoreApplication.translate("MainWindow", u"Doku gem\u00e4\u00df MaStR erzeugen", None))
        self.create_doc2_btn.setText(QCoreApplication.translate("MainWindow", u"SUN-Doku erzeugen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Doku gem. MatStR", None))
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
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.load_btn.setText(QCoreApplication.translate("MainWindow", u"Laden", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

