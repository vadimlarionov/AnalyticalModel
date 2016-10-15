# -*- coding: utf-8 -*-

from math import pow, fabs
from conf import Conf


class AnalyticalModel:
    def __init__(self, num_ws, t_processing_ws, t_formation_req, t_transfer_forward,
                 t_transfer_back, num_processors, t_process_on_processor, num_disks,
                 t_process_on_disk, p_access_to_disk):
        self.__num_ws = num_ws
        self.__t_processing_ws = t_processing_ws
        self.__t_formation_req = t_formation_req
        self.__t_transfer_forward = t_transfer_forward
        self.__t_transfer_back = t_transfer_back
        self.__num_processors = num_processors
        self.__t_process_on_processor = t_process_on_processor
        self.__num_disks = num_disks
        self.__t_process_on_disk = t_process_on_disk
        self.__p_access_to_disk = p_access_to_disk

        self.beta = 1 / (1 - self.__p_access_to_disk)
        self.t_k = (self.__t_transfer_forward + self.__t_transfer_back) / 2
        self.p_i = 1 / self.__num_disks
        self.lambda_f1 = self.__lambda_f1()
        self.start_lambda = self.lambda_f1
        self.end_lambda = None

    def __lambda_f1(self):
        min_value = min(1 / (2 * self.t_k), self.__num_processors / (self.beta * self.__t_process_on_processor),
                        1 / (self.beta * self.p_i * self.__t_process_on_disk))
        return Conf.k1 * min_value * (self.__num_ws - 1) / self.__num_ws

    def t_stay_on_channel(self):
        return 2 * self.t_k / (1 - 2 * self.lambda_f1 * self.t_k)

    def t_stay_on_processor(self):
        value = self.beta * self.lambda_f1 * self.__t_process_on_processor / self.__num_processors
        return self.beta * self.__t_process_on_processor / (1 - pow(value, self.__num_processors))

    def t_stay_on_disk(self):
        value = self.beta * self.p_i * self.lambda_f1 * self.__t_process_on_disk
        return self.beta * self.__t_process_on_disk / (1 - value)

    def t_cycle(self):
        return self.__t_processing_ws + self.__t_formation_req + \
               self.t_stay_on_channel() + self.t_stay_on_processor() + self.t_stay_on_disk()

    def lambda_f(self):
        self.end_lambda = (self.__num_ws - 1) / self.t_cycle()
        return self.end_lambda

    def load_ws(self):
        return (self.__t_processing_ws + self.__t_formation_req) / self.t_cycle()

    def load_user(self):
        return self.__t_formation_req / self.t_cycle()

    def __lambda(self):
        return self.__num_ws / self.t_cycle()

    def load_channel(self):
        return 2 * self.__lambda() * self.t_k

    def load_processor(self):
        return self.beta * self.__lambda() * self.__t_process_on_processor / self.__num_processors

    def load_disk(self):
        return self.beta * self.__lambda() * self.p_i * self.__t_process_on_disk

    def modeling(self):
        iteration = 0
        current_delta = Conf.delta + 1
        while current_delta > Conf.delta and iteration < Conf.max_iterations:
            lambda_f = self.lambda_f()
            diff = self.lambda_f1 - lambda_f
            current_delta = fabs(diff) / lambda_f
            self.lambda_f1 -= diff / Conf.k2
            iteration += 1
        if iteration == Conf.max_iterations:
            print('Reached the maximum number of iterations=' + str(iteration))
        return iteration
