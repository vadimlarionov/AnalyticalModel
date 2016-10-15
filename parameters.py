# -*- coding: utf-8 -*-


class Param:
    def __init__(self, row, text, values=None):
        if values is None:
            values = []
        self.row = row
        self.text = text
        self.values = values

    def __repr__(self):
        return 'Param: {' + 'row: {}, text: {}, values: {}'.format(self.row, self.text, self.values) + '}'


def check_params(params):
    current_row = 0
    for key in params.keys():
        if key != current_row:
            msg = 'actual=' + str(key) + ' , expected=' + str(current_row)
            raise ValueError(msg)
        current_row += 1


class InputParams(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.num_ws = Param(0, 'Количество рабочих станций', [10, 10, 10, 10, 10])
        self[self.num_ws.row] = self.num_ws

        self.t_processing_ws = Param(1, 'Среднее время дообработки запроса на РС', [0, 0, 0, 0, 50])
        self[self.t_processing_ws.row] = self.t_processing_ws

        self.t_formation_req = Param(2, 'Среднее время формирования запроса на РС', [100, 200, 100, 100, 50])
        self[self.t_formation_req.row] = self.t_formation_req

        self.t_transfer_forward = Param(3, 'Среднее время передачи через канал в прямом направлении', [1, 1, 1, 1, 1])
        self[self.t_transfer_forward.row] = self.t_transfer_forward

        self.t_transfer_back = Param(4, 'Среднее время передачи через канал в обратном направлении', [1, 1, 1, 1, 1])
        self[self.t_transfer_back.row] = self.t_transfer_back

        self.num_processors = Param(5, 'Количество процессоров', [1, 1, 1, 1, 1])
        self[self.num_processors.row] = self.num_processors

        self.t_process_on_processor = Param(6, 'Среднее время обработки запроса на процессоре', [10, 10, 10, 10, 10])
        self[self.t_process_on_processor.row] = self.t_process_on_processor

        self.num_disks = Param(7, 'Количество дисков', [1, 1, 2, 1, 2])
        self[self.num_disks.row] = self.num_disks

        self.t_process_on_disk = Param(8, 'Среднее время обработки запроса на диске', [10, 10, 20, 20, 20])
        self[self.t_process_on_disk.row] = self.t_process_on_disk

        self.p_access_to_disk = Param(9, 'Вероятность обращения запроса к ЦП после обработки на диске',
                                      [0, 0, 0, 0, 0.5])
        self[self.p_access_to_disk.row] = self.p_access_to_disk

        sorted(self)
        check_params(self)


class OutputParams(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__count_attributes = 0

        self.__add_attribute('load_ws', 'Загрузка рабочей станции')
        self.__add_attribute('load_user', 'Загрузка ользователя')
        self.__add_attribute('avg_ws', 'Среднее количество работающих РС')
        self.__add_attribute('load_channel', 'Загрузка канала')
        self.__add_attribute('load_processor', 'Загрузка процессора')
        self.__add_attribute('load_disk', 'Загрузка i-го диска')
        self.__add_attribute('t_cycle', 'Среднее время цикла системы')
        self.__add_attribute('t_reaction', 'Среднее время реакции системы')
        self.__add_attribute('start_lambda', 'Начальная интенсивность фонового потока')
        self.__add_attribute('end_lambda', 'Конечная интенсивность фонового потока')
        self.__add_attribute('num_iterations', 'Количество итераций')

        sorted(self)
        check_params(self)

    def __add_attribute(self, attribute_name, param_text):
        param = Param(self.__count_attributes, param_text)
        self.__count_attributes += 1
        setattr(self, attribute_name, param)
        self[param.row] = param
