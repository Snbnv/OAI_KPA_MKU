from PyQt5 import QtWidgets
import sys
from .oai_kpa_mku import *

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)
    ui = ClientGUIWindow(uniq_name="oai_kpa_mku", widget='False', debug='True')
    ui.show()
    app.exec_()
