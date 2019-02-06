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
        ("cidracyhcat", "tachycardic", False)
])
    
    
def test_string_tolerance(testString, targetString, expected):
    from tachycardia import string_tolerance
    
    string_tolerance_test = string_tolerance(testString, targetString)
    assert string_tolerance_test == expected