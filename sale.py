# This file is part of sale_pos_discount module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['SaleLine']
__metaclass__ = PoolMeta


class SaleLine:
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

#     def update_prices(self):
#         result = super(SaleLine, self).update_prices()
#         result['unit_price_w_tax'] = super(SaleLine, self).get_price_with_tax(
#             [self], ['unit_price_w_tax', 'amount_w_tax']
#             )['unit_price_w_tax'][self.id]
#         result['amount_w_tax'] = super(SaleLine, self).get_price_with_tax(
#             [self], ['unit_price_w_tax', 'amount_w_tax']
#             )['amount_w_tax'][self.id]
#         return result
