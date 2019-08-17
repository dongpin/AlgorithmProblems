import unittest

from Python.Problems.epi5_6_buy_and_sell_a_stock_once import *

# Test Cases
def test_buy_and_sell_a_stock_once():
    assert buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30
