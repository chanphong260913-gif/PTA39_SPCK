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
        self.reset_nav()
        self.home.setProperty("class", "active")
        self.stackedWidget.setCurrentWidget(self.home_page)

    def goto_linh_kien(self):
        self.reset_nav()
        self.linh_kien.setProperty("class", "active")
        self.stackedWidget.setCurrentWidget(self.linh_kien_page)

    def goto_pc(self):
        self.reset_nav()
        self.pc.setProperty("class", "active")
        self.stackedWidget.setCurrentWidget(self.pc_page)

    def goto_sap_co(self):
        self.reset_nav()
        self.sap_co.setProperty("class", "active")
        self.stackedWidget.setCurrentWidget(self.sap_co_page)

    def goto_account(self):
        self.reset_nav()
        self.account.setProperty("class", "active")
        self.stackedWidget.setCurrentWidget(self.account_page)

    # ------------------ ham ho tro ------------------
    def reset_nav(self):
        self.home.setProperty("class", "")
        self.linh_kien.setProperty("class", "")
        self.pc.setProperty("class", "")
        self.sap_co.setProperty("class", "")
        self.account.setProperty("class", "")
