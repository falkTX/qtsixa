# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/ui/qtsixa_referencew.ui'
#
# Created: Sat Sep 17 22:26:11 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ReferenceW(object):
    def setupUi(self, ReferenceW):
        ReferenceW.setObjectName(_fromUtf8("ReferenceW"))
        ReferenceW.resize(351, 430)
        ReferenceW.setWindowTitle(QtGui.QApplication.translate("ReferenceW", "QtSixA - Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ReferenceW)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(ReferenceW)
        self.textBrowser.setHtml(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Sixaxis/DualShock3 input events reference</span><br />------------------------------------------------------------<br /><span style=\" font-weight:600;\">Buttons:</span><br />0. Select<br />1. L3<br />2. R3<br />3. Start<br />4. Up<br />5. Right<br />6. Down<br />7. Left<br />8. L2<br />9. R2<br />10. L1<br />11. R1<br />12. Triangle<br />13. Circle<br />14. Cross<br />15. Square<br />16. PS<br /><br /><span style=\" font-weight:600;\">Axis:</span><br />0. Left Axis X (Horizontal)<br />1. Left Axis Y (Vertical)<br />2. Right Axis X (Horizontal)<br />3. Right Axis Y (Vertical)<br />4. Accelerometer X (roll)<br />5. Accelerometer Y (pitch)<br />6. Accelerometer Z (gravity)<br />7. Gyro/Yaw (not working yet)<br />8. Up<br />9. Right<br />10. Down<br />11. Left<br />12. L2<br />13. R2<br />14. L1<br />15. R1<br />16. Triangle<br />17. Circle<br />18. Cross<br />19. Square<br />20. Acceleration X<br />21. Acceleration Y<br />22. Acceleration Z<br />23. Speed X<br />24. Speed Y<br />25. Speed Z<br />26. Position X<br />27. Position Y<br />28. Position Z<br /><br /><br /><span style=\" font-weight:600; font-style:italic;\">Note:</span><span style=\" font-style:italic;\"><br />Some games will increase these values by 1 value,<br />starting at 1 instead of 0;</span></p></body></html>"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtGui.QDialogButtonBox(ReferenceW)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ReferenceW)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReferenceW.accept)
        QtCore.QMetaObject.connectSlotsByName(ReferenceW)

    def retranslateUi(self, ReferenceW):
        pass

