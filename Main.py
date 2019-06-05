import numpy as np
import matplotlib as mpl
import pandas as pd
import random
import itertools

def spam(data, minSup, frequentItems):
    F = frequentItems
    #V, F = generateCandidates(data, minSup, maxItemLength)
    for i in range(0, len(F)):#len(F)
        #print("item", F[i])
        s = F[i]
        pat = []
        pat.append(s)

        i = []
        i.append(s[0])

        checkIfFrequent(data, pat, minSup)
        search(pat, F, i, minSup, data)


def search(pattern, S, I, minSup, data):
    tempS = []
    tempI = []
    p = []
    elementsInTempSGreaterThani = []
    elementsInTempIGreaterThani = []

    for i in range(0, len(S)):#len(S)
        x = S[i]
        #print("aaa", x)
        p = []
        for j in range(0, len(pattern)):
            p.append(pattern[j])

        p.append(x)
        #print("bbb", p)
        if checkIfFrequent(data, p, minSup) is True:
            tempS.append(x)

    p2 = []
    #print("ccc", tempS)
    for i in range(0, len(tempS)):#len(tempS)
        x2 = tempS[i]
        #print("aaa", x2)
        p2 = []
        for j in range(0, len(pattern)):
            p2.append(pattern[j])

        p2.append(x2)
        # print("bbb", p)
        search(p2, tempS, elementsInTempSGreaterThani, minSup, data)

    #for i in range(0, len(I)):
    #    x2 = I[i]
    #    p2 = pattern
    #    l = len(p2)
    #    p2[l-1].append(x2)
    #    if checkIfFrequent(data, p, minSup):
    #        tempI.append(x2)

    #for i in range(0, tempI):
    #   search(p2, tempS, elementsInTempIGreaterThani, minSup, data)


def checkIfFrequent(ds, pattern, minSup):
    count = 0
    for i in range(0, len(ds)):#len(ds)
        transaction = ds[i]
        sequence = transaction[1]
        if len(pattern) > len(ds):
            continue

        m = 0
        for j in range(0, len(sequence)):#len(sequence)
            itemset = sequence[j]
            itemsetP = pattern[m]
            if len(itemsetP) > len(itemset):
                continue

            l = 0
            for k in range(0, len(itemset)):#len(itemset)
                item = itemset[k]
                itemP =itemsetP[l]
                if item is itemP:
                    l = l + 1
                    if l == len(itemsetP):
                        m = m + 1
                        break

            if m == len(pattern):
                count = count + 1
                break

    #print("counter ", count)
    if count >= minSup:
        print("pattern", pattern)
        return True

    return False


# not used
def generateCandidates(ds, minSup, maxItemLength):
    ds = [(0, [['a', 'b'], ['c'], ['f', 'g'], ['g'], ['e']]), (1, [['a', 'd'], ['c'], ['b'], ['a', 'b', 'e', 'f']]),
          (2, [['a'], ['b'], ['f'], ['e']]), (3, [['b'], ['f', 'g']])]

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
    freqs = []
    #set of frequent items
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

        if count >= minSup:
            F.append(letters[m])

    print("F", F)
    F.append(['a', 'b'])
    F.append(['f', 'g'])
    print("F", F)

    return V, F


# not used
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

    #dataset = generateData(4, 3, 2, 5)
    #print("generated data", dataset)

    minSup = 2
    ds = [(0, [['a', 'b'], ['c'], ['f', 'g'], ['g'], ['e']]),
          (1, [['a', 'd'], ['c'], ['b'], ['a', 'b', 'e', 'f']]),
          (2, [['a'], ['b'], ['f'], ['e']]),
          (3, [['b'], ['f', 'g']])]
    f = [['a'], ['b'], ['c'], ['e'], ['f'], ['g'], ['a', 'b'], ['f', 'g']]
    spam(ds, minSup, f)
    #checkIfFrequent(ds, [['a'], ['c'], ['f']], 2)
