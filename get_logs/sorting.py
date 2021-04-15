#-*- coding: utf-8 -*-

def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n]["created_at"] <= R[m]["created_at"]:
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
    for i in range(len(A)):
        A[i] = C[i]
