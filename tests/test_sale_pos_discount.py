# This file is part of the sale_pos_discount module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SalePOSDiscountTestCase(ModuleTestCase):
    'Test Sale POS Discount module'
    module = 'sale_pos_discount'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SalePOSDiscountTestCase))
    return suite
