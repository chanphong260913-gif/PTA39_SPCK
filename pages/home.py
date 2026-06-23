from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re


class HomePage(QMainWindow):
    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        # load file ui
        ui_path = self.root_dir + "/ui/home.ui"
        uic.loadUi(ui_path, self)

        # mac dinh moi vao -> home
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.home.setProperty("class", "active")
        
        # bat su kien cho cac nut nav
        self.home.clicked.connect(self.goto_home)
        self.linh_kien.clicked.connect(self.goto_linh_kien)
        self.pc.clicked.connect(self.goto_pc)
        self.sap_co.clicked.connect(self.goto_sap_co)
        self.account.clicked.connect(self.goto_account)

        # hien thi giao dien
        self.show()

    # ------------------ xu ly su kien ------------------
    # TODO: chuyen den page (stacked widget trong home)
    def goto_home(self):
        self.set_active(self.home)
        self.stackedWidget.setCurrentWidget(self.home_page)

    def goto_linh_kien(self):
        self.set_active(self.linh_kien)
        self.stackedWidget.setCurrentWidget(self.linh_kien_page)

    def goto_pc(self):
        self.set_active(self.pc)
        self.stackedWidget.setCurrentWidget(self.pc_page)

    def goto_sap_co(self):
        self.set_active(self.sap_co)
        self.stackedWidget.setCurrentWidget(self.sap_co_page)

    def goto_account(self):
        self.set_active(self.account)
        self.stackedWidget.setCurrentWidget(self.account_page)

    # ------------------ ham ho tro ------------------
    def set_active(self, btn):
        buttons = [
            self.home,
            self.linh_kien,
            self.pc,
            self.sap_co,
            self.account
        ]

        for b in buttons:
            b.setProperty("class", "")

        btn.setProperty("class", "active")

        # refresh style
        for b in buttons:
            b.style().unpolish(b)
            b.style().polish(b)
            b.update()
