import numpy as np
import matplotlib as mpl
import pandas as pd
import random
import itertools

def spam(data, minSup, frequentItems):
    F = frequentItems
    for i in range(0, len(F)):#len(F)
        s = F[i]
        pat = []
        pat.append(s)

        e = []
        for j in range(i+1, len(F)):
            e.append(F[j])

        checkIfFrequent(data, pat, minSup)
        search(pat, F, e, minSup, data)


def search(pattern, S, E, minSup, data):
    tempS = []
    tempE = []
    p = []
    elementsInTempSGreaterThani = []
    elementsInTempEGreaterThani = []

    for i in range(0, len(S)):#len(S)
        x = S[i]
        p = []
        for j in range(0, len(pattern)):
            p.append(pattern[j])

        p.append(x)
        if checkIfFrequent(data, p, minSup) is True:
            tempS.append(x)

    p2 = []
    for i in range(0, len(tempS)):#len(tempS)
        x2 = tempS[i]
        p2 = []
        for j in range(0, len(pattern)):
            p2.append(pattern[j])

        p2.append(x2)
        elementsInTempSGreaterThani = []
        for j in range(i+1, len(tempS)):
            elementsInTempSGreaterThani.append(tempS[j])

        search(p2, tempS, elementsInTempSGreaterThani, minSup, data)

    p3 = []
    for i in range(0, len(E)):#len(E)
        x3 = E[i]
        p3 = []
        for j in range(0, len(pattern)-1):
            p3.append(pattern[j])

        last = []
        temp = pattern[len(pattern)-1]
        for j in range(0, len(temp)):
            last.append(temp[j])
        flag = True
        for k in range(0, len(last)):
            if x3[0] == last[k]:
                flag = False

        if flag:
            for j in range(0, len(x3)):
                last.append(x3[j])

        p3.append(last)
        if checkIfFrequent(data, p3, minSup):
            tempE.append(x3)

    p4 = []
    for i in range(0, len(tempE)):#len(tempE)
        x4 = E[i]
        p4 = []
        for j in range(0, len(pattern) - 1):
            p4.append(pattern[j])

        last2 = []
        temp2 = pattern[len(pattern) - 1]
        for j in range(0, len(temp2)):
            last2.append(temp2[j])
        flag = True
        for k in range(0, len(last2)):
            if x4[0] is last2[k]:
                flag = True

        if flag:
            for j in range(0, len(x4)):
                last2.append(x4[j])

        p4.append(last2)
        elementsInTempEGreaterThani = []
        for j in range(i+1, len(tempE)):
            elementsInTempEGreaterThani.append(tempE[j])

        search(p4, tempS, elementsInTempEGreaterThani, minSup, data)


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
                itemP = itemsetP[l]
                if item is itemP:
                    l = l + 1
                    if l == len(itemsetP):
                        m = m + 1
                        break

            if m == len(pattern):
                count = count + 1
                break

    if count >= minSup:
        print("pattern ", pattern, " support ", count)
        return True

    return False


# not used
def generateCandidates(ds, minSup, maxItemLength):
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
    #print(letters)
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
    #set of 1-frequent items
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

    print("generated data", table)
    return table


if __name__ == "__main__":
    #a = input("give number of transactions: ")
    #b = input("give maximum length of a sequence: ")
    #c = input("give maximum length of a itemset: ")
    #d = input("give maximum number of letter from the alphabet to choose from: ")
    #e = input("give minimum support: ")

    #dataset = generateData(4, 3, 2, 5)
    #vds, f = generateCandidates(dataset, minSup, maxItemLength)

    minSup = 2
    ds = [(0, [['a', 'b', 'e'], ['c'], ['f', 'g'], ['g'], ['e']]),
          (1, [['a', 'd'], ['c'], ['b'], ['a', 'b', 'e', 'f'], ['g']]),
          (2, [['a'], ['b'], ['f'], ['e']]),
          (3, [['b'], ['f', 'g']])]
    f = [['a'], ['b'], ['c'], ['e'], ['f'], ['g']]
    spam(ds, minSup, f)
