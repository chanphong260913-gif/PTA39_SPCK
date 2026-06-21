from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re

# mock data
account = {"fullname": "", "email": "", "password": ""}


class RegisterPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()  # ke thua cac code init cua lop cha
        self.main_window = main_window  # luu tham so
        self.root_dir = root_dir

        # load file ui
        ui_path = self.root_dir + "/ui/register.ui"
        uic.loadUi(ui_path, self)

        # bat su kien cho cac nut bam

        # 2. nut chuyen register
        self.dangnhap.clicked.connect(
            self.goto_login
        )  # click vao nut chuyen register -> goi ham goto_login

        # chay app
        self.show()

    # ------------------ xu ly su kien ------------------

    def goto_login(self):
        from pages.login import LoginPage

        self.login_page = LoginPage(
            main_window=self.main_window, root_dir=self.root_dir
        )
        self.close()  # ✅ đóng cửa sổ

    # ------------------- ham ho tro (private) ---------------------

