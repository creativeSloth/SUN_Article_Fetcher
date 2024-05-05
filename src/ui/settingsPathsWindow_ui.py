# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsPathsWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1700, 480)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(Dialog)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.source_paths_Doc_Fetcher_headline_label = QLabel(self.frame)
        self.source_paths_Doc_Fetcher_headline_label.setObjectName(u"source_paths_Doc_Fetcher_headline_label")
        self.source_paths_Doc_Fetcher_headline_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.source_paths_Doc_Fetcher_headline_label.sizePolicy().hasHeightForWidth())
        self.source_paths_Doc_Fetcher_headline_label.setSizePolicy(sizePolicy)
        self.source_paths_Doc_Fetcher_headline_label.setMinimumSize(QSize(500, 30))
        self.source_paths_Doc_Fetcher_headline_label.setMaximumSize(QSize(16777215, 30))
        self.source_paths_Doc_Fetcher_headline_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Sitka Heading"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.source_paths_Doc_Fetcher_headline_label.setFont(font)
        self.source_paths_Doc_Fetcher_headline_label.setFrameShape(QFrame.StyledPanel)
        self.source_paths_Doc_Fetcher_headline_label.setFrameShadow(QFrame.Sunken)
        self.source_paths_Doc_Fetcher_headline_label.setTextFormat(Qt.AutoText)

        self.verticalLayout.addWidget(self.source_paths_Doc_Fetcher_headline_label)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.source_path_btn = QPushButton(self.frame_3)
        self.source_path_btn.setObjectName(u"source_path_btn")
        sizePolicy.setHeightForWidth(self.source_path_btn.sizePolicy().hasHeightForWidth())
        self.source_path_btn.setSizePolicy(sizePolicy)
        self.source_path_btn.setMinimumSize(QSize(250, 40))
        self.source_path_btn.setMaximumSize(QSize(300, 40))
        self.source_path_btn.setAutoDefault(False)

        self.horizontalLayout_8.addWidget(self.source_path_btn)

        self.source_path_text = QPlainTextEdit(self.frame_3)
        self.source_path_text.setObjectName(u"source_path_text")
        self.source_path_text.setEnabled(False)
        sizePolicy.setHeightForWidth(self.source_path_text.sizePolicy().hasHeightForWidth())
        self.source_path_text.setSizePolicy(sizePolicy)
        self.source_path_text.setMinimumSize(QSize(1300, 40))
        self.source_path_text.setMaximumSize(QSize(1800, 40))

        self.horizontalLayout_8.addWidget(self.source_path_text)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame_8)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.templates_paths_headline_label_2 = QLabel(self.frame_2)
        self.templates_paths_headline_label_2.setObjectName(u"templates_paths_headline_label_2")
        self.templates_paths_headline_label_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.templates_paths_headline_label_2.sizePolicy().hasHeightForWidth())
        self.templates_paths_headline_label_2.setSizePolicy(sizePolicy)
        self.templates_paths_headline_label_2.setMinimumSize(QSize(500, 30))
        self.templates_paths_headline_label_2.setMaximumSize(QSize(16777215, 30))
        self.templates_paths_headline_label_2.setSizeIncrement(QSize(0, 0))
        self.templates_paths_headline_label_2.setFont(font)
        self.templates_paths_headline_label_2.setFrameShape(QFrame.StyledPanel)
        self.templates_paths_headline_label_2.setFrameShadow(QFrame.Sunken)
        self.templates_paths_headline_label_2.setTextFormat(Qt.AutoText)

        self.verticalLayout_3.addWidget(self.templates_paths_headline_label_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.source_btn_matstr = QPushButton(self.frame_5)
        self.source_btn_matstr.setObjectName(u"source_btn_matstr")
        sizePolicy.setHeightForWidth(self.source_btn_matstr.sizePolicy().hasHeightForWidth())
        self.source_btn_matstr.setSizePolicy(sizePolicy)
        self.source_btn_matstr.setMinimumSize(QSize(250, 40))
        self.source_btn_matstr.setMaximumSize(QSize(300, 30))

        self.horizontalLayout.addWidget(self.source_btn_matstr)

        self.source_path_text_matstr = QPlainTextEdit(self.frame_5)
        self.source_path_text_matstr.setObjectName(u"source_path_text_matstr")
        self.source_path_text_matstr.setEnabled(False)
        sizePolicy.setHeightForWidth(self.source_path_text_matstr.sizePolicy().hasHeightForWidth())
        self.source_path_text_matstr.setSizePolicy(sizePolicy)
        self.source_path_text_matstr.setMinimumSize(QSize(1300, 40))
        self.source_path_text_matstr.setMaximumSize(QSize(1800, 30))

        self.horizontalLayout.addWidget(self.source_path_text_matstr)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.source_btn_docu = QPushButton(self.frame_6)
        self.source_btn_docu.setObjectName(u"source_btn_docu")
        sizePolicy.setHeightForWidth(self.source_btn_docu.sizePolicy().hasHeightForWidth())
        self.source_btn_docu.setSizePolicy(sizePolicy)
        self.source_btn_docu.setMinimumSize(QSize(250, 40))
        self.source_btn_docu.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_2.addWidget(self.source_btn_docu)

        self.source_path_text_docu = QPlainTextEdit(self.frame_6)
        self.source_path_text_docu.setObjectName(u"source_path_text_docu")
        self.source_path_text_docu.setEnabled(False)
        sizePolicy.setHeightForWidth(self.source_path_text_docu.sizePolicy().hasHeightForWidth())
        self.source_path_text_docu.setSizePolicy(sizePolicy)
        self.source_path_text_docu.setMinimumSize(QSize(1300, 40))
        self.source_path_text_docu.setMaximumSize(QSize(1800, 30))

        self.horizontalLayout_2.addWidget(self.source_path_text_docu)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_6.addWidget(self.buttonBox, 0, Qt.AlignLeft)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.source_path_btn.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.source_paths_Doc_Fetcher_headline_label.setText(QCoreApplication.translate("Dialog", u"\u00dcbertragung von Dokumenten", None))
        self.source_path_btn.setText(QCoreApplication.translate("Dialog", u"Quellpfad festlegen", None))
        self.source_path_text.setPlainText("")
        self.templates_paths_headline_label_2.setText(QCoreApplication.translate("Dialog", u"Erstellung der Dokumentation", None))
        self.source_btn_matstr.setText(QCoreApplication.translate("Dialog", u"Template gem. MatStR", None))
        self.source_btn_docu.setText(QCoreApplication.translate("Dialog", u"Template Dokumentation", None))
    # retranslateUi

