# -*- coding: utf-8 -*-


class Conf:

    min_variants = 1
    max_variants = 7
    default_variants = 5

    delta = 0.0009
    max_iterations = (1 << 100)
    # k1 = 0.0995 / 0.09        # Это тот k1, при котором start_lambda совпадает с методичкой
    k1 = 0.99995
    k2 = 1000

