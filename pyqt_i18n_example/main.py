#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

class Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.generate_ui()
        self.button.clicked.connect(self.show_text)
        self.show()

    def generate_ui(self):
        self.button = QtGui.QPushButton(self.tr("Click me!"), self)
        self.label = QtGui.QLabel("",self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

    def show_text(self):
        self.label.setText(self.tr("Hello World!"))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load('de.qm')
    app.installTranslator(translator)
    widget = Widget()
    sys.exit(app.exec_())

