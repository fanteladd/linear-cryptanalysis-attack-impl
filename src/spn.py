#!/usr/bin/env python3

from utils import binToInt,intToBin,sboxInverse

def permutation(x):
    """
    given a list x containing four 4-bit numbers,
    return a list permuted containing four 4-bit numbers such that 'permuted' is the
    permutation according to the defined spn of the input list
    """
    binary = intToBin(x)
    permuted = []
    for i in range(0,4):
        permuted.append(binary[0+i])
        permuted.append(binary[4+i])
        permuted.append(binary[8+i])
        permuted.append(binary[12+i])
    permuted = binToInt(permuted)
    return permuted

def inv_permutation(x):
    binary = intToBin(x)
    permuted = []
    for i in reversed(range(0,4)):
        permuted.append(binary[3-i])
        permuted.append(binary[7-i])
        permuted.append(binary[11-i])
        permuted.append(binary[15-i])
    permuted = binToInt(permuted)
    return permuted

def keyschedule(k):
    """
    Given a 32-bit key 'k', i.e., a list where each element in the list is a 4-bit number,
    returns a list 'listkey' of five 16-bit keys, where the i+1-th key is the round key for round i+1
    """
    listkey = []
    for i in range(0,5):
        ki = list(k[i:i+4])
        listkey.append(ki)
    return listkey

def encrypt(x,sbox,keyschedule):
    """
    Given a 16-bit plain text, an sbox, and a list containing the key schedule given by a key k,
    returns a 16-bit ciphertext obtained using the key k
    """
    u = x.copy()
    for r in range(0,3):
        for i in range(0,len(u)):
            u[i] = (sbox[u[i] ^ keyschedule[r][i]])
        u = permutation(u)
    for i in range(0,len(u)):
        u[i] = (sbox[u[i] ^ keyschedule[3][i]])
    for i in range(0,len(u)):
        u[i] = (u[i] ^ keyschedule[4][i])
    return u

def decrypt(y,sbox,keyschedule):
    """
    Given a 16-bit cipher text, an sbox, and a list containing the key schedule given by a key k,
    returns a 16-bit plain text obtained using key k
    """
    u = y.copy()
    sbox_inv = sboxInverse(sbox) 
    for i in range(0,len(u)):
        u[i] = (u[i] ^ keyschedule[4][i])
    for i in range(0,len(u)):
        u[i] = sbox_inv[u[i]]
        u[i] = u[i] ^ keyschedule[3][i]
    for r in reversed(range(0,3)):
        u = inv_permutation(u)
        for i in range(0,len(u)):
            u[i] = sbox_inv[u[i]]
            u[i] = u[i] ^ keyschedule[r][i]
    return u
