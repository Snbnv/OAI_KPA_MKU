# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oai_kpa_mku_widget_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 400)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.userFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userFrame.sizePolicy().hasHeightForWidth())
        self.userFrame.setSizePolicy(sizePolicy)
        self.userFrame.setStatusTip("")
        self.userFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userFrame.setObjectName("userFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.userFrame)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 0)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_KU5 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU5.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU5.setSizeIncrement(QtCore.QSize(130, 40))
        self.pushButton_KU5.setToolTip("")
        self.pushButton_KU5.setObjectName("pushButton_KU5")
        self.gridLayout_2.addWidget(self.pushButton_KU5, 1, 2, 1, 1)
        self.pushButton_KU14 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU14.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU14.setToolTip("")
        self.pushButton_KU14.setObjectName("pushButton_KU14")
        self.gridLayout_2.addWidget(self.pushButton_KU14, 5, 2, 1, 1)
        self.pushButton_KU16 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU16.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU16.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU16.setToolTip("")
        self.pushButton_KU16.setObjectName("pushButton_KU16")
        self.gridLayout_2.addWidget(self.pushButton_KU16, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 4, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.userFrame)
        self.spinBox.setStatusTip("")
        self.spinBox.setWhatsThis("")
        self.spinBox.setMinimum(50)
        self.spinBox.setMaximum(500)
        self.spinBox.setSingleStep(10)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 6, 2, 1, 1)
        self.pushButton_KU2 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU2.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU2.setObjectName("pushButton_KU2")
        self.gridLayout_2.addWidget(self.pushButton_KU2, 3, 0, 1, 1)
        self.pushButton_KU7 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU7.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU7.setToolTip("")
        self.pushButton_KU7.setObjectName("pushButton_KU7")
        self.gridLayout_2.addWidget(self.pushButton_KU7, 1, 3, 1, 1)
        self.pushButton_KU1 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU1.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU1.setObjectName("pushButton_KU1")
        self.gridLayout_2.addWidget(self.pushButton_KU1, 1, 0, 1, 1)
        self.pushButton_KU6 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU6.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU6.setToolTip("")
        self.pushButton_KU6.setObjectName("pushButton_KU6")
        self.gridLayout_2.addWidget(self.pushButton_KU6, 3, 2, 1, 1)
        self.pushButton_KU12 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU12.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU12.setToolTip("")
        self.pushButton_KU12.setObjectName("pushButton_KU12")
        self.gridLayout_2.addWidget(self.pushButton_KU12, 5, 1, 1, 1)
        self.pushButton_KU15 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU15.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU15.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU15.setToolTip("")
        self.pushButton_KU15.setObjectName("pushButton_KU15")
        self.gridLayout_2.addWidget(self.pushButton_KU15, 4, 3, 1, 1)
        self.pushButton_KU10 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU10.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU10.setObjectName("pushButton_KU10")
        self.gridLayout_2.addWidget(self.pushButton_KU10, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem1, 7, 2, 1, 1)
        self.pushButton_KU11 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU11.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU11.setToolTip("")
        self.pushButton_KU11.setObjectName("pushButton_KU11")
        self.gridLayout_2.addWidget(self.pushButton_KU11, 4, 1, 1, 1)
        self.pushButton_KU3 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU3.setObjectName("pushButton_KU3")
        self.gridLayout_2.addWidget(self.pushButton_KU3, 1, 1, 1, 1)
        self.pushButton_KU8 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU8.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU8.setToolTip("")
        self.pushButton_KU8.setObjectName("pushButton_KU8")
        self.gridLayout_2.addWidget(self.pushButton_KU8, 3, 3, 1, 1)
        self.pushButton_KU4 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU4.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU4.setObjectName("pushButton_KU4")
        self.gridLayout_2.addWidget(self.pushButton_KU4, 3, 1, 1, 1)
        self.pushButton_KU9 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU9.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU9.setObjectName("pushButton_KU9")
        self.gridLayout_2.addWidget(self.pushButton_KU9, 4, 0, 1, 1)
        self.pushButton_KU13 = QtWidgets.QPushButton(self.userFrame)
        self.pushButton_KU13.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_KU13.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_KU13.setToolTip("")
        self.pushButton_KU13.setObjectName("pushButton_KU13")
        self.gridLayout_2.addWidget(self.pushButton_KU13, 4, 2, 1, 1)
        self.Apply = QtWidgets.QPushButton(self.userFrame)
        self.Apply.setMinimumSize(QtCore.QSize(40, 20))
        self.Apply.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Apply.setObjectName("Apply")
        self.gridLayout_2.addWidget(self.Apply, 6, 3, 1, 1)
        self.gridLayout.addWidget(self.userFrame, 0, 1, 1, 1)
        self.coreGLayout = QtWidgets.QGridLayout()
        self.coreGLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.coreGLayout.setObjectName("coreGLayout")
        self.moduleSerialNumberLEdit = QtWidgets.QLineEdit(Form)
        self.moduleSerialNumberLEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moduleSerialNumberLEdit.sizePolicy().hasHeightForWidth())
        self.moduleSerialNumberLEdit.setSizePolicy(sizePolicy)
        self.moduleSerialNumberLEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.moduleSerialNumberLEdit.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.moduleSerialNumberLEdit.setText("")
        self.moduleSerialNumberLEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.moduleSerialNumberLEdit.setObjectName("moduleSerialNumberLEdit")
        self.coreGLayout.addWidget(self.moduleSerialNumberLEdit, 2, 1, 1, 1)
        self.statusLineEdit = QtWidgets.QLineEdit(Form)
        self.statusLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.statusLineEdit.setObjectName("statusLineEdit")
        self.coreGLayout.addWidget(self.statusLineEdit, 2, 0, 1, 1)
        self.connectionPButton = QtWidgets.QPushButton(Form)
        self.connectionPButton.setEnabled(True)
        self.connectionPButton.setMinimumSize(QtCore.QSize(150, 30))
        self.connectionPButton.setMaximumSize(QtCore.QSize(2000, 30))
        self.connectionPButton.setFlat(False)
        self.connectionPButton.setObjectName("connectionPButton")
        self.coreGLayout.addWidget(self.connectionPButton, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.coreGLayout, 10, 1, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_KU5.setText(_translate("Form", "КУ5"))
        self.pushButton_KU14.setText(_translate("Form", "КУ14"))
        self.pushButton_KU16.setText(_translate("Form", "КУ16"))
        self.spinBox.setToolTip(_translate("Form", "<html><head/><body><p>Настройка длительност сигнала (мс)</p></body></html>"))
        self.pushButton_KU2.setText(_translate("Form", "КУ2"))
        self.pushButton_KU7.setText(_translate("Form", "КУ7"))
        self.pushButton_KU1.setText(_translate("Form", "КУ1"))
        self.pushButton_KU6.setText(_translate("Form", "КУ6"))
        self.pushButton_KU12.setText(_translate("Form", "КУ12"))
        self.pushButton_KU15.setText(_translate("Form", "КУ15"))
        self.pushButton_KU10.setText(_translate("Form", "КУ10"))
        self.pushButton_KU11.setText(_translate("Form", "КУ11"))
        self.pushButton_KU3.setText(_translate("Form", "КУ3"))
        self.pushButton_KU8.setText(_translate("Form", "КУ8"))
        self.pushButton_KU4.setText(_translate("Form", "КУ4"))
        self.pushButton_KU9.setText(_translate("Form", "КУ9"))
        self.pushButton_KU13.setText(_translate("Form", "КУ13"))
        self.Apply.setToolTip(_translate("Form", "<html><head/><body><p>Применить настройки длительности сигнала</p></body></html>"))
        self.Apply.setText(_translate("Form", "Применить"))
        self.moduleSerialNumberLEdit.setPlaceholderText(_translate("Form", "Serial Number"))
        self.connectionPButton.setText(_translate("Form", "Подключение"))
