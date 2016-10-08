"""Copyright 2016 WaizungTaam.  All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
- 2016-10-08
- waizungtaam@gmail.com
- Reference: https://en.wikipedia.org/wiki/Gaussian_elimination

"""

def pivot_row(A, k):
    i_max = k
    for i in range(k + 1, len(A)):
        if abs(A[i][k]) > abs(A[i - 1][k]):
            i_max = i
    return i_max
    
def forward_eliminate(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n)):
        i_max = pivot_row(A, k)
        if A[i_max][k] == 0:
            break
        A[k], A[i_max] = A[i_max], A[k]  # Operation 1: swap
        for i in range(k + 1, m):
            c = A[i][k] / A[k][k]  # Operation 3: linear
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - c * A[k][j]
            A[i][k] = 0

def backward_substitute(A):
    m, n = len(A), len(A[0])    
    for k in range(min(m, n) - 1, 0, -1):  # [min(m, n), 1]
        if A[k][k] == 0:
            continue
        for i in range(k - 1, -1, -1):  # [k - 1, 0]
            c = A[i][k] / A[k][k]
            for j in range(i, n):
                A[i][j] = A[i][j] - c * A[k][j]  # Operation 3: linear
    for i in range(min(m, n)):
        if A[i][i] == 0:
            continue
        for j in range(n - 1, i - 1, -1):  # [n - 1, i]
            A[i][j] = A[i][j] / A[i][i]  # Operaton 2: scale

def gaussian_eliminate(A):
    forward_eliminate(A)
    backward_substitute(A)


def demo():
    A = [[1, 3, 1, 9], \
         [1, 1, -1, 1], \
         [3, 11, 5, 35]]
    gaussian_eliminate(A)
    for r in A:
        print(r)
    print()

    B = [[2, 1, -1, 8], \
         [-3, -1, 2, -11], \
         [-2, 1, 2, -3]]
    gaussian_eliminate(B);  ### floating point problem ...
    for r in B:
        print(r)

if __name__ == "__main__":
    demo()