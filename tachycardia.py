# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:17:13 2019

@author: Mars
"""
import re

def is_tachycardic(inputString):
    rmPuncInput = re.sub(r'\W', '', inputString)
    loweredInput = str.lower(rmPuncInput)
    targetString = "tachycardic"
    if loweredInput == targetString: # if literally found without punctuation
        output = True
    else:
        output = string_tolerance(loweredInput,targetString)
    return output

def string_tolerance(inputString, targetString):
    # identify missing characters
    if len(inputString) > len(targetString):
        return False
    else: # now, all we test are inputStrings that are the same lenth or less than targetString
        # diff the sets 
        diffLists = (list(set(targetString) - set(inputString))) 
        if len(diffLists) < 5: # now, there should be at most 2 mispellings and/or 2 missing chars, so 4 differences at most
            # if there are 4 or less differences, now there needs to be a comparison of the order of characters
            return True
        else:
            return False
        
def main():
    pass


if __name__ == "__main__":
    main()
