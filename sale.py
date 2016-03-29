# This file is part of sale_pos_discount module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['SaleLine']


class SaleLine:
    __metaclass__ = PoolMeta
    __name__ = 'sale.line'

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        if 'discount' not in cls.unit_price_w_tax.on_change_with:
            cls.unit_price_w_tax.on_change_with.add('discount')
        if 'gross_unit_price' not in cls.unit_price_w_tax.on_change_with:
            cls.unit_price_w_tax.on_change_with.add('gross_unit_price')
        if 'discount' not in cls.amount_w_tax.on_change_with:
            cls.amount_w_tax.on_change_with.add('discount')
        if 'gross_unit_price' not in cls.amount_w_tax.on_change_with:
            cls.amount_w_tax.on_change_with.add('gross_unit_price')
