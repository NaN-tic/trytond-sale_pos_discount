# This file is part of the sale_pos_discount module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import sale


def register():
    Pool.register(
        sale.SaleLine,
        module='sale_pos_discount', type_='model')
