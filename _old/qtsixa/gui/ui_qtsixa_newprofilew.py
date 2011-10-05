# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/ui/qtsixa_newprofilew.ui'
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

class Ui_NewProfileW(object):
    def setupUi(self, NewProfileW):
        NewProfileW.setObjectName(_fromUtf8("NewProfileW"))
        NewProfileW.resize(686, 439)
        NewProfileW.setWindowTitle(QtGui.QApplication.translate("NewProfileW", "QtSixA - New Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5 = QtGui.QGridLayout(NewProfileW)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.dockWidget = QtGui.QDockWidget(NewProfileW)
        self.dockWidget.setMinimumSize(QtCore.QSize(500, 400))
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetClosable|QtGui.QDockWidget.DockWidgetFloatable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit.setReadOnly(True)
        self.textEdit.setHtml(QtGui.QApplication.translate("NewProfileW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>keylist.txt</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/*</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> * Keys and buttons</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> *</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> * Abbreviations in the comments:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> * AC - Application Control</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> * AL - Application Launch Button</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> * SC - System Control</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\"> */</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-style:italic; color:#787775; background-color:#201f1f;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-style:italic; color:#787775; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_ESC                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_1                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_2                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_3                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_4                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_5                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_6                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_7                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_8                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_9                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_0                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MINUS               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">12</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_EQUAL               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">13</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BACKSPACE           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">14</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_TAB                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">15</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_Q                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">16</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_W                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">17</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_E                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">18</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_R                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">19</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_T                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_Y                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">21</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_U                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">22</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_I                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">23</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_O                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">24</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_P                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">25</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LEFTBRACE           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">26</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RIGHTBRACE          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">27</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_ENTER               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">28</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LEFTCTRL            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">29</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_A                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">30</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_S                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">31</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_D                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">32</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">33</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_G                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">34</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_H                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">35</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_J                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">36</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_K                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">37</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_L                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">38</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SEMICOLON           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">39</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_APOSTROPHE          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">40</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_GRAVE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">41</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LEFTSHIFT           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">42</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BACKSLASH           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">43</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_Z                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">44</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_X                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">45</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_C                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">46</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_V                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">47</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_B                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">48</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_N                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">49</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_M                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">50</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_COMMA               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">51</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DOT                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">52</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SLASH               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">53</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RIGHTSHIFT          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">54</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPASTERISK          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LEFTALT             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">56</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SPACE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">57</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CAPSLOCK            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">58</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F1                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">59</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F2                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">60</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F3                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">61</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F4                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">62</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F5                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">63</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F6                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">64</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F7                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">65</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F8                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">66</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F9                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">67</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F10                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">68</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_NUMLOCK             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">69</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SCROLLLOCK          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">70</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP7                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">71</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP8                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">72</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP9                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">73</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPMINUS             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">74</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP4                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">75</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP5                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">76</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP6                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">77</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPPLUS              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">78</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP1                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">79</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP2                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">80</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP3                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">81</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KP0                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">82</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPDOT               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">83</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_ZENKAKUHANKAKU      </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">85</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_102ND               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">86</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F11                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">87</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F12                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">88</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RO                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">89</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KATAKANA            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">90</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HIRAGANA            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">91</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HENKAN              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">92</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KATAKANAHIRAGANA    </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">93</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MUHENKAN            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">94</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPJPCOMMA           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">95</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPENTER             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">96</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RIGHTCTRL           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">97</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPSLASH             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">98</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SYSRQ               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RIGHTALT            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">100</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LINEFEED            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">101</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HOME                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">102</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_UP                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">103</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PAGEUP              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">104</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LEFT                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">105</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RIGHT               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">106</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_END                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">107</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DOWN                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">108</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PAGEDOWN            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">109</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_INSERT              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">110</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DELETE              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MACRO               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">112</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MUTE                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">113</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_VOLUMEDOWN          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">114</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_VOLUMEUP            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">115</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_POWER               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">116</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* SC System Power Down */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPEQUAL             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">117</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPPLUSMINUS         </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">118</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PAUSE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">119</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SCALE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">120</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Compiz Scale (Expose) */</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-style:italic; color:#787775; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPCOMMA             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">121</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HANGEUL             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">122</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HANGUEL             KEY_HANGEUL</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HANJA               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">123</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_YEN                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">124</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_LEFTMETA            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">125</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RIGHTMETA           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">126</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_COMPOSE             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">127</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_STOP                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">128</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Stop */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_AGAIN               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">129</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PROPS               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">130</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Properties */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_UNDO                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">131</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Undo */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FRONT               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">132</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_COPY                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">133</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Copy */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_OPEN                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">134</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Open */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PASTE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">135</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Paste */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FIND                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">136</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Search */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CUT                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">137</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Cut */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HELP                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">138</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Integrated Help Center */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MENU                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">139</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* Menu (show menu) */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CALC                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">140</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Calculator */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SETUP               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">141</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SLEEP               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">142</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* SC System Sleep */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_WAKEUP              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">143</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* System Wake Up */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FILE                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">144</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Local Machine Browser */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SENDFILE            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">145</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DELETEFILE          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">146</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_XFER                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">147</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PROG1               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">148</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PROG2               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">149</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_WWW                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">150</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Internet Browser */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MSDOS               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">151</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_COFFEE              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">152</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Terminal Lock/Screensaver */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SCREENLOCK          KEY_COFFEE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DIRECTION           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">153</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CYCLEWINDOWS        </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">154</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MAIL                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">155</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BOOKMARKS           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">156</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Bookmarks */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_COMPUTER            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">157</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BACK                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">158</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Back */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FORWARD             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">159</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Forward */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CLOSECD             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">160</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_EJECTCD             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">161</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_EJECTCLOSECD        </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">162</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_NEXTSONG            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">163</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PLAYPAUSE           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">164</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PREVIOUSSONG        </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">165</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_STOPCD              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">166</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_RECORD              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">167</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_REWIND              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">168</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PHONE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">169</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* Media Select Telephone */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_ISO                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">170</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CONFIG              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">171</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Consumer Control Configuration */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HOMEPAGE            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">172</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Home */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_REFRESH             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">173</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Refresh */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_EXIT                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">174</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Exit */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MOVE                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">175</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_EDIT                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">176</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SCROLLUP            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">177</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SCROLLDOWN          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">178</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPLEFTPAREN         </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">179</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KPRIGHTPAREN        </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">180</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_NEW                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">181</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC New */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_REDO                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">182</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Redo/Repeat */</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-style:italic; color:#787775; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F13                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">183</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F14                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">184</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F15                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">185</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F16                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">186</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F17                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">187</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F18                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">188</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F19                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">189</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F20                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">190</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F21                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">191</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F22                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">192</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F23                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">193</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_F24                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">194</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PLAYCD              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">200</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PAUSECD             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">201</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PROG3               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">202</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PROG4               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">203</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DASHBOARD           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">204</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Dashboard */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SUSPEND             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">205</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CLOSE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">206</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Close */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PLAY                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">207</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FASTFORWARD         </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">208</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BASSBOOST           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">209</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_PRINT               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">210</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Print */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_HP                  </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">211</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CAMERA              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">212</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SOUND               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">213</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_QUESTION            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">214</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_EMAIL               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">215</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CHAT                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">216</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SEARCH              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">217</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CONNECT             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">218</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FINANCE             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">219</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AL Checkbook/Finance */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SPORT               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">220</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SHOP                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">221</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_ALTERASE            </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">222</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_CANCEL              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">223</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Cancel */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BRIGHTNESSDOWN      </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">224</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BRIGHTNESSUP        </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">225</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_MEDIA               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">226</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SWITCHVIDEOMODE     </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">227</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* Cycle between available video</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">                                   outputs (Monitor/LCD/TV-out/etc) */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KBDILLUMTOGGLE      </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">228</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KBDILLUMDOWN        </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">229</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_KBDILLUMUP          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">230</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SEND                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">231</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Send */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_REPLY               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">232</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Reply */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_FORWARDMAIL         </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">233</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Forward Msg */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_SAVE                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">234</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* AC Save */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DOCUMENTS           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">235</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BATTERY             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">236</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BLUETOOTH           </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">237</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_WLAN                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">238</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_UWB                 </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">239</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_UNKNOWN             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">240</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_VIDEO_NEXT          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">241</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* drive next video source */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_VIDEO_PREV          </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">242</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* drive previous video source */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BRIGHTNESS_CYCLE    </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">243</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* brightness up, after max is min */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_BRIGHTNESS_ZERO     </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">244</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* brightness off, use ambient */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">KEY_DISPLAY_OFF         </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">245</span><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">     </span><span style=\" font-family:\'Courier New,courier\'; font-style:italic; color:#787775;\">/* display device to off state */</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-style:italic; color:#787775; background-color:#201f1f;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-style:italic; color:#787775; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_MISC                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">256</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_0                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">256</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_1                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">257</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_2                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">258</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_3                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">259</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_4                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">260</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_5                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">261</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_6                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">262</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_7                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">263</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_8                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">264</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_9                   </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">265</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; color:#c0a25f; background-color:#201f1f;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_MOUSE               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">272</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_LEFT                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">272</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_RIGHT               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">273</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_MIDDLE              </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">274</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_SIDE                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">275</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_EXTRA               </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">276</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_FORWARD             </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">277</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_BACK                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">278</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; color:#d4d2cf;\">BTN_TASK                </span><span style=\" font-family:\'Courier New,courier\'; color:#c0a25f;\">279</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#201f1f;\"><span style=\" font-family:\'Courier New,courier\'; background-color:#201f1f;\"> </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_4.addWidget(self.textEdit)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.gridLayout_5.addWidget(self.dockWidget, 0, 0, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_app = QtGui.QLabel(NewProfileW)
        self.label_app.setText(QtGui.QApplication.translate("NewProfileW", "Application:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_app.setObjectName(_fromUtf8("label_app"))
        self.horizontalLayout.addWidget(self.label_app)
        self.line_app = QtGui.QLineEdit(NewProfileW)
        self.line_app.setText(_fromUtf8("(App Name)"))
        self.line_app.setObjectName(_fromUtf8("line_app"))
        self.horizontalLayout.addWidget(self.line_app)
        self.label_author = QtGui.QLabel(NewProfileW)
        self.label_author.setText(QtGui.QApplication.translate("NewProfileW", "Author:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_author.setObjectName(_fromUtf8("label_author"))
        self.horizontalLayout.addWidget(self.label_author)
        self.line_author = QtGui.QLineEdit(NewProfileW)
        self.line_author.setText(_fromUtf8("(Your Name)"))
        self.line_author.setObjectName(_fromUtf8("line_author"))
        self.horizontalLayout.addWidget(self.line_author)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.b_keys = QtGui.QPushButton(NewProfileW)
        self.b_keys.setText(QtGui.QApplication.translate("NewProfileW", "&View available keys", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/manual.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_keys.setIcon(icon)
        self.b_keys.setCheckable(True)
        self.b_keys.setObjectName(_fromUtf8("b_keys"))
        self.horizontalLayout_2.addWidget(self.b_keys)
        self.b_tips = QtGui.QPushButton(NewProfileW)
        self.b_tips.setEnabled(True)
        self.b_tips.setText(QtGui.QApplication.translate("NewProfileW", "&Tips && Tricks", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/hint.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_tips.setIcon(icon1)
        self.b_tips.setObjectName(_fromUtf8("b_tips"))
        self.horizontalLayout_2.addWidget(self.b_tips)
        spacerItem = QtGui.QSpacerItem(458, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.b_close = QtGui.QPushButton(NewProfileW)
        self.b_close.setText(QtGui.QApplication.translate("NewProfileW", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_close.setIcon(icon2)
        self.b_close.setObjectName(_fromUtf8("b_close"))
        self.horizontalLayout_2.addWidget(self.b_close)
        self.b_done = QtGui.QPushButton(NewProfileW)
        self.b_done.setText(QtGui.QApplication.translate("NewProfileW", "&Done!", None, QtGui.QApplication.UnicodeUTF8))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_done.setIcon(icon3)
        self.b_done.setObjectName(_fromUtf8("b_done"))
        self.horizontalLayout_2.addWidget(self.b_done)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.toolBox = QtGui.QToolBox(NewProfileW)
        self.toolBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.toolBox.setFrameShadow(QtGui.QFrame.Sunken)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 412, 297))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_l2 = QtGui.QLabel(self.page)
        self.label_l2.setText(_fromUtf8("L2"))
        self.label_l2.setObjectName(_fromUtf8("label_l2"))
        self.horizontalLayout_3.addWidget(self.label_l2)
        self.s_l2 = QtGui.QSpinBox(self.page)
        self.s_l2.setMaximum(279)
        self.s_l2.setObjectName(_fromUtf8("s_l2"))
        self.horizontalLayout_3.addWidget(self.s_l2)
        spacerItem2 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.s_r2 = QtGui.QSpinBox(self.page)
        self.s_r2.setMaximum(279)
        self.s_r2.setObjectName(_fromUtf8("s_r2"))
        self.horizontalLayout_3.addWidget(self.s_r2)
        self.label_r2 = QtGui.QLabel(self.page)
        self.label_r2.setText(QtGui.QApplication.translate("NewProfileW", "R2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_r2.setObjectName(_fromUtf8("label_r2"))
        self.horizontalLayout_3.addWidget(self.label_r2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_l1 = QtGui.QLabel(self.page)
        self.label_l1.setText(_fromUtf8("L1"))
        self.label_l1.setObjectName(_fromUtf8("label_l1"))
        self.horizontalLayout_4.addWidget(self.label_l1)
        self.s_l1 = QtGui.QSpinBox(self.page)
        self.s_l1.setMaximum(279)
        self.s_l1.setObjectName(_fromUtf8("s_l1"))
        self.horizontalLayout_4.addWidget(self.s_l1)
        spacerItem5 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.s_r1 = QtGui.QSpinBox(self.page)
        self.s_r1.setMaximum(279)
        self.s_r1.setObjectName(_fromUtf8("s_r1"))
        self.horizontalLayout_4.addWidget(self.s_r1)
        self.label_r1 = QtGui.QLabel(self.page)
        self.label_r1.setText(QtGui.QApplication.translate("NewProfileW", "R1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_r1.setObjectName(_fromUtf8("label_r1"))
        self.horizontalLayout_4.addWidget(self.label_r1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.label_select = QtGui.QLabel(self.page)
        self.label_select.setText(_fromUtf8("Select"))
        self.label_select.setObjectName(_fromUtf8("label_select"))
        self.horizontalLayout_5.addWidget(self.label_select)
        self.s_select = QtGui.QSpinBox(self.page)
        self.s_select.setMaximum(279)
        self.s_select.setObjectName(_fromUtf8("s_select"))
        self.horizontalLayout_5.addWidget(self.s_select)
        self.line_2 = QtGui.QFrame(self.page)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_5.addWidget(self.line_2)
        self.s_start = QtGui.QSpinBox(self.page)
        self.s_start.setMaximum(279)
        self.s_start.setObjectName(_fromUtf8("s_start"))
        self.horizontalLayout_5.addWidget(self.s_start)
        self.label_start = QtGui.QLabel(self.page)
        self.label_start.setText(_fromUtf8("Start"))
        self.label_start.setObjectName(_fromUtf8("label_start"))
        self.horizontalLayout_5.addWidget(self.label_start)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem10)
        self.s_ps = QtGui.QSpinBox(self.page)
        self.s_ps.setMaximum(279)
        self.s_ps.setObjectName(_fromUtf8("s_ps"))
        self.horizontalLayout_25.addWidget(self.s_ps)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_24.addItem(spacerItem12)
        self.label_ps = QtGui.QLabel(self.page)
        self.label_ps.setText(_fromUtf8("PS"))
        self.label_ps.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_ps.setObjectName(_fromUtf8("label_ps"))
        self.horizontalLayout_24.addWidget(self.label_ps)
        spacerItem13 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_24.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.label_up = QtGui.QLabel(self.page)
        self.label_up.setText(QtGui.QApplication.translate("NewProfileW", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.label_up.setObjectName(_fromUtf8("label_up"))
        self.horizontalLayout_6.addWidget(self.label_up)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.s_up = QtGui.QSpinBox(self.page)
        self.s_up.setMaximum(279)
        self.s_up.setObjectName(_fromUtf8("s_up"))
        self.horizontalLayout_7.addWidget(self.s_up)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_left = QtGui.QLabel(self.page)
        self.label_left.setText(QtGui.QApplication.translate("NewProfileW", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.label_left.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_left.setObjectName(_fromUtf8("label_left"))
        self.horizontalLayout_8.addWidget(self.label_left)
        self.s_left = QtGui.QSpinBox(self.page)
        self.s_left.setMaximum(279)
        self.s_left.setObjectName(_fromUtf8("s_left"))
        self.horizontalLayout_8.addWidget(self.s_left)
        self.line = QtGui.QFrame(self.page)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_8.addWidget(self.line)
        self.s_right = QtGui.QSpinBox(self.page)
        self.s_right.setMaximum(279)
        self.s_right.setObjectName(_fromUtf8("s_right"))
        self.horizontalLayout_8.addWidget(self.s_right)
        self.label_right = QtGui.QLabel(self.page)
        self.label_right.setText(QtGui.QApplication.translate("NewProfileW", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.label_right.setObjectName(_fromUtf8("label_right"))
        self.horizontalLayout_8.addWidget(self.label_right)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.s_down = QtGui.QSpinBox(self.page)
        self.s_down.setMaximum(279)
        self.s_down.setObjectName(_fromUtf8("s_down"))
        self.horizontalLayout_9.addWidget(self.s_down)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem21)
        self.label_down = QtGui.QLabel(self.page)
        self.label_down.setText(QtGui.QApplication.translate("NewProfileW", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.label_down.setObjectName(_fromUtf8("label_down"))
        self.horizontalLayout_10.addWidget(self.label_down)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem22)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16.addLayout(self.verticalLayout_2)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem23)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem24)
        self.label_triangle = QtGui.QLabel(self.page)
        self.label_triangle.setText(QtGui.QApplication.translate("NewProfileW", "Triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_triangle.setObjectName(_fromUtf8("label_triangle"))
        self.horizontalLayout_11.addWidget(self.label_triangle)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem25)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem26)
        self.s_triangle = QtGui.QSpinBox(self.page)
        self.s_triangle.setMaximum(279)
        self.s_triangle.setObjectName(_fromUtf8("s_triangle"))
        self.horizontalLayout_12.addWidget(self.s_triangle)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem27)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_square = QtGui.QLabel(self.page)
        self.label_square.setText(QtGui.QApplication.translate("NewProfileW", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.label_square.setObjectName(_fromUtf8("label_square"))
        self.horizontalLayout_13.addWidget(self.label_square)
        self.s_square = QtGui.QSpinBox(self.page)
        self.s_square.setMaximum(279)
        self.s_square.setObjectName(_fromUtf8("s_square"))
        self.horizontalLayout_13.addWidget(self.s_square)
        self.line_3 = QtGui.QFrame(self.page)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_13.addWidget(self.line_3)
        self.s_circle = QtGui.QSpinBox(self.page)
        self.s_circle.setMaximum(279)
        self.s_circle.setObjectName(_fromUtf8("s_circle"))
        self.horizontalLayout_13.addWidget(self.s_circle)
        self.label_circle = QtGui.QLabel(self.page)
        self.label_circle.setText(QtGui.QApplication.translate("NewProfileW", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_circle.setObjectName(_fromUtf8("label_circle"))
        self.horizontalLayout_13.addWidget(self.label_circle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem28 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem28)
        self.s_cross = QtGui.QSpinBox(self.page)
        self.s_cross.setMaximum(279)
        self.s_cross.setObjectName(_fromUtf8("s_cross"))
        self.horizontalLayout_14.addWidget(self.s_cross)
        spacerItem29 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem29)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem30 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem30)
        self.label_cross = QtGui.QLabel(self.page)
        self.label_cross.setText(QtGui.QApplication.translate("NewProfileW", "Cross", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cross.setObjectName(_fromUtf8("label_cross"))
        self.horizontalLayout_15.addWidget(self.label_cross)
        spacerItem31 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem31)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16.addLayout(self.verticalLayout_3)
        spacerItem32 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem32)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        spacerItem33 = QtGui.QSpacerItem(20, 26, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem33)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(-223, 0, 490, 293))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem34 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem34)
        self.label = QtGui.QLabel(self.page_2)
        self.label.setText(QtGui.QApplication.translate("NewProfileW", "Axis Speed Multiplier:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_23.addWidget(self.label)
        self.s_speed = QtGui.QSpinBox(self.page_2)
        self.s_speed.setSuffix(QtGui.QApplication.translate("NewProfileW", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.s_speed.setMinimum(1)
        self.s_speed.setMaximum(9)
        self.s_speed.setProperty("value", 6)
        self.s_speed.setObjectName(_fromUtf8("s_speed"))
        self.horizontalLayout_23.addWidget(self.s_speed)
        spacerItem35 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem35)
        self.gridLayout_6.addLayout(self.horizontalLayout_23, 0, 0, 1, 3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        spacerItem36 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem36)
        self.label_combo_left = QtGui.QLabel(self.page_2)
        self.label_combo_left.setText(QtGui.QApplication.translate("NewProfileW", "Use Left Axis As:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_combo_left.setObjectName(_fromUtf8("label_combo_left"))
        self.horizontalLayout_19.addWidget(self.label_combo_left)
        self.combo_left = QtGui.QComboBox(self.page_2)
        self.combo_left.setObjectName(_fromUtf8("combo_left"))
        self.combo_left.addItem(_fromUtf8(""))
        self.combo_left.setItemText(0, QtGui.QApplication.translate("NewProfileW", "Mouse", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_left.addItem(_fromUtf8(""))
        self.combo_left.setItemText(1, QtGui.QApplication.translate("NewProfileW", "Scroll", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_left.addItem(_fromUtf8(""))
        self.combo_left.setItemText(2, QtGui.QApplication.translate("NewProfileW", "Custom Buttons", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_left.addItem(_fromUtf8(""))
        self.combo_left.setItemText(3, QtGui.QApplication.translate("NewProfileW", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_19.addWidget(self.combo_left)
        spacerItem37 = QtGui.QSpacerItem(126, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem37)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.group_left_h = QtGui.QGroupBox(self.page_2)
        self.group_left_h.setTitle(QtGui.QApplication.translate("NewProfileW", "Left Axis (Horizontal)", None, QtGui.QApplication.UnicodeUTF8))
        self.group_left_h.setObjectName(_fromUtf8("group_left_h"))
        self.gridLayout = QtGui.QGridLayout(self.group_left_h)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_4 = QtGui.QLabel(self.group_left_h)
        self.label_4.setText(QtGui.QApplication.translate("NewProfileW", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_17.addWidget(self.label_4)
        self.s_left_left = QtGui.QSpinBox(self.group_left_h)
        self.s_left_left.setMaximum(279)
        self.s_left_left.setObjectName(_fromUtf8("s_left_left"))
        self.horizontalLayout_17.addWidget(self.s_left_left)
        self.line_5 = QtGui.QFrame(self.group_left_h)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_17.addWidget(self.line_5)
        self.s_left_right = QtGui.QSpinBox(self.group_left_h)
        self.s_left_right.setMaximum(279)
        self.s_left_right.setObjectName(_fromUtf8("s_left_right"))
        self.horizontalLayout_17.addWidget(self.s_left_right)
        self.label_5 = QtGui.QLabel(self.group_left_h)
        self.label_5.setText(QtGui.QApplication.translate("NewProfileW", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_17.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.group_left_h)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem38 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem38)
        self.group_left_v = QtGui.QGroupBox(self.page_2)
        self.group_left_v.setTitle(QtGui.QApplication.translate("NewProfileW", "Left Axis (Vertical)", None, QtGui.QApplication.UnicodeUTF8))
        self.group_left_v.setObjectName(_fromUtf8("group_left_v"))
        self.gridLayout_2 = QtGui.QGridLayout(self.group_left_v)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_2 = QtGui.QLabel(self.group_left_v)
        self.label_2.setText(QtGui.QApplication.translate("NewProfileW", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.s_left_up = QtGui.QSpinBox(self.group_left_v)
        self.s_left_up.setMaximum(279)
        self.s_left_up.setObjectName(_fromUtf8("s_left_up"))
        self.verticalLayout_6.addWidget(self.s_left_up)
        self.line_4 = QtGui.QFrame(self.group_left_v)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_6.addWidget(self.line_4)
        self.s_left_down = QtGui.QSpinBox(self.group_left_v)
        self.s_left_down.setMaximum(279)
        self.s_left_down.setObjectName(_fromUtf8("s_left_down"))
        self.verticalLayout_6.addWidget(self.s_left_down)
        self.label_3 = QtGui.QLabel(self.group_left_v)
        self.label_3.setText(QtGui.QApplication.translate("NewProfileW", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_6.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.group_left_v)
        spacerItem39 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem39)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.line_8 = QtGui.QFrame(self.page_2)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_6.addWidget(self.line_8, 1, 1, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        spacerItem40 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem40)
        self.label_combo_right = QtGui.QLabel(self.page_2)
        self.label_combo_right.setText(QtGui.QApplication.translate("NewProfileW", "Use Right Axis As:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_combo_right.setObjectName(_fromUtf8("label_combo_right"))
        self.horizontalLayout_22.addWidget(self.label_combo_right)
        self.combo_right = QtGui.QComboBox(self.page_2)
        self.combo_right.setObjectName(_fromUtf8("combo_right"))
        self.combo_right.addItem(_fromUtf8(""))
        self.combo_right.setItemText(0, QtGui.QApplication.translate("NewProfileW", "Mouse", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_right.addItem(_fromUtf8(""))
        self.combo_right.setItemText(1, QtGui.QApplication.translate("NewProfileW", "Scroll", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_right.addItem(_fromUtf8(""))
        self.combo_right.setItemText(2, QtGui.QApplication.translate("NewProfileW", "Custom Buttons", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_right.addItem(_fromUtf8(""))
        self.combo_right.setItemText(3, QtGui.QApplication.translate("NewProfileW", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_22.addWidget(self.combo_right)
        spacerItem41 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem41)
        self.verticalLayout_8.addLayout(self.horizontalLayout_22)
        self.group_right_h = QtGui.QGroupBox(self.page_2)
        self.group_right_h.setTitle(QtGui.QApplication.translate("NewProfileW", "Right Axis (Horizontal)", None, QtGui.QApplication.UnicodeUTF8))
        self.group_right_h.setObjectName(_fromUtf8("group_right_h"))
        self.gridLayout_3 = QtGui.QGridLayout(self.group_right_h)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_6 = QtGui.QLabel(self.group_right_h)
        self.label_6.setText(QtGui.QApplication.translate("NewProfileW", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_18.addWidget(self.label_6)
        self.s_right_left = QtGui.QSpinBox(self.group_right_h)
        self.s_right_left.setMaximum(279)
        self.s_right_left.setObjectName(_fromUtf8("s_right_left"))
        self.horizontalLayout_18.addWidget(self.s_right_left)
        self.line_6 = QtGui.QFrame(self.group_right_h)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_18.addWidget(self.line_6)
        self.s_right_right = QtGui.QSpinBox(self.group_right_h)
        self.s_right_right.setMaximum(279)
        self.s_right_right.setObjectName(_fromUtf8("s_right_right"))
        self.horizontalLayout_18.addWidget(self.s_right_right)
        self.label_7 = QtGui.QLabel(self.group_right_h)
        self.label_7.setText(QtGui.QApplication.translate("NewProfileW", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_18.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.group_right_h)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        spacerItem42 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem42)
        self.group_right_v = QtGui.QGroupBox(self.page_2)
        self.group_right_v.setTitle(QtGui.QApplication.translate("NewProfileW", "Right Axis (Vertical)", None, QtGui.QApplication.UnicodeUTF8))
        self.group_right_v.setObjectName(_fromUtf8("group_right_v"))
        self.gridLayout_4 = QtGui.QGridLayout(self.group_right_v)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_8 = QtGui.QLabel(self.group_right_v)
        self.label_8.setText(QtGui.QApplication.translate("NewProfileW", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_7.addWidget(self.label_8)
        self.s_right_up = QtGui.QSpinBox(self.group_right_v)
        self.s_right_up.setMaximum(279)
        self.s_right_up.setObjectName(_fromUtf8("s_right_up"))
        self.verticalLayout_7.addWidget(self.s_right_up)
        self.line_7 = QtGui.QFrame(self.group_right_v)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_7.addWidget(self.line_7)
        self.s_right_down = QtGui.QSpinBox(self.group_right_v)
        self.s_right_down.setMaximum(279)
        self.s_right_down.setObjectName(_fromUtf8("s_right_down"))
        self.verticalLayout_7.addWidget(self.s_right_down)
        self.label_9 = QtGui.QLabel(self.group_right_v)
        self.label_9.setText(QtGui.QApplication.translate("NewProfileW", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_20.addWidget(self.group_right_v)
        spacerItem43 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem43)
        self.verticalLayout_8.addLayout(self.horizontalLayout_20)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 1, 2, 1, 1)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.toolBox, 1, 1, 1, 1)
        self.label_app.setBuddy(self.line_app)
        self.label_author.setBuddy(self.line_author)
        self.label_combo_left.setBuddy(self.combo_left)
        self.label_combo_right.setBuddy(self.combo_right)

        self.retranslateUi(NewProfileW)
        self.toolBox.setCurrentIndex(0)
        self.combo_left.setCurrentIndex(3)
        self.combo_right.setCurrentIndex(3)
        QtCore.QObject.connect(self.b_close, QtCore.SIGNAL(_fromUtf8("clicked()")), NewProfileW.reject)
        QtCore.QObject.connect(self.b_keys, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dockWidget.setVisible)
        QtCore.QObject.connect(self.dockWidget, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.b_keys.setChecked)
        QtCore.QMetaObject.connectSlotsByName(NewProfileW)

    def retranslateUi(self, NewProfileW):
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("NewProfileW", "Buttons", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("NewProfileW", "Axis", None, QtGui.QApplication.UnicodeUTF8))

import qtsixa_rc
