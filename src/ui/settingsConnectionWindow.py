# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\3441\Documents\Familie\Edgar\Weiterbildungen\Kurse\Python Bootcamp\Projekte\SUN_Article_Fetcher\src/ui\settingsConnectionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.server_settings_headline_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.server_settings_headline_label.sizePolicy().hasHeightForWidth())
        self.server_settings_headline_label.setSizePolicy(sizePolicy)
        self.server_settings_headline_label.setMinimumSize(
            QtCore.QSize(250, 30))
        self.server_settings_headline_label.setMaximumSize(
            QtCore.QSize(16777215, 25))
        self.server_settings_headline_label.setSizeIncrement(
            QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.server_settings_headline_label.setFont(font)
        self.server_settings_headline_label.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.server_settings_headline_label.setFrameShadow(
            QtWidgets.QFrame.Sunken)
        self.server_settings_headline_label.setTextFormat(QtCore.Qt.AutoText)
        self.server_settings_headline_label.setObjectName(
            "server_settings_headline_label")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.server_settings_headline_label)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.db_type = QtWidgets.QComboBox(Dialog)
        self.db_type.setMaximumSize(QtCore.QSize(100, 16777215))
        self.db_type.setFrame(True)
        self.db_type.setModelColumn(0)
        self.db_type.setObjectName("db_type")
        self.db_type.addItem("")
        self.db_type.addItem("")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.db_type)
        self.db_name_label = QtWidgets.QLabel(Dialog)
        self.db_name_label.setObjectName("db_name_label")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.db_name_label)
        self.db_name = QtWidgets.QPlainTextEdit(Dialog)
        self.db_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.db_name.setObjectName("db_name")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.db_name)
        self.db_server_label = QtWidgets.QLabel(Dialog)
        self.db_server_label.setObjectName("db_server_label")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.db_server_label)
        self.db_server = QtWidgets.QPlainTextEdit(Dialog)
        self.db_server.setMaximumSize(QtCore.QSize(16777215, 25))
        self.db_server.setObjectName("db_server")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.db_server)
        self.user_label = QtWidgets.QLabel(Dialog)
        self.user_label.setObjectName("user_label")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.user_label)
        self.user = QtWidgets.QPlainTextEdit(Dialog)
        self.user.setMaximumSize(QtCore.QSize(16777215, 25))
        self.user.setObjectName("user")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.user)
        self.pw_label = QtWidgets.QLabel(Dialog)
        self.pw_label.setObjectName("pw_label")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.pw_label)
        self.pw = QtWidgets.QPlainTextEdit(Dialog)
        self.pw.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pw.setObjectName("pw")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pw)
        self.server_settings_headline_label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.server_settings_headline_label_2.sizePolicy().hasHeightForWidth())
        self.server_settings_headline_label_2.setSizePolicy(sizePolicy)
        self.server_settings_headline_label_2.setMinimumSize(
            QtCore.QSize(250, 30))
        self.server_settings_headline_label_2.setMaximumSize(
            QtCore.QSize(16777215, 0))
        self.server_settings_headline_label_2.setSizeIncrement(
            QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.server_settings_headline_label_2.setFont(font)
        self.server_settings_headline_label_2.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.server_settings_headline_label_2.setFrameShadow(
            QtWidgets.QFrame.Sunken)
        self.server_settings_headline_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.server_settings_headline_label_2.setObjectName(
            "server_settings_headline_label_2")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.SpanningRole, self.server_settings_headline_label_2)
        self.sql_query_btn = QtWidgets.QPushButton(Dialog)
        self.sql_query_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.sql_query_btn.setDefault(True)
        self.sql_query_btn.setObjectName("sql_query_btn")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.SpanningRole, self.sql_query_btn)
        self.query_input = QtWidgets.QPlainTextEdit(Dialog)
        self.query_input.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.query_input.sizePolicy().hasHeightForWidth())
        self.query_input.setSizePolicy(sizePolicy)
        self.query_input.setMinimumSize(QtCore.QSize(0, 10))
        self.query_input.setMaximumSize(QtCore.QSize(16777215, 60))
        self.query_input.setSizeIncrement(QtCore.QSize(0, 500))
        self.query_input.setAutoFillBackground(True)
        self.query_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.query_input.setTabChangesFocus(False)
        self.query_input.setUndoRedoEnabled(True)
        self.query_input.setPlainText("")
        self.query_input.setTextInteractionFlags(
            QtCore.Qt.TextEditorInteraction)
        self.query_input.setObjectName("query_input")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.SpanningRole, self.query_input)
        self.sql_query_2_btn = QtWidgets.QPushButton(Dialog)
        self.sql_query_2_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.sql_query_2_btn.setDefault(True)
        self.sql_query_2_btn.setObjectName("sql_query_2_btn")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.SpanningRole, self.sql_query_2_btn)
        self.query_2_input = QtWidgets.QPlainTextEdit(Dialog)
        self.query_2_input.setEnabled(True)
        self.query_2_input.setMinimumSize(QtCore.QSize(0, 40))
        self.query_2_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.query_2_input.setSizeIncrement(QtCore.QSize(0, 500))
        self.query_2_input.setAutoFillBackground(True)
        self.query_2_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.query_2_input.setTabChangesFocus(False)
        self.query_2_input.setUndoRedoEnabled(True)
        self.query_2_input.setPlainText("")
        self.query_2_input.setTextInteractionFlags(
            QtCore.Qt.TextEditorInteraction)
        self.query_2_input.setObjectName("query_2_input")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.SpanningRole, self.query_2_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.server_settings_headline_label.setText(
            _translate("Dialog", "Servereinstellungen"))
        self.label.setText(_translate("Dialog", "Datenbanktyp:"))
        self.db_type.setItemText(0, _translate("Dialog", "PostgreSQL"))
        self.db_type.setItemText(1, _translate("Dialog", "MySQL"))
        self.db_name_label.setText(_translate("Dialog", "Datenbankname:"))
        self.db_server_label.setText(_translate("Dialog", "Server:Port:"))
        self.user_label.setText(_translate("Dialog", "User:"))
        self.pw_label.setText(_translate("Dialog", "Passwort:"))
        self.server_settings_headline_label_2.setText(
            _translate("Dialog", "Queries zur Abfrage von Datenbank"))
        self.sql_query_btn.setText(_translate(
            "Dialog", "Datenbank-Abfrage eingeben (Übertragung von Doklumenten)"))
        self.sql_query_2_btn.setText(_translate(
            "Dialog", "Datenbank-Abfrage eingeben (Doku gem. MatStR)"))
