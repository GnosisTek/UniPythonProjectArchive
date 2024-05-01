# -*- coding: utf-8 -*-
# pylint: disable=C0103

''' 
Unittests for jugs class
'''


import unittest


from jugs import Jug

class Jug_tests(unittest.TestCase):
    ''' tests Jug class '''

    def test_cap(self):
        ''' tests capacity set by __init__ '''
        self.assertAlmostEqual(Jug(123).capacity(), 123)

    def test_temp(self):
        ''' tests pour_in temperature()'''
        j = Jug(123)
        j.pour_in(32, 56)
        self.assertAlmostEqual(j.temperature(), 56)

    def test_wv(self):
        ''' tests pour_in water_volume()'''
        j = Jug(123)
        j.pour_in(32, 56)
        self.assertAlmostEqual(j.water_volume(), 32)

    def test_over(self):
        ''' tests pour_in overflow'''
        j = Jug(123)
        j.pour_in(249, 56)
        self.assertAlmostEqual(j.water_volume(), 123)

    def test_out(self):
        ''' tests pour_out without supplying into_jug'''
        j = Jug(123)
        j.pour_in(100, 56)
        j.pour_out(6)
        self.assertAlmostEqual(j.water_volume(), 94)

    def test_allout(self):
        ''' tests pour_out with 'all' '''
        j = Jug(123)
        j.pour_in(100, 56)
        j.pour_out('all')
        self.assertAlmostEqual(j.water_volume(), 0)

    def test_allout2(self):
        ''' tests pour_out stipulating more than is inside'''
        j = Jug(123)
        j.pour_in(100, 56)
        j.pour_out(200)
        self.assertAlmostEqual(j.water_volume(), 0)

    def test_out_in(self):
        ''' tests pour_out supplying into_jug, checking volume'''
        j = Jug(123)
        j2 = Jug(20)
        j.pour_in(100, 56)
        j.pour_out(10, into_jug=j2)
        self.assertAlmostEqual(j2.water_volume(), 10)

    def test_out_in2(self):
        ''' tests pour_out supplying into_jug, checking temperature'''
        j = Jug(123)
        j2 = Jug(20)
        j.pour_in(100, 56)
        j.pour_out(10, into_jug=j2)
        self.assertAlmostEqual(j2.temperature(), 56)

    def test_out_in3(self):
        ''' tests pour_out supplying into_jug, checking mixing temperature'''
        j = Jug(123)
        j2 = Jug(20)
        j.pour_in(10, 60)
        j2.pour_in(10, 0)
        j.pour_out(10, into_jug=j2)
        self.assertAlmostEqual(j2.temperature(), 30)

unittest.main(exit=False)


