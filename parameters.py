# -*- coding: utf-8 -*-


class Param:
    def __init__(self, row, text, values=None):
        if values is None:
            values = []
        self.row = row
        self.text = text
        self.values = values


def check_params(params):
    current_row = 0
    for key in params.keys():
        if key != current_row:
            msg = 'actual=' + str(key) + ' , expected=' + str(current_row)
            raise ValueError(msg)
        current_row += 1

input_params = {}

num_ws = Param(0, 'Количество рабочих станций', [10, 10, 10, 10, 10])
input_params[num_ws.row] = num_ws

t_processing_ws = Param(1, 'Среднее время дообработки запроса на РС', [0, 0, 0, 0, 0])
input_params[t_processing_ws.row] = t_processing_ws

t_formation_req = Param(2, 'Среднее время формирования запроса на РС', [100, 200, 100, 100, 50])
input_params[t_formation_req.row] = t_formation_req

t_transfer_forward = Param(3, 'Среднее время передачи через канал в прямом направлении', [1, 1, 1, 1, 1])
input_params[t_transfer_forward.row] = t_transfer_forward

t_transfer_back = Param(4, 'Среднее время передачи через канал в обратном направлении', [1, 1, 1, 1, 1])
input_params[t_transfer_back.row] = t_transfer_back

num_processors = Param(5, 'Количество процессоров', [1, 1, 1, 1, 1])
input_params[num_processors.row] = num_processors

t_process_on_processor = Param(6, 'Среднее время обработки запроса на процессоре', [10, 10, 10, 10, 10])
input_params[t_process_on_processor.row] = t_process_on_processor

num_disks = Param(7, 'Количество дисков', [1, 1, 2, 1, 2])
input_params[num_disks.row] = num_disks

t_process_on_disk = Param(8, 'Среднее время обработки запроса на диске', [10, 10, 20, 20, 20])
input_params[t_process_on_disk.row] = t_process_on_disk

p_access_to_disk = Param(9, 'Вероятность обращения запроса к ЦП после обработки на диске', [0, 0, 0, 0, 0.5])
input_params[p_access_to_disk.row] = p_access_to_disk

# Check params
sorted(input_params)
check_params(input_params)
