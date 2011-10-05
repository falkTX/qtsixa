# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/ui/qtsixa_preferencesw.ui'
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

class Ui_PreferencesW(object):
    def setupUi(self, PreferencesW):
        PreferencesW.setObjectName(_fromUtf8("PreferencesW"))
        PreferencesW.setEnabled(True)
        PreferencesW.resize(336, 287)
        PreferencesW.setWindowTitle(QtGui.QApplication.translate("PreferencesW", "QtSixA - Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_7 = QtGui.QVBoxLayout(PreferencesW)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.prefTab = QtGui.QTabWidget(PreferencesW)
        self.prefTab.setTabPosition(QtGui.QTabWidget.South)
        self.prefTab.setObjectName(_fromUtf8("prefTab"))
        self.main = QtGui.QWidget()
        self.main.setObjectName(_fromUtf8("main"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.main)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.groupBox_startup = QtGui.QGroupBox(self.main)
        self.groupBox_startup.setTitle(QtGui.QApplication.translate("PreferencesW", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_startup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_startup.setObjectName(_fromUtf8("groupBox_startup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_startup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.box_startup = QtGui.QCheckBox(self.groupBox_startup)
        self.box_startup.setEnabled(True)
        self.box_startup.setText(QtGui.QApplication.translate("PreferencesW", "Start QtSixA at startup", None, QtGui.QApplication.UnicodeUTF8))
        self.box_startup.setCheckable(True)
        self.box_startup.setChecked(False)
        self.box_startup.setObjectName(_fromUtf8("box_startup"))
        self.verticalLayout.addWidget(self.box_startup)
        self.box_warn = QtGui.QCheckBox(self.groupBox_startup)
        self.box_warn.setText(QtGui.QApplication.translate("PreferencesW", "Show useful warnings when appropriate", None, QtGui.QApplication.UnicodeUTF8))
        self.box_warn.setObjectName(_fromUtf8("box_warn"))
        self.verticalLayout.addWidget(self.box_warn)
        self.box_1inst = QtGui.QCheckBox(self.groupBox_startup)
        self.box_1inst.setText(QtGui.QApplication.translate("PreferencesW", "Allow only one instance", None, QtGui.QApplication.UnicodeUTF8))
        self.box_1inst.setObjectName(_fromUtf8("box_1inst"))
        self.verticalLayout.addWidget(self.box_1inst)
        self.verticalLayout_11.addWidget(self.groupBox_startup)
        self.groupBox_systray = QtGui.QGroupBox(self.main)
        self.groupBox_systray.setTitle(QtGui.QApplication.translate("PreferencesW", "Systray", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_systray.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_systray.setObjectName(_fromUtf8("groupBox_systray"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_systray)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.box_systray = QtGui.QCheckBox(self.groupBox_systray)
        self.box_systray.setText(QtGui.QApplication.translate("PreferencesW", "Show QtSixA on systray", None, QtGui.QApplication.UnicodeUTF8))
        self.box_systray.setObjectName(_fromUtf8("box_systray"))
        self.verticalLayout_3.addWidget(self.box_systray)
        self.box_min = QtGui.QCheckBox(self.groupBox_systray)
        self.box_min.setEnabled(False)
        self.box_min.setText(QtGui.QApplication.translate("PreferencesW", "Start QtSixA minimized (requires systray)", None, QtGui.QApplication.UnicodeUTF8))
        self.box_min.setObjectName(_fromUtf8("box_min"))
        self.verticalLayout_3.addWidget(self.box_min)
        self.box_close = QtGui.QCheckBox(self.groupBox_systray)
        self.box_close.setEnabled(False)
        self.box_close.setText(QtGui.QApplication.translate("PreferencesW", "Minimize to systray on close (requires systray)", None, QtGui.QApplication.UnicodeUTF8))
        self.box_close.setObjectName(_fromUtf8("box_close"))
        self.verticalLayout_3.addWidget(self.box_close)
        self.verticalLayout_11.addWidget(self.groupBox_systray)
        self.prefTab.addTab(self.main, _fromUtf8(""))
        self.notify = QtGui.QWidget()
        self.notify.setObjectName(_fromUtf8("notify"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.notify)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.groupNotify = QtGui.QGroupBox(self.notify)
        self.groupNotify.setTitle(QtGui.QApplication.translate("PreferencesW", "Notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.groupNotify.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupNotify.setObjectName(_fromUtf8("groupNotify"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupNotify)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.box_notify = QtGui.QCheckBox(self.groupNotify)
        self.box_notify.setStatusTip(QtGui.QApplication.translate("PreferencesW", "Very nice with Notify-OSD or KDE 4.3", None, QtGui.QApplication.UnicodeUTF8))
        self.box_notify.setText(QtGui.QApplication.translate("PreferencesW", "Enable notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.box_notify.setObjectName(_fromUtf8("box_notify"))
        self.verticalLayout_9.addWidget(self.box_notify)
        self.box_notify_start = QtGui.QCheckBox(self.groupNotify)
        self.box_notify_start.setEnabled(False)
        self.box_notify_start.setStatusTip(QtGui.QApplication.translate("PreferencesW", "Auto-srats every time you login", None, QtGui.QApplication.UnicodeUTF8))
        self.box_notify_start.setText(QtGui.QApplication.translate("PreferencesW", "Run at session startup", None, QtGui.QApplication.UnicodeUTF8))
        self.box_notify_start.setObjectName(_fromUtf8("box_notify_start"))
        self.verticalLayout_9.addWidget(self.box_notify_start)
        self.verticalLayout_10.addWidget(self.groupNotify)
        self.groupNFor = QtGui.QGroupBox(self.notify)
        self.groupNFor.setEnabled(True)
        self.groupNFor.setTitle(QtGui.QApplication.translate("PreferencesW", "Show notifications for:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupNFor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupNFor.setObjectName(_fromUtf8("groupNFor"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupNFor)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label = QtGui.QLabel(self.groupNFor)
        self.label.setText(QtGui.QApplication.translate("PreferencesW", "- Sixaxis/DualShock3<br>\n"
"- PS3 Keypads<br>\n"
"- PS3 Remotes<br>\n"
"- Sixaxis imitations<br>\n"
"- Keypad imitations<br>\n"
"- Bluetooth dongles<br>\n"
"- Other joysticks", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.verticalLayout_10.addWidget(self.groupNFor)
        self.prefTab.addTab(self.notify, _fromUtf8(""))
        self.verticalLayout_7.addWidget(self.prefTab)
        self.line = QtGui.QFrame(PreferencesW)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_7.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(PreferencesW)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_7.addWidget(self.buttonBox)

        self.retranslateUi(PreferencesW)
        self.prefTab.setCurrentIndex(0)
        QtCore.QObject.connect(self.box_notify, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.box_notify_start.setEnabled)
        QtCore.QObject.connect(self.box_systray, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.box_min.setEnabled)
        QtCore.QObject.connect(self.box_systray, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.box_close.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PreferencesW.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PreferencesW.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesW)

    def retranslateUi(self, PreferencesW):
        self.prefTab.setTabText(self.prefTab.indexOf(self.main), QtGui.QApplication.translate("PreferencesW", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.prefTab.setTabText(self.prefTab.indexOf(self.notify), QtGui.QApplication.translate("PreferencesW", "Notify", None, QtGui.QApplication.UnicodeUTF8))

