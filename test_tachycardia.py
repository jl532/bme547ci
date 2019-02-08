# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:37:09 2019

@author: Mars
"""
import pytest


@pytest.mark.parametrize("inputString, expected", [
        ("tachycardic", True),  # random capitalization
        ("Tachycardic", True),
        ("TachycardiC", True),
        ("tachYcardic", True),
        (" tachycardic", True),
        ("tachycardic ", True),
        ("...tachycardic...", True),  # random punctionation
        (" , tachycardic , ", True),
        (" Jason Liu", False),  # True Negative
        (" tachycrdic ", True),  # deletions
        (" achycardic ", True),
        (" T4chycardic", True),  # substitutions
        (" Tacycard1c", True),  # combination of delection and substitution
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
        '124', '12',
        '123'
]


@pytest.mark.parametrize("inputStr, expected", [
        ("123", ['123', '23', '3', '2', '13', '1', '12']),
        ("1234", slice1234Output),
])
def test_string_slicer_two(inputStr, expected):
    from tachycardia import string_slicer_two

    slicer_output_test = string_slicer_two(inputStr)
    assert slicer_output_test == expected


@pytest.mark.parametrize("inputStr, targetStr, expected", [
        ("jason liu", "jason liu", True),
        ("jason li", "jason liu", True),
        ("jason l", "jason liu", True),
        ("json liu", "jason liu", True),
        ("1234567", "7654321", False),
        ("12367", "1234567", True),
        ("125678", "1234567", False),
        ("tachylardic", "tachycardic", True),
])
def test_max_overlap_finder(inputStr, targetStr, expected):
    from tachycardia import max_overlap_finder

    overlap_output = max_overlap_finder(inputStr, targetStr)
    assert overlap_output == expected
