#!/usr/bin/env python3

from utils import *
from spn import keyschedule,encrypt

sbox = {0x0: 0x8,0x1: 0x4,0x2: 0x2,0x3: 0x1,0x4: 0xC,0x5: 0x6,0x6: 0x3,0x7: 0xD,0x8: 0xA,0x9: 0x5,0xA: 0xE,0xB: 0x7,0xC: 0xF,0xD: 0xB,0xE: 0x9,0xF: 0x0}

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
                u4_1 = sbox_inv[l1 ^ y[0]]
                u4_3 = sbox_inv[l2 ^ y[2]]
                u4_1bin = intToBin([u4_1])
                u4_3bin = intToBin([u4_3])
                z = x1[15]^u4_1bin[0]^u4_3bin[0]

                if z == 0:
                    count[l1][l2] += 1
    max = -1
    for l1 in range(0,16):
        for l2 in range(0,16):
            count[l1][l2] = abs(count[l1][l2] - (len(T)/2))
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
