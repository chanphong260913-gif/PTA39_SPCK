from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re

# mock data
account = {"email": "admin@gmail.com", "password": "123456"}


class LoginPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()  # ke thua cac code init cua lop cha
        self.main_window = main_window  # luu tham so
        self.root_dir = root_dir

        # load file ui
        ui_path = self.root_dir + "/ui/Login2.ui"
        uic.loadUi(ui_path, self)

        # bat su kien cho cac nut bam
        self.dangki.clicked.connect(self.goto_register)
        self.login.clicked.connect(self.handle_login)

        # chay app
        self.show()

    # ------------------ xu ly su kien ------------------
    #1. nut login
    def handle_login(self):
        email_input = (
            self.email.text().strip()
        )  # lay du lieu tu email input, xoa khoang trang 2 dau
        password_input = self.password.text()

        # validate du lieu
        if self.__validate_input(email_input, password_input) is not None:
            print(self.__validate_input(email_input, password_input))
            return  # khong lam gi nua
        else:
            # kiem tra tai khoan
            if (
                email_input == account["email"]
                and password_input == account["password"]
            ):
                # thanh cong -> chuyen sang home
                from pages.home import HomePage

                self.home_page = HomePage(
                    main_window=self.main_window, root_dir=self.root_dir
                )
                self.close()  # ✅ đóng cửa sổ
            else:
                self.__show_message("Email hoặc mật khẩu không đúng!")
    #2. nut chuyen register
    def goto_register(self):
        from pages.register import RegisterPage

        self.register_page = RegisterPage(main_window=self.main_window, root_dir=self.root_dir)
        self.register_page.show()
        self.close()
    # ------------------ ham ho tro ------------------
    def __show_message(self, message):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(
            QMessageBox.Icon.Information
        )  # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Nút bấm OK
        # Hiển thị hộp thoại
        msg.exec()