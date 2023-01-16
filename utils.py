#!/usr/bin/env python3

from bitstring import BitArray
import random as rd

def intToBin(a):
    binary = []
    for i in a:
        cifraBin = []
        for j in bin(i).replace("0b",""):
            cifraBin.append(int(j))
        x = cifraBin[::-1]
        while len(x) < 4:
            x += [0]
        cifraBin = x[::-1]
        binary += cifraBin
    return binary

def binToInt(a):
    b = []
    for i in a:
        b.append(int(i))
    intt = []
    i = 0
    for i in range(3, len(a), 4):
        bitlist = b[i-3:i+1]
        c = BitArray(bitlist)
        intt.append(c.uint)
    return intt

def sboxInverse(sbox):
    inv_sbox = {}
    for k,v in sbox.items():
        inv_sbox[v] = k
    return inv_sbox 

def linearApprox(input_int, output_int, sbox):
    """
    punto a: generazione tabella contenente i valori di Nd
    """
    total = 0
    for ii in range(16):
        input_masked = ii & input_int
        output_masked = sbox[ii] & output_int
        if (bin(input_masked).count("1") - bin(output_masked).count("1")) % 2 == 0:
            total += 1 
    result = total - (16//2)
    if result > 0:
        result = "+" + str(result)
    else:
        result = str(result)
    return result

