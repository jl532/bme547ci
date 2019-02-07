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
    if loweredInput == targetString:  # if literally found without punctuation
        output = True
    else:
        output = string_tolerance(loweredInput, targetString)
    return output


def string_tolerance(inputString, targetString):  # identify missing characters
    if len(inputString) > len(targetString):
        return False
    else:
        diffLists = (list(set(targetString) - set(inputString)))
        if len(diffLists) < 4:  # 4 set differences at most
            return max_overlap_finder(inputString, targetString)
        else:
            return False


def string_slicer_two(inStr):
    possibleSlices = []
    possibleSlices.append(inStr)
    for firstPos in range(len(inStr)):
        singleSlice = inStr[:firstPos] + inStr[firstPos + 1:]
        possibleSlices.append(singleSlice)
        for secondPos in range(len(inStr)-firstPos):
            doubleSlice = singleSlice[:secondPos] + singleSlice[secondPos + 1:]
            if doubleSlice not in possibleSlices:
                possibleSlices.append(doubleSlice)
    return possibleSlices


def max_overlap_finder(inputString, targetString):
    globalBestOverlap = 0
    possibleSlices = string_slicer_two(targetString)
    for eachPossibleSlice in possibleSlices:
        for overIndex in range(len(eachPossibleSlice) - len(inputString) + 1):
            overlap = 0
            for charLoc, eachInputChar in enumerate(inputString, 0):
                if eachInputChar == eachPossibleSlice[overIndex + charLoc]:
                    overlap = overlap + 1
            if overlap > globalBestOverlap:
                globalBestOverlap = overlap
    if globalBestOverlap >= len(targetString) - 2:
        return True
    else:
        return False


def main():
    pass


if __name__ == "__main__":
    main()
