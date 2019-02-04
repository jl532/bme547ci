# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:17:13 2019

@author: Mars
"""
import re


def is_tachycardic(inputString):
    rmPuncInput = re.sub(r'\W', '', inputString)
    loweredInput = str.lower(rmPuncInput)
    if loweredInput == "tachycardic":
        output = True
    else:
        output = False
    return output


def main():
    pass


if __name__ == "__main__":
    main()
