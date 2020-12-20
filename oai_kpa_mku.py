import json
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import time
import os
import re
import oai_kpa_mku_data
import oai_kpa_mku_widget


class ClientGUIWindow(QtWidgets.QWidget, oai_kpa_mku_widget.Ui_Form):
    def __init__(self, *args, **kwargs):
        # # Стандартная часть окна # #
        # обязательная часть для запуска виджета
        super().__init__()
        self.setupUi(self)

        # словарь настройки (здесь же обрабатывается параметры **kwargs)
        self.uniq_name = kwargs.get("uniq_name", 'oai_kpa_stm_un')
        self.core_cfg = {'serial_num': '20653699424D', 'widget': True}
        self.user_cfg = {'example': '20653699424D'}
        self.default_cfg = {'core': self.core_cfg, 'user': self.user_cfg}
        self.loaded_cfg = self.load_cfg()
        self.cfg = self.cfg_process(self.loaded_cfg, kwargs)

        # отслеживание состояния окна

        self.state = 0
        # # Изменяемая часть окна # #
        self.moduleSerialNumberLEdit.setText(self.cfg["core"]["serial_num"])

        # Часть под правку: здесь вы инициализируете необходимые компоненты
        self.module = oai_kpa_mku_data.OaiMKU()

        # описываем элементы стандартного окна
        self.connectionPButton.clicked.connect(self.reconnect)
        self.pushButton_TK_On.clicked.connect(self.module.tk_on)
        self.pushButton_TK_Off.clicked.connect(self.module.tk_off)
        self.pushButton_MRK_Off.clicked.connect(self.module.mrk_off)
        self.pushButton_MRK_On.clicked.connect(self.module.mrk_on)
        self.pushButton_PK1.clicked.connect(self.module.pk1_on)
        self.pushButton_PK2.clicked.connect(self.module.pk2_on)
        self.pushButton_PK_Off.clicked.connect(self.module.pk_off)

    @staticmethod
    def cfg_process(default_cfg, new_cfg):
        """
        Process default and new cfg-s and forms actual cfg
        :param default_cfg: default parameters set
        :param new_cfg: cfg to update
        :return: actual_cfg
        """
        cfg = default_cfg
        for key, value in new_cfg.items():
            for c_key, c_value in default_cfg["core"].items():
                if c_key == key:
                    cfg["core"][key] = value
            for c_key, c_value in default_cfg["user"].items():
                if c_key == key:
                    cfg["user"][key] = value
        return cfg

    def connection_state_check(self):
        if self.module.state == -2:
            self.set_status_string(string="Ошибка подключения", color="lightcoral")
        elif self.module.state == -1:
            self.set_status_string(string="Ошибка подключения", color="orangered")
        elif self.module.state == 0:
            self.set_status_string(string="Необходимо подключение", color="white")
        elif self.module.state == 1:
            self.set_status_string(string="Подключение успешно", color="darkseagreen")
        else:
            self.set_status_string(string="Подключение успешно", color="white")
        pass

    def set_status_string(self, string="Нет информации", color="white"):
        self.statusLineEdit.setText(str(string))
        self.statusLineEdit.setStyleSheet('QLineEdit {background-color: %s;}' % color)

    def connect(self):
        serial_number = self.moduleSerialNumberLEdit.text()
        if re.findall(r"[0-9a-fA-F]{8,12}", serial_number):
            self.cfg["core"]["serial_num"] = serial_number
        else:
            serial_number = self.serial_number
            self.moduleSerialNumberLEdit.setText(self.cfg["core"]["serial_num"])
        self.module.connect(serial_num=serial_number)
        self.connection_state_check()
        #
        self.save_cfg()
        pass

    def disconnect(self):
        self.module.disconnect()
        self.connection_state_check()
        pass

    def reconnect(self):
        self.disconnect()
        self.connect()
        self.connection_state_check()
        pass

    def save_cfg(self):
        try:
            os.mkdir("cfg")
        except OSError as error:
            pass
        #
        with open("cfg\\" + self.uniq_name + ".json", 'w') as cfg_file:
            json.dump(self.cfg, cfg_file)

    def save_default_cfg(self):
        try:
            os.mkdir("cfg")
        except OSError as error:
            pass
        #
        with open("cfg\\" + self.uniq_name + ".json", 'w') as cfg_file:
            json.dump(self.default_cfg, cfg_file)

    def load_cfg(self):
        loaded_cfg = {}
        try:
            with open("cfg\\" + self.uniq_name + ".json", 'r') as cfg_file:
                loaded_cfg = json.load(cfg_file)
        except FileNotFoundError:
            loaded_cfg = self.default_cfg
        return loaded_cfg

    def closeEvent(self, event):
        #
        pass


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)
    ui = ClientGUIWindow(uniq_name="oai_kpa_mku", widget='True')
    ui.show()
    app.exec_()

    #app = QtWidgets.QApplication(sys.argv)
    #Form = QtWidgets.QWidget()
    #ui = ClientGUIWindow(uniq_name="oai_kpa_mku", widget='True')
    #ui.setupUi(Form)
    #Form.show()
    #sys.exit(app.exec_())