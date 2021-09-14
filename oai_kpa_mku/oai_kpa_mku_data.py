import time
import struct
import oai_modbus


class OaiMKU:
    def __init__(self, **kwargs):
        self.serial_number = kwargs.get('serial_num', '20693699424D')
        self.debug = kwargs.get('debug', False)

        self.client = oai_modbus.OAI_Modbus(serial_num=[self.serial_number])

        self.client.debug_print_flag = self.debug

        self.state = 0

        #self.low_time = 0x86A0
        #self.high_time = 0x0001
        self.dec = 100
        self.set_time(dec=self.dec)
        self.GPIO_alternative_set = 1228
        self.GPIO1_12_alternative_set = 1242
        self.GPIO13_28_alternative_set = 1243

    def init(self):
        self.client.ao_read_ranges = [[1228, 1245], [1059, 1063]]
        self.client.write_regs(offset=1060, data_list=[0x1FFF, 0xF000, 0x0000, 0x0000])

    def set_time(self, dec):
        tmp = (dec * 1000)
        self.low_time = int(hex((tmp >> 0) & 0xFFFF), 16)
        self.high_time = int(hex((tmp >> 16) & 0xFFFF), 16)

    def connect(self, serial_num=None):
        """
        connection to the HW-module
        connection parameter can be updated
        :param serial_num: serial_number
        :return: nothing
        """
        if serial_num:
            self.serial_number = serial_num
            self.client.serial_numbers.append(self.serial_number)
        pass
        if self.client.connect() == 1:
            self.init()
            self.state = 1
        else:
            self.state = -1
        return self.state

    def disconnect(self):
        try:
            if self.client.disconnect() == 0:
                self.state = 0
            else:
                self.state = -1
        except AttributeError:
            self.state = -1
            pass
        return self.state

    def reconnect(self):
        self.disconnect()
        self.connect()

    def impact(self, low_time, high_time, offset, gpio_num):
        """
        Set gpio to output for a specific amount of time
        :param low_time: set time     0x0000[0000]
        :param high_time: set time    0x[0000]0000
        :param gpio_num: number gpio
        :return:
        """

        self.client.write_regs(offset=offset, data_list=[gpio_num])
        self.client.write_regs(offset=self.GPIO_alternative_set,
                               data_list=[0x0001, 0x0001, 0x0000, 0x0000, 0x0000, low_time, high_time, 0x0000, 0x0000])

    def on_gpio(self, offset, ao_register_map):
        """
            Set gpio to output
        :param offset: register number
        :param ao_register_map: register map
        :return:
        """
        self.client.write_ranges = ao_register_map
        self.client.write_regs(offset, ao_register_map)

    def off_gpio(self, offset):
        """
            Set all gpio in register to input
        :param offset: register number
        :return:
        """
        self.client.write_regs(offset, [0x1000, 0x0000, 0x0000, 0x0000])

    def gpio_1(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0800)

    def gpio_2(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0400)

    def gpio_3(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0200)

    def gpio_4(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0100)

    def gpio_5(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0080)

    def gpio_6(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0040)

    def gpio_7(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0020)

    def gpio_8(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0010)

    def gpio_9(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0008)

    def gpio_10(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0004)

    def gpio_11(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0002)

    def gpio_12(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0001)

    def gpio_13(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO13_28_alternative_set,
                    gpio_num=0x8000)

    def gpio_14(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO13_28_alternative_set,
                    gpio_num=0x4000)

    def gpio_15(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO13_28_alternative_set,
                    gpio_num=0x2000)

    def gpio_16(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO13_28_alternative_set,
                    gpio_num=0x1000)


if __name__ == '__main__':
    mku = OaiMKU(serial_num="20693699424D", debug=True)
    mku.connect()
    mku.set_time(dec=100)
    print(hex(mku.low_time))
    print(hex(mku.high_time))

    mku.gpio_1()
