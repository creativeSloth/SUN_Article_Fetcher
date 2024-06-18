# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsConnectionWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(746, 470)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.server_settings_headline_label = QLabel(self.frame)
        self.server_settings_headline_label.setObjectName(u"server_settings_headline_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.server_settings_headline_label.sizePolicy().hasHeightForWidth())
        self.server_settings_headline_label.setSizePolicy(sizePolicy1)
        self.server_settings_headline_label.setMinimumSize(QSize(250, 30))
        self.server_settings_headline_label.setMaximumSize(QSize(16777215, 25))
        self.server_settings_headline_label.setSizeIncrement(QSize(5, 0))
        font = QFont()
        font.setFamilies([u"Sitka Heading"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.server_settings_headline_label.setFont(font)
        self.server_settings_headline_label.setFrameShape(QFrame.StyledPanel)
        self.server_settings_headline_label.setFrameShadow(QFrame.Sunken)
        self.server_settings_headline_label.setTextFormat(Qt.AutoText)

        self.verticalLayout_4.addWidget(self.server_settings_headline_label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.user_label = QLabel(self.frame_2)
        self.user_label.setObjectName(u"user_label")
        sizePolicy.setHeightForWidth(self.user_label.sizePolicy().hasHeightForWidth())
        self.user_label.setSizePolicy(sizePolicy)
        self.user_label.setMinimumSize(QSize(0, 30))
        self.user_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.user_label, 3, 0, 1, 1, Qt.AlignLeft)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.db_name_label = QLabel(self.frame_2)
        self.db_name_label.setObjectName(u"db_name_label")
        sizePolicy.setHeightForWidth(self.db_name_label.sizePolicy().hasHeightForWidth())
        self.db_name_label.setSizePolicy(sizePolicy)
        self.db_name_label.setMinimumSize(QSize(0, 30))
        self.db_name_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.db_name_label, 1, 0, 1, 1, Qt.AlignLeft)

        self.pw = QLineEdit(self.frame_2)
        self.pw.setObjectName(u"pw")
        self.pw.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pw, 3, 4, 1, 1)

        self.db_server = QLineEdit(self.frame_2)
        self.db_server.setObjectName(u"db_server")

        self.gridLayout.addWidget(self.db_server, 1, 4, 1, 1)

        self.pw_label = QLabel(self.frame_2)
        self.pw_label.setObjectName(u"pw_label")
        sizePolicy.setHeightForWidth(self.pw_label.sizePolicy().hasHeightForWidth())
        self.pw_label.setSizePolicy(sizePolicy)
        self.pw_label.setMinimumSize(QSize(0, 30))
        self.pw_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.pw_label, 3, 3, 1, 1, Qt.AlignLeft)

        self.user = QLineEdit(self.frame_2)
        self.user.setObjectName(u"user")

        self.gridLayout.addWidget(self.user, 3, 2, 1, 1)

        self.db_name = QLineEdit(self.frame_2)
        self.db_name.setObjectName(u"db_name")

        self.gridLayout.addWidget(self.db_name, 1, 2, 1, 1)

        self.db_server_label = QLabel(self.frame_2)
        self.db_server_label.setObjectName(u"db_server_label")
        sizePolicy.setHeightForWidth(self.db_server_label.sizePolicy().hasHeightForWidth())
        self.db_server_label.setSizePolicy(sizePolicy)
        self.db_server_label.setMinimumSize(QSize(0, 30))
        self.db_server_label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.db_server_label, 1, 3, 1, 1, Qt.AlignLeft)

        self.db_type = QComboBox(self.frame_2)
        self.db_type.addItem("")
        self.db_type.addItem("")
        self.db_type.setObjectName(u"db_type")
        sizePolicy1.setHeightForWidth(self.db_type.sizePolicy().hasHeightForWidth())
        self.db_type.setSizePolicy(sizePolicy1)
        self.db_type.setMaximumSize(QSize(100, 16777215))
        self.db_type.setFrame(True)
        self.db_type.setModelColumn(0)

        self.gridLayout.addWidget(self.db_type, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.server_settings_headline_label_2 = QLabel(self.frame)
        self.server_settings_headline_label_2.setObjectName(u"server_settings_headline_label_2")
        sizePolicy1.setHeightForWidth(self.server_settings_headline_label_2.sizePolicy().hasHeightForWidth())
        self.server_settings_headline_label_2.setSizePolicy(sizePolicy1)
        self.server_settings_headline_label_2.setMinimumSize(QSize(250, 30))
        self.server_settings_headline_label_2.setMaximumSize(QSize(16777215, 0))
        self.server_settings_headline_label_2.setSizeIncrement(QSize(5, 0))
        self.server_settings_headline_label_2.setFont(font)
        self.server_settings_headline_label_2.setFrameShape(QFrame.StyledPanel)
        self.server_settings_headline_label_2.setFrameShadow(QFrame.Sunken)
        self.server_settings_headline_label_2.setTextFormat(Qt.AutoText)

        self.verticalLayout_4.addWidget(self.server_settings_headline_label_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sql_query_btn = QPushButton(self.frame_3)
        self.sql_query_btn.setObjectName(u"sql_query_btn")
        self.sql_query_btn.setMinimumSize(QSize(300, 25))

        self.verticalLayout_3.addWidget(self.sql_query_btn)

        self.query_input = QPlainTextEdit(self.frame_3)
        self.query_input.setObjectName(u"query_input")
        self.query_input.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.query_input.sizePolicy().hasHeightForWidth())
        self.query_input.setSizePolicy(sizePolicy1)
        self.query_input.setMinimumSize(QSize(300, 10))
        self.query_input.setMaximumSize(QSize(16777215, 80))
        self.query_input.setSizeIncrement(QSize(0, 500))
        self.query_input.setAutoFillBackground(True)
        self.query_input.setFrameShadow(QFrame.Raised)
        self.query_input.setTabChangesFocus(False)
        self.query_input.setUndoRedoEnabled(True)
        self.query_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_3.addWidget(self.query_input)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sql_query_2_btn = QPushButton(self.frame_4)
        self.sql_query_2_btn.setObjectName(u"sql_query_2_btn")
        self.sql_query_2_btn.setMinimumSize(QSize(300, 25))

        self.verticalLayout_2.addWidget(self.sql_query_2_btn)

        self.query_2_input = QPlainTextEdit(self.frame_4)
        self.query_2_input.setObjectName(u"query_2_input")
        self.query_2_input.setEnabled(True)
        self.query_2_input.setMinimumSize(QSize(300, 40))
        self.query_2_input.setMaximumSize(QSize(16777215, 80))
        self.query_2_input.setSizeIncrement(QSize(0, 500))
        self.query_2_input.setAutoFillBackground(True)
        self.query_2_input.setFrameShadow(QFrame.Raised)
        self.query_2_input.setTabChangesFocus(False)
        self.query_2_input.setUndoRedoEnabled(True)
        self.query_2_input.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_2.addWidget(self.query_2_input)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignLeft)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.db_type.setCurrentIndex(0)
        self.sql_query_btn.setDefault(True)
        self.sql_query_2_btn.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.server_settings_headline_label.setText(QCoreApplication.translate("Dialog", u"Servereinstellungen", None))
        self.user_label.setText(QCoreApplication.translate("Dialog", u"User:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Datenbanktyp:", None))
        self.db_name_label.setText(QCoreApplication.translate("Dialog", u"Datenbankname:", None))
        self.pw_label.setText(QCoreApplication.translate("Dialog", u"Passwort:", None))
        self.db_name.setText("")
        self.db_server_label.setText(QCoreApplication.translate("Dialog", u"Server:Port:", None))
        self.db_type.setItemText(0, QCoreApplication.translate("Dialog", u"PostgreSQL", None))
        self.db_type.setItemText(1, QCoreApplication.translate("Dialog", u"MySQL", None))

        self.server_settings_headline_label_2.setText(QCoreApplication.translate("Dialog", u"Queries zur Abfrage von Datenbank", None))
        self.sql_query_btn.setText(QCoreApplication.translate("Dialog", u"\u00dcbertragung von Dokumenten", None))
        self.query_input.setPlainText("")
        self.sql_query_2_btn.setText(QCoreApplication.translate("Dialog", u"Doku gem. MatStR", None))
        self.query_2_input.setPlainText("")
    # retranslateUi

