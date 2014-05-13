#encoding: utf-8
import random
from nose.tools import *
import sys
sys.path.append('..')

from romanizer import romanize

def test_romanize_takes_a_number_as_argument():
    assert_raises(TypeError, romanize)

def test_romanize_number_can_not_be_negative():
    with assert_raises(ValueError) as e:
        romanize(random.randint(1, 1000) * -1)
    assert_equal(e.exception.message, 'can not romanize negative numbers')

def test_romanize_number_can_not_be_zero():
    with assert_raises(ValueError) as e:
        romanize(0)
    assert_equal(e.exception.message, 'can not romanize zero')

def test_romanize_returns_string():
    assert_is_instance(romanize(random.randint(1,1000)), str)


def test_romanize_should_encode_single_digit_numbers():
    assert_equal(romanize(1), 'I')
    assert_equal(romanize(2), 'II')
    assert_equal(romanize(3), 'III')
    assert_equal(romanize(4), 'IV')
    assert_equal(romanize(5), 'V')
    assert_equal(romanize(6), 'VI')
    assert_equal(romanize(7), 'VII')
    assert_equal(romanize(8), 'VIII')
    assert_equal(romanize(9), 'IX')


def test_romanize_should_encode_double_digit_numbers():
    assert_equal(romanize(10), 'X')
    assert_equal(romanize(12), 'XII')
    assert_equal(romanize(20), 'XX')
    assert_equal(romanize(36), 'XXXVI')
    assert_equal(romanize(44), 'XLIV')
    assert_equal(romanize(87), 'LXXXVII')
    assert_equal(romanize(92), 'XCII')


def test_romanize_should_encode_triple_digit_numbers():
    assert_equal(romanize(100), 'C')
    assert_equal(romanize(666), 'DCLXVI')
    assert_equal(romanize(747), 'DCCXLVII')
    assert_equal(romanize(999), 'CMXCIX')

def test_romanize_should_encode_four_digit_numbers():
    assert_equal(romanize(1000), 'M')
    assert_equal(romanize(1066), 'MLXVI')
    assert_equal(romanize(1492), 'MCDXCII')
    assert_equal(romanize(1978), 'MCMLXXVIII')
    assert_equal(romanize(2063), 'MMLXIII')
