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
        self.productlist.setCurrentWidget(self.cpu1)
        self.cpu.setProperty("class", "active")
        # bat su kien cho cac nut nav
        self.home.clicked.connect(self.goto_home)
        self.linh_kien.clicked.connect(self.goto_linh_kien)
        self.pc.clicked.connect(self.goto_pc)
        self.sap_co.clicked.connect(self.goto_sap_co)
        self.account.clicked.connect(self.goto_account)

        self.cpu.clicked.connect(self.goto_cpu)
        self.gpu.clicked.connect(self.goto_gpu)
        self.mainboard.clicked.connect(self.goto_mainboard)
        self.ram.clicked.connect(self.goto_ram)
        self.ssd.clicked.connect(self.goto_ssd)
        self.psu.clicked.connect(self.goto_psu)
        self.case_2.clicked.connect(self.goto_case)
        self.casefan.clicked.connect(self.goto_casefan)

        # bat su kien cho cac nut phan trang
        self.setup_paging_buttons()

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
    
    def goto_cpu(self):
        self.set_active(self.cpu)
        self.productlist.setCurrentWidget(self.cpu1)

    def goto_gpu(self):
        self.set_active(self.gpu)
        self.productlist.setCurrentWidget(self.gpu1)

    def goto_mainboard(self):
        self.set_active(self.mainboard)
        self.productlist.setCurrentWidget(self.mainboard1)

    def goto_ram(self):
        self.set_active(self.ram)
        self.productlist.setCurrentWidget(self.ram1)

    def goto_ssd(self):
        self.set_active(self.ssd)
        self.productlist.setCurrentWidget(self.ssd1)

    def goto_psu(self):
        self.set_active(self.psu)
        self.productlist.setCurrentWidget(self.psu1)

    def goto_case(self):
        self.set_active(self.case_2)
        self.productlist.setCurrentWidget(self.case1)

    def goto_casefan(self):
        self.set_active(self.casefan)
        self.productlist.setCurrentWidget(self.casefan1)   

    def setup_paging_buttons(self):
        """
        Tu dong bat cac nut co ten:
        cpu1to2
        cpu2to1
        gpu1to2
        mainboard1to2
        ...
        """

        pattern = re.compile(r"(.+?)(\d+)to(\d+)")

        for btn in self.findChildren(type(self.home)):
            name = btn.objectName()

            match = pattern.fullmatch(name)

            if match:
                category, from_page, to_page = match.groups()

                btn.clicked.connect(
                    lambda checked=False,
                    c=category,
                    p=to_page:
                    self.goto_product_page(c, p)
                )

    def goto_product_page(self, category, page_number):
        """
        cpu + 2 -> cpu2
        gpu + 1 -> gpu1
        """

        page_name = f"{category}{page_number}"

        page = self.findChild(type(self.home_page), page_name)

        if page:
            self.productlist.setCurrentWidget(page)
         

    # ------------------ ham ho tro ------------------
    def set_active(self, btn):
        buttons = [
            self.home,
            self.linh_kien,
            self.pc,
            self.sap_co,
            self.account,
            self.cpu,
            self.gpu,
            self.mainboard,
            self.ram,
            self.ssd,
            self.psu,
            self.case_2,
            self.casefan
        ]

        for b in buttons:
            b.setProperty("class", "")

        btn.setProperty("class", "active")

        # refresh style
        for b in buttons:
            b.style().unpolish(b)
            b.style().polish(b)
            b.update()
