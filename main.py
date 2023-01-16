#!/usr/bin/env python3

import linearAttackExercise as l
import linearAttackExample as ll

from diffAttack import differentialAttack,calcolaCombinazioni
import random as rd
import time

print("------------------------------------------")
print("Attacco di crittoanalisi lineare esercizio 4.15")
k = [ rd.randint(0,15) for _ in range(0,8) ]
k = [6, 11, 12, 8, 15, 1, 4, 9]
print("chiave:",k)
comb = l.createPairs(2000,k)
startTime = time.time()
key = l.linearAttack(comb,l.sbox)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
print("8 bit di chiave trovati:",key)
print("")

print("------------------------------------------")
print("Confronto attacco di crittoanalisi lineare e differenziale (esempio)")
k = [ rd.randint(0,15) for _ in range(0,8) ]
k = [6, 11, 12, 8, 15, 1, 4, 9]
print("chiave:",k)
comb = ll.createPairs(9000,k)

startTime1 = time.time()
key = ll.linearAttack(comb,ll.sbox)
executionTime = (time.time() - startTime1)
print('Execution time in seconds: ' + str(executionTime))
print("8 bit di chiave trovati con attacco lineare:",key)

comb = calcolaCombinazioni(11,k)
startTime2 = time.time()
key = differentialAttack(comb,ll.sbox)
executionTime = (time.time() - startTime2)
print('Execution time in seconds: ' + str(executionTime))
print("8 bit di chiave trovati con attacco differenziale:",key)
