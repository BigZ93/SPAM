import numpy as np
import matplotlib as mpl
import pandas as pd
import random

def spam(data, minSup):
    patterns = []
    V, F = generateCandidates(data, minSup)
    #for i in F:
    #   search(...)
    return patterns


def search(pattern, S, I, minSup):
    p = ][]
    tempS = []
    tempI = []
    #for j in S:
    #   if:
    #
    #for j in tempS:
    #    search()
    #for j in I:
    #    if:
    #
    #for j in tempI:
    #   search()
    return p


def generateCandidates(ds, minSup):
    V = []
    F = []
    #list of all letters
    letters = []
    temp = len(ds)
    for i in range(0, temp):
        transaction = ds[i]
        sequence = transaction[1]
        temp2 = len(sequence)
        for j in range(0, temp2):
            item = sequence[j]
            temp3 = len(item)
            for k in range(0, temp3):
                letter = item[k]
                if letter not in letters:
                    letters.append(letter)

    letters.sort()
    print(letters)
    #vertical database
    l = []
    l2 = []
    temp0 = len(letters)
    for m in range(0, temp0):#tebelka dla kazdej litery   temp0
        l2 = []
        for i in range(0, temp):#dla kazdego sid   temp
            l = []
            transaction = ds[i]
            sequence = transaction[1]
            temp2 = len(sequence)
            for j in range(0, temp2):#dla kazdego itemsetu   temp2
                item = sequence[j]
                temp3 = len(item)
                for k in range(0, temp3):#dla kazdego itemu   temp3
                    letter = item[k]
                    if letter is letters[m]:
                        l.append(j)

            #if not l:
                #l.append("-")

            tuple = (i, l)
            #print("tumple ", tuple)
            l2.append(tuple)

        tuple2 = (letters[m], l2)
        #print("    tuple2 ", tuple2)
        V.append(tuple2)

    print("V", V)
    #frequent itemset
    for m in range(0, temp0):#tebelka dla kazdej litery   temp0
        count = 0
        for i in range(0, temp):#dla kazdego sid   temp
            transaction = ds[i]
            sequence = transaction[1]
            temp2 = len(sequence)
            for j in range(0, temp2):#dla kazdego itemsetu   temp2
                item = sequence[j]
                temp3 = len(item)
                for k in range(0, temp3):#dla kazdego itemu   temp3
                    letter = item[k]
                    if letter is letters[m]:
                        count = count + 1

        tuple = (letters[m], count)
        #print("tuple", tuple)
        if count > minSup:
            F.append(tuple)

    print("F", F)

    return V, F


def generateData(maxItems, maxSeqLength, maxItemLength, lastLetter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    table = []
    seq = []
    item = []
    for i in range(0, maxItems):    #maxItems
        seq = []
        seqLength = random.randint(1, maxSeqLength)
        for j in range(0, seqLength):   #seqLength
            item = []
            itemLength = random.randint(1, maxItemLength)
            for k in range(0, itemLength):  #itemLength
                while(1):
                    l = alphabet[random.randint(0, lastLetter)]
                    if l not in item:
                        break

                item.append(l)

            item.sort()
            seq.append(item)

        tuple = (i, seq)
        table.append(tuple)

    return table


if __name__ == "__main__":
    #a = input("give number of transactions: ")
    #b = input("give maximum length of a sequence: ")
    #c = input("give maximum length of a itemset: ")
    #d = input("give maximum number of letter from the alphabet to choose from: ")
    #e = input("give minimum support: ")
    dataset = generateData(4, 3, 2, 5)
    vds, f = generateCandidates(dataset, minSup=1)
    print(dataset)

