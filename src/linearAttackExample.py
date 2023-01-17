#!/usr/bin/env python3

from utils import *
from spn import keyschedule,encrypt

#esempio
sbox = {0x0: 0xE,0x1: 0x4,0x2: 0xD,0x3: 0x1,0x4: 0x2,0x5: 0xF,0x6: 0xB,0x7: 0x8,0x8: 0x3,0x9: 0xA,0xA: 0x6,0xB: 0xC,0xC: 0x5,0xD: 0x9,0xE: 0x0,0xF: 0x7}

def linearAttack(T,sbox):
    """
    punto d: implementazione dell'attacco
    """
    sbox_inv = sboxInverse(sbox)
    count = []
    maxkey = ()
    for l1 in range(0,16):
        countRow = []
        for l2 in range(0,16):
            countRow.append(0)
        count.append(countRow)

    for (x,y) in T:
        x1 = intToBin(x)
        for l1 in range(0,16):
            for l2 in range(0,16):
                u4_2 = sbox_inv[l1 ^ y[1]]
                u4_4 = sbox_inv[l2 ^ y[3]]
                u4_2bin = intToBin([u4_2])
                u4_4bin = intToBin([u4_4])
                z = x1[4]^x1[6]^x1[7]^u4_2bin[1]^u4_2bin[3]^u4_4bin[1]^u4_4bin[3]

                if z == 0:
                    count[l1][l2] += 1
    max = -1
    for l1 in range(0,16):
        for l2 in range(0,16):
            count[l1][l2] = abs(count[l1][l2] - (len(T)//2))
            if count[l1][l2] > max:
                max = count[l1][l2]
                maxkey = (l1,l2)
    return maxkey

def createPairs(n,k):
    """
    Generatore di coppie del tipo (x,y), dove x è una stringa da 4 byte 
    e y è una stringa di 4 byte tale che y = encrypt(x)
    """
    list = []
    i = 0
    while i != n:
        x = [rd.randint(0,15) for _ in range(0,4)]
        if x not in list:
            list.append(x)
            i += 1
    pairs = []
    for x in list:
        y = encrypt(x,sbox,keyschedule(k))
        pairs.append((x,y))
    return pairs
