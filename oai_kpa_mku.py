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
        # создание и обработка словаря настройки (здесь же обрабатывается параметры **kwargs)
        self.uniq_name = kwargs.get("uniq_name", 'oai_kpa_mku_un')
        self.debug = kwargs.get('debug', False)
        self.debug_print_flag = self.debug
        # настройки по умолчанию
        # настройки не для изменения (одинаковые для каждого типа плат)
        self.core_cfg = {'serial_num': '20693699424D',
                         'widget': True}
        # настройки для вашего модуля (разные для каждого типа плат)
        self.user_cfg = {
            'T': 100,
            'KU01': {'name': 'ТК вкл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Включить ТК</p></body></html>'},
            'KU02': {'name': 'ТК откл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Отключить ТК</p></body></html>'},
            'KU03': {'name': 'МРК вкл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Включить МРК</p></body></html>'},
            'KU04': {'name': 'МРК откл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Отключить МРК</p></body></html>'},
            'KU05': {'name': 'ПК1 вкл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Задействовать 1й полукомплект</p></body></html>'},
            'KU06': {'name': 'ПК2 вкл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Задействовать 2й полукомплект</p></body></html>'},
            'KU07': {'name': 'Откл', 'state': 1,
                     'tooltip': '<html><head/><body><p>Отключить БЭ</p></body></html>'},
            'KU08': {'name': '', 'state': 0, 'tooltip': ''},
            'KU09': {'name': '', 'state': 0, 'tooltip': ''},
            'KU10': {'name': '', 'state': 0, 'tooltip': ''},
            'KU11': {'name': '', 'state': 0, 'tooltip': ''},
            'KU12': {'name': '', 'state': 0, 'tooltip': ''},
            'KU13': {'name': '', 'state': 0, 'tooltip': ''},
            'KU14': {'name': '', 'state': 0, 'tooltip': ''},
            'KU15': {'name': '', 'state': 0, 'tooltip': ''},
            'KU16': {'name': '', 'state': 0, 'tooltip': ''}
        }
        self.default_cfg = {"core": self.core_cfg,
                            "user": self.user_cfg
                            }
        self.loaded_cfg = self.load_cfg()
        self.cfg = self.cfg_process(self.loaded_cfg, kwargs)
        # скрываем ненужные элементы
        if self.cfg["core"]["widget"] is str(True):
            self.connectionPButton.hide()
        # описываем элементы стандартного окна
        self.connectionPButton.clicked.connect(self.reconnect)
        # переменные для создание лога
        self.log_file_title = self.generate_log_title()
        self.log_file_data = ["0" for i in range(len(self.log_file_title))]
        self.log_file = None
        self.recreate_log_files()
        self.ku = ""
        # отслеживание состояния окна
        self.state = 0
        # # Изменяемая часть окна # #
        self.moduleSerialNumberLEdit.setText(self.cfg["core"]["serial_num"])
        # Часть под правку: здесь вы инициализируете необходимые компоненты
        self.module = oai_kpa_mku_data.OaiMKU(serial_num=self.cfg["core"]["serial_num"], debug=self.debug_print_flag)
        self.spinBox.setProperty("value", self.cfg["user"]["T"])
        self.module.set_time(self.spinBox.value())
        # описываем элементы стандартного окна
        self.button_init(push_button=self.pushButton_KU1, ku="KU01", gpio=self.module.gpio_1)
        self.button_init(push_button=self.pushButton_KU2, ku="KU02", gpio=self.module.gpio_2)
        self.button_init(push_button=self.pushButton_KU3, ku="KU03", gpio=self.module.gpio_3)
        self.button_init(push_button=self.pushButton_KU4, ku="KU04", gpio=self.module.gpio_4)
        self.button_init(push_button=self.pushButton_KU5, ku="KU05", gpio=self.module.gpio_5)
        self.button_init(push_button=self.pushButton_KU6, ku="KU06", gpio=self.module.gpio_6)
        self.button_init(push_button=self.pushButton_KU7, ku="KU07", gpio=self.module.gpio_7)
        self.button_init(push_button=self.pushButton_KU8, ku="KU08", gpio=self.module.gpio_8)
        self.button_init(push_button=self.pushButton_KU9, ku="KU09", gpio=self.module.gpio_9)
        self.button_init(push_button=self.pushButton_KU10, ku="KU10", gpio=self.module.gpio_10)
        self.button_init(push_button=self.pushButton_KU11, ku="KU11", gpio=self.module.gpio_11)
        self.button_init(push_button=self.pushButton_KU12, ku="KU12", gpio=self.module.gpio_12)
        self.button_init(push_button=self.pushButton_KU13, ku="KU13", gpio=self.module.gpio_13)
        self.button_init(push_button=self.pushButton_KU14, ku="KU14", gpio=self.module.gpio_14)
        self.button_init(push_button=self.pushButton_KU15, ku="KU15", gpio=self.module.gpio_15)
        self.button_init(push_button=self.pushButton_KU16, ku="KU16", gpio=self.module.gpio_16)

        self.Apply.clicked.connect(lambda: self.module.set_time(self.spinBox.value()))
        self.Apply.clicked.connect(self.log_write)

    def set_ku(self, ku):
        self.ku = ku

    def button_init(self, push_button, ku, gpio):
        """
        Button initialization, assigns parameters from cfg to a button (name, state, tooltip),
        sets visibility and clicked command
        :param push_button: button object from widget
        :param ku: button object from cfg
        :param gpio: function set gpio to output
        """
        if self.cfg["user"][ku]["state"] == 0:
            push_button.hide()
        _translate = QtCore.QCoreApplication.translate
        push_button.setToolTip(_translate("Form", self.cfg["user"][ku]["tooltip"]))
        push_button.setText(_translate("Form", self.cfg["user"][ku]["name"]))
        push_button.clicked.connect(gpio)
        push_button.clicked.connect(lambda: self.set_ku(ku))
        push_button.clicked.connect(self.log_write)
        push_button.clicked.connect(lambda: self.set_ku(""))

    def connection_state_check(self):
        """
        The useful method to generate correct status string with color
        """
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
        """
        setting string and color to gui output status-line
        :param string: string to GUI-output
        :param color: background color
        """
        self.statusLineEdit.setText(str(string))
        self.statusLineEdit.setStyleSheet('QLineEdit {background-color: %s;}' % color)

    def connect(self):
        """
        connection to kpa-module
        :return: nothing
        """
        serial_number = self.moduleSerialNumberLEdit.text()
        if re.findall(r"[0-9a-fA-F]{8,12}", serial_number):
            self.cfg["core"]["serial_num"] = serial_number
        else:
            serial_number = self.serial_number
            self.moduleSerialNumberLEdit.setText(self.cfg["core"]["serial_num"])
        self.module.connect(serial_num=serial_number)
        self.connection_state_check()
        #
        self.log_write()
        self.save_cfg()
        pass

    def disconnect(self):
        """
        disconnect from kpa_module, if connection is established; in other cases do nothing
        :return: nothing
        """
        self.module.disconnect()
        self.connection_state_check()
        pass

    def reconnect(self):
        """
        reconnect module
        :return: nothing
        """
        self.disconnect()
        self.connect()
        self.connection_state_check()
        pass

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

    def save_cfg(self):
        try:
            os.mkdir("cfg")
        except OSError as error:
            pass
        #
        with open("cfg\\" + self.uniq_name + ".json", 'w', encoding="utf-8") as cfg_file:
            json.dump(self.cfg, cfg_file, sort_keys=True, indent=4, ensure_ascii=False)

    def save_default_cfg(self):
        try:
            os.mkdir("cfg")
        except OSError as error:
            pass
        with open("cfg\\" + self.uniq_name + ".json", 'w', encoding="utf-8") as cfg_file:
            json.dump(self.default_cfg, cfg_file, sort_keys=True, indent=4, ensure_ascii=False)

    def load_cfg(self):
        try:
            with open("cfg\\" + self.uniq_name + ".json", 'r', encoding="utf-8") as cfg_file:
                loaded_cfg = json.load(cfg_file)
        except FileNotFoundError:
            loaded_cfg = self.default_cfg
        return loaded_cfg

    @staticmethod
    def create_log_file(file=None, dir_name="log", sub_dir="log", sub_sub_dir=True, prefix="", extension=".csv"):
        """
        log-file creation
        :param file: if log-file already created, it will be closed
        :param dir_name: the folder, where logs will be stored
        :param sub_dir: the postfix for time_date (%Y_%m_%d_<sub_dir>) sub_dir_name
        :param sub_sub_dir: if True in sub_dir the log-files will be placed in additional folder (%Y_%m_%d_%H-%M-%S_<sub_dir>)
        :param prefix: the file-name prefix ("%Y_%m_%d %H-%M-%S <prefix> <extension>)
        :param extension: the file-name extension ("%Y_%m_%d %H-%M-%S <prefix> <extension>)
        :return: lof_file handle
        """
        sub_dir_name = dir_name + "\\" + time.strftime("%Y_%m_%d", time.localtime()) + " " + sub_dir
        if sub_sub_dir:
            sub_sub_dir_name = sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                                   time.localtime()) + sub_dir
        else:
            sub_sub_dir_name = sub_dir_name
        try:
            os.makedirs(sub_sub_dir_name)
        except (OSError, AttributeError) as error:
            print(error)
            pass
        try:
            if file:
                file.close()
        except (OSError, NameError, AttributeError) as error:
            print(error)
            pass
        file_name = sub_sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                            time.localtime()) + prefix + " " + extension
        file = open(file_name, 'a', encoding="utf-8")
        return file

    @staticmethod
    def close_log_file(file=None):
        """
        closing lo-file, if it possible; in other cases does nothing
        :param file: file to close
        """
        if file:
            try:
                file.close()
            except (OSError, NameError, AttributeError) as error:
                print(error)
            finally:
                file = None
        pass

    def recreate_log_files(self):
        """
        log-file recreation
        """
        # перезапуск лог файла
        self.log_file = self.create_log_file(file=self.log_file, dir_name="log", sub_dir=self.uniq_name,
                                             sub_sub_dir=False, prefix=self.uniq_name, extension=".csv")
        self.log_file.write(self.log_file_title)
        pass

    def generate_log_title(self):
        """
        log-file title list generation
        :return: title list for log-file
        """
        # обязательная часть - время в формате с.мс
        log_title = ["Time, s", "T"]
        # список данных, генерируемых модулем
        data_title_list = []
        for i in self.cfg["user"]:
            if i == "T":
                continue
            elif self.cfg["user"][i]["state"] == 1:
                data_title_list.append(i + " (" + self.cfg["user"][i]["name"] + ")")
            else:
                data_title_list.append(i + " (not used)")
        log_title.extend(data_title_list)
        return ";".join(log_title) + "\n"

    def generate_log_data(self):
        """
        log-file data list generation
        :return: data list for log-file
        """
        # обязательная часть - время в формате с.мс
        if self.module.state == 1:
            log_title = ["%.3f" % time.perf_counter(), str(self.spinBox.value())]
        # список данных, генерируемых модулем
            data_title_list = []

            for i in self.cfg["user"]:
                if i == "T":
                    continue
                elif i == self.ku:
                    data_title_list.append("%.3f" % 1)
                else:
                    data_title_list.append("%.3f" % 0)
        #
            log_title.extend(data_title_list)
            return ";".join(log_title) + '\n'

    def log_write_as_connection(self):
        if 1:
            self.log_write()
        pass

    def log_write(self):
        """
        function, witch rerun every log_update_time_ms, to write data to log
        :return: nothing
        """
        log_data = self.generate_log_data()
        if log_data:
            self.log_file.write(log_data)
        pass

    def closeEvent(self, event):
        self.save_cfg()
        #
        try:
            self.log_file.close()
        except FileNotFoundError as error:
            print(error)
        pass


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)
    ui = ClientGUIWindow(uniq_name="oai_kpa_mku", widget='False', debug='True')
    ui.show()
    app.exec_()
