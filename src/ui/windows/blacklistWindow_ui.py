# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blacklistWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractScrollArea, QApplication,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_blacklist_dialog(object):
    def setupUi(self, blacklist_dialog):
        if not blacklist_dialog.objectName():
            blacklist_dialog.setObjectName(u"blacklist_dialog")
        blacklist_dialog.resize(1500, 800)
        self.verticalLayout_2 = QVBoxLayout(blacklist_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(blacklist_dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.blacklist = QTableWidget(self.frame_2)
        if (self.blacklist.columnCount() < 5):
            self.blacklist.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.blacklist.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.blacklist.setObjectName(u"blacklist")
        self.blacklist.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blacklist.sizePolicy().hasHeightForWidth())
        self.blacklist.setSizePolicy(sizePolicy)
        self.blacklist.setMinimumSize(QSize(500, 100))
        self.blacklist.setMaximumSize(QSize(456456, 4554))
        self.blacklist.setAutoFillBackground(True)
        self.blacklist.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.blacklist.setDragDropOverwriteMode(False)
        self.blacklist.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.blacklist.setAlternatingRowColors(True)
        self.blacklist.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.blacklist.setGridStyle(Qt.SolidLine)
        self.blacklist.setSortingEnabled(True)
        self.blacklist.setWordWrap(False)
        self.blacklist.setCornerButtonEnabled(True)
        self.blacklist.horizontalHeader().setVisible(True)
        self.blacklist.horizontalHeader().setCascadingSectionResizes(True)
        self.blacklist.horizontalHeader().setMinimumSectionSize(60)
        self.blacklist.horizontalHeader().setDefaultSectionSize(180)
        self.blacklist.horizontalHeader().setHighlightSections(True)
        self.blacklist.horizontalHeader().setProperty("showSortIndicator", True)
        self.blacklist.horizontalHeader().setStretchLastSection(False)
        self.blacklist.verticalHeader().setVisible(False)
        self.blacklist.verticalHeader().setCascadingSectionResizes(False)
        self.blacklist.verticalHeader().setMinimumSectionSize(5)
        self.blacklist.verticalHeader().setHighlightSections(True)
        self.blacklist.verticalHeader().setProperty("showSortIndicator", True)
        self.blacklist.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.blacklist)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.buttonBox = QDialogButtonBox(blacklist_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_2.addWidget(self.buttonBox, 0, Qt.AlignLeft)


        self.retranslateUi(blacklist_dialog)
        self.buttonBox.accepted.connect(blacklist_dialog.accept)
        self.buttonBox.rejected.connect(blacklist_dialog.reject)

        QMetaObject.connectSlotsByName(blacklist_dialog)
    # setupUi

    def retranslateUi(self, blacklist_dialog):
        blacklist_dialog.setWindowTitle(QCoreApplication.translate("blacklist_dialog", u"Dialog", None))
        ___qtablewidgetitem = self.blacklist.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("blacklist_dialog", u"<>", None));
        ___qtablewidgetitem1 = self.blacklist.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("blacklist_dialog", u"Artikelnummer", None));
        ___qtablewidgetitem2 = self.blacklist.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("blacklist_dialog", u"Artikelbezeichnung", None));
        ___qtablewidgetitem3 = self.blacklist.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("blacklist_dialog", u"hinzugef\u00fcgt am", None));
        ___qtablewidgetitem4 = self.blacklist.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("blacklist_dialog", u"-->", None));
    # retranslateUi

