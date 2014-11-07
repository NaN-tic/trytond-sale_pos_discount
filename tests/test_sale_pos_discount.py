#!/usr/bin/env python
# This file is part of the sale_pos_discount module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_depends, test_view
import os
import sys
import trytond.tests.test_tryton
import unittest


class SalePOSDiscountTestCase(unittest.TestCase):
    'Test Sale POS Discount module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_pos_discount')

    def test0005views(self):
        'Test views'
        test_view('sale_pos_discount')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SalePOSDiscountTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
