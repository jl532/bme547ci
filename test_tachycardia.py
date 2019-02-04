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
])


def test_is_tachycardic(inputString, expected):
    from tachycardia import is_tachycardic

    isTachycardicTest = is_tachycardic(inputString)
    assert isTachycardicTest == expected
