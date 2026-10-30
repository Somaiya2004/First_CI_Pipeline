import importlib
import pytest

dec_bin_mod = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = dec_bin_mod.decimal_to_binary

def test_decimal_to_binary_basic():
    assert decimal_to_binary(5) == "101"
    assert decimal_to_binary(10) == "1010"

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "0"

def test_decimal_to_binary_powers_of_two():
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(8) == "1000"

def test_decimal_to_binary_negative():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)
