# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:37:09 2019

@author: Mars
"""
import pytest


@pytest.mark.parametrize("inputString, expected", [
        ("tachycardic", True),
        ("Tachycardic", True),
        ("TachycardiC", True),
        ("tachYcardic", True),
        (" tachycardic", True),
        ("tachycardic ", True),
        ("...tachycardic...", True),
        (" , tachycardic , ", True),
        (" Jason Liu", False),
        (" tachycrdic ", True),
        (" achycardic ", True),
        (" T4chycardic", True),
        (" Tacycard1c", True),
])
def test_is_tachycardic(inputString, expected):
    from tachycardia import is_tachycardic

    isTachycardicTest = is_tachycardic(inputString)
    assert isTachycardicTest == expected


@pytest.mark.parametrize("testString, targetString, expected", [
        ("jason liu", "tachycardic", False),
        ("tachycrdic", "tachycardic", True),
        ("achycardic", "tachycardic", True),
        ("t4chycardic", "tachycardic", True),
        ("tachycard1c", "tachycardic", True),
        ("t4chycard1c", "tachycardic", True),
        ("tchycardc", "tachycardic", True),
        ("tachycard", "tachycardic", True),
        ("cidracyhcat", "tachycardic", False),
        ("tachycidra", "tachycardic", False),
        ("thcaycardia", "tachycardic", False),
        ("tachycard", "tachycardic", True),
])
def test_string_tolerance(testString, targetString, expected):
    from tachycardia import string_tolerance

    string_tolerance_test = string_tolerance(testString, targetString)
    assert string_tolerance_test == expected

# needed to place the output in a separate list declaration
# because it wouldn't fit in one line.

slice1234Output = [
        '1234',
        '234', '34', '24', '23',
        '134', '14', '13',
        '124', '123'
]


@pytest.mark.parametrize("inputStr, expected", [
        ("123", ['123', '23', '3', '2', '13', '1', '12']),
        ("1234", slice1234Output),
])
def test_string_slicer_two(inputStr, expected):
    from tachycardia import string_slicer_two

    slicer_output_test = string_slicer_two(inputStr)
    assert slicer_output_test == expected
