import time
import struct
import oai_modbus


class OaiMKU:
    def __init__(self, **kwargs):

        self.client = oai_modbus.OAI_Modbus(serial_num=['20703699424D'], debug=True)
        self.client.connect()

        self.client.continuously_ao_flag = True
        self.client.continuously_ai_flag = True
        self.client.reverse_bytes_flag = True

        self.client.ao_read_ranges = [[1059, 1063]]
        # self.init_GPIO_write_ranges = [1060, [0x1FE0, 0x0000, 0x0000, 0x0000]]
        self.init_GPIO_write_ranges = [0x1FE0, 0x0000, 0x0000, 0x0000]
        self.client.write_ranges = self.init_GPIO_write_ranges
        self.offset = 1060
        self.client.write_regs(self.offset, self.init_GPIO_write_ranges)
        self.low_time = 0x86A0
        self.high_time = 0x0001

    def impulse(self, low_time, high_time, gpio1_12):
        self.client.write_ranges = [0x0001, 0x0001, 0x0000, 0x0000, 0x0000, self.low_time, self.high_time, 0x0000, 0x0000, gpio1_12, 0x0000, 0x0000, 0x0000]
        self.offset = [1228]
        self.client.write_regs(self.offset, self.client.write_ranges)

    def impact(self, ao_register_map, def_register_map):
        self.client.write_ranges = ao_register_map
        self.client.write_regs()
        time.sleep(1)
        self.client.write_ranges = def_register_map
        self.client.write_regs()

    def tk_on(self):                                    # на панели ТК вкл / в Ш2 ТК"Вкл. БДД"(-) 5,6 пин
        #ao_register_map = [[1064, [0x1800]]]
        #def_register_map = [[1064, [0x1000]]]
        #self.impact(ao_register_map, def_register_map)
        gpio1_12 = [0x1800]
        low_time = self.low_time
        high_time = self.high_time
        self.impulse(low_time, high_time, gpio1_12)

    def tk_off(self):                                   # на панели ТК откл / в Ш2 ТК"Выкл. БДД"(-) 7,8 пин
        ao_register_map = [[1064, [0x1400]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)

    def mrk_on(self):                                   # на панели МРК вкл / Ш2 МКУ"Вкл. БДД"(-) 9,10 пин
        ao_register_map = [[1064, [0x1200]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)

    def mrk_off(self):                                  # на панели МРК откл / Ш2 МКУ"Выкл. БДД"(-) 11,12 пин
        ao_register_map = [[1064, [0x1100]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)

    def pk2_on(self):                                   # на панели ПК2 вкл / Ш2 МКУ"Вкл. 2БДК"(-) 13,14 пин
        ao_register_map = [[1064, [0x1040]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)

    def pk1_on(self):                                   # на панели ПК1 вкл / Ш2 МКУ"Вкл. 1БДК"(-) 15,16 пин
        ao_register_map = [[1064, [0x1080]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)

    def pk_off(self):                                   # на панели ПК откл / Ш2 МКУ"Выкл. БДК"(-) 17,18 пин
        ao_register_map = [[1064, [0x1020]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)

    def gpio_8(self):
        ao_register_map = [[1064, [0x1010]]]
        def_register_map = [[1064, [0x1000]]]
        self.impact(ao_register_map, def_register_map)


if __name__ == '__main__':

    mku = OaiMKU()
    #mku.tk_on()
    #mku.tk_off()
    #mku.mrk_on()
    #mku.mrk_off()
    #mku.pk1_on()
    #mku.pk2_on()
    #mku.pk_off()

    #mku.gpio_8()

