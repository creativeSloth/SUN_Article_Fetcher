# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\3441\Documents\Familie\Edgar\Weiterbildungen\Kurse\Python Bootcamp\Projekte\SUN_Article_Fetcher\src/ui/windows\blacklistWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_blacklist_dialog(object):
    def setupUi(self, blacklist_dialog):
        blacklist_dialog.setObjectName("blacklist_dialog")
        blacklist_dialog.resize(1500, 800)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(blacklist_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(blacklist_dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.blacklist = QtWidgets.QTableWidget(self.frame_2)
        self.blacklist.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blacklist.sizePolicy().hasHeightForWidth())
        self.blacklist.setSizePolicy(sizePolicy)
        self.blacklist.setMinimumSize(QtCore.QSize(500, 100))
        self.blacklist.setMaximumSize(QtCore.QSize(456456, 4554))
        self.blacklist.setAutoFillBackground(True)
        self.blacklist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.blacklist.setDragDropOverwriteMode(False)
        self.blacklist.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.blacklist.setAlternatingRowColors(True)
        self.blacklist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.blacklist.setGridStyle(QtCore.Qt.SolidLine)
        self.blacklist.setWordWrap(False)
        self.blacklist.setCornerButtonEnabled(True)
        self.blacklist.setObjectName("blacklist")
        self.blacklist.setColumnCount(4)
        self.blacklist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(3, item)
        self.blacklist.horizontalHeader().setVisible(True)
        self.blacklist.horizontalHeader().setCascadingSectionResizes(True)
        self.blacklist.horizontalHeader().setDefaultSectionSize(180)
        self.blacklist.horizontalHeader().setHighlightSections(True)
        self.blacklist.horizontalHeader().setMinimumSectionSize(60)
        self.blacklist.horizontalHeader().setSortIndicatorShown(True)
        self.blacklist.horizontalHeader().setStretchLastSection(False)
        self.blacklist.verticalHeader().setVisible(False)
        self.blacklist.verticalHeader().setCascadingSectionResizes(False)
        self.blacklist.verticalHeader().setHighlightSections(True)
        self.blacklist.verticalHeader().setMinimumSectionSize(5)
        self.blacklist.verticalHeader().setSortIndicatorShown(True)
        self.blacklist.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.blacklist)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(blacklist_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox, 0, QtCore.Qt.AlignLeft)

        self.retranslateUi(blacklist_dialog)
        self.buttonBox.accepted.connect(blacklist_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(blacklist_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(blacklist_dialog)

    def retranslateUi(self, blacklist_dialog):
        _translate = QtCore.QCoreApplication.translate
        blacklist_dialog.setWindowTitle(_translate("blacklist_dialog", "Dialog"))
        self.blacklist.setSortingEnabled(True)
        item = self.blacklist.horizontalHeaderItem(0)
        item.setText(_translate("blacklist_dialog", "<>"))
        item = self.blacklist.horizontalHeaderItem(1)
        item.setText(_translate("blacklist_dialog", "Artikelnummer"))
        item = self.blacklist.horizontalHeaderItem(2)
        item.setText(_translate("blacklist_dialog", "Artikelbezeichnung"))
        item = self.blacklist.horizontalHeaderItem(3)
        item.setText(_translate("blacklist_dialog", "-->"))
