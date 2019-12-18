#!/bin/python3

import math
import os
import random
import re
import sys

def sub_lists(my_list):
    subs = [[]]
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1

    return subs

def calculate_score(start, end, genes, health, d):
    score = 0
    g = genes[start : end + 1]
    h = health[start : end + 1]
    dna = sub_lists(d)
    print(g)
    print(dna)
    for gene_dna in dna:
        i = start
        for gene in g:
            if (gene == gene_dna):
                score = score + health[i]
                print(score)
            i = i + 1
    
    return score

if __name__ == '__main__':
    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input())

    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        score = calculate_score(first, last, genes, health, d)
        if (s_itr == 0):
            max_score = score
            min_score = score
        
        else:
            if(score > max_score):
                max_score = score
            
            if(score < min_score):
                min_score = score
    
    print("{} {}".format(min_score, max_score))
