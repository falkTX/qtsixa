#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Imports
import os, sys
from commands import getoutput
from PyQt4.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt4.QtGui import QApplication, QMessageBox

import shared, qtsixa_main, qtsixa_manage


#--------------- main ------------------
if __name__ == '__main__':

  #For easy debugging, print version information to terminal
  print "Qt version:", QT_VERSION_STR
  print "PyQt version:", PYQT_VERSION_STR
  print "QtSixA version: 1.5.0"

  #Check for root tool
  shared.ROOT = getoutput("qtsixa "+"--get-root")
  print "Will use '"+shared.ROOT.split()[0]+"' for root actions"

  shared.init_config(None)
  shared.editProfile = ""

  shared.app = QApplication(sys.argv)
  if (shared.Globals.close_to_tray): shared.app.setQuitOnLastWindowClosed(False)
  gui = qtsixa_main.MainW()
  #gui = qtsixa_manage.ManageW()
  if (not "sixad" in getoutput("groups").split()):
    ask = QMessageBox.question(None, shared.app.translate("Init.Warn", "QtSixA - Question"), shared.app.translate("Init.Warn", ""
    "In order to use QtSixA you moust be in the sixad group.\n\nDo you want do do this now?"),
          QMessageBox.Yes | QMessageBox.No)
    if (ask == QMessageBox.Yes):
      #if look4Root(None):
        user = getoutput("whoami")
        os.system(shared.ROOT+" addgroup "+user+" sixad")
        QMessageBox.information(None, shared.app.translate("Init.Warn", "QtSixA - Information"), shared.app.translate("Init.Warn", "Please logoff and login again to make it work"))
  if (shared.Globals.start_minimized and shared.Globals.systray_enabled):
      gui.hide()
  else:
      gui.show()
  gui.show()
  shared.app.exec_()

