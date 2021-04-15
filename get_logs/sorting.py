#-*- coding: utf-8 -*-
from datetime import datetime

def sort(data, key):
    merge_sort(data, key)
    return data

def compare(first, second, key): #True if second >= first
    if key == 'created_at':
        a = datetime.fromisoformat(first[key])
        b = datetime.fromisoformat(second[key])
    else:
        a = first[key]
        b = second[key]
    if a <= b:
        return True
    else:
        return False

def merge_sort(data, key):
    if len(data) == 1 or len(data) == 0:
        return
    L, R = data[:len(data) // 2], data[len(data) // 2:]
    merge_sort(L, key)
    merge_sort(R, key)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if compare(L[n], R[m], key):
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(data)):
        data[i] = C[i]
