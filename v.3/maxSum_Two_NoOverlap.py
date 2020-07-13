"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array A of non-negative integers,
return the maximum sum of elements in two non-overlapping (contiguous) subarrays,
which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)
"""

#answer 1.
# time : O(n^2) , space : O(n)
def maxSumTwoNoOverlap(A: list, L: int, M: int) -> int:
    def findMaxSum(A, L, M):
        max_num = -1

        for i in range(len(A) - L):
            L_slice = A[i: L + i]
            L_sum = sum(L_slice)
            for j in range(L + i, len(A)):
                M_slice = A[j: M + j]
                M_sum = sum(M_slice)
                max_num = max(L_sum + M_sum, max_num)
        return max_num

    forwords_sum = findMaxSum(A, L, M)
    A.reverse()
    backwards_sum = findMaxSum(A, L, M)

    return max(forwords_sum, backwards_sum)

#answer 2.
# time : O(n) , space : O(1)

def maxSumTwoNoOverlap(A: list, L: int, M: int) -> int:

    if len(A) < L + M:
        return -1

    for i in range(1, len(A)):
        A[i] += A[i - 1]

    result, L_max, M_max = A[L + M - 1], A[L - 1], A[M - 1]

    for i in range(L + M, len(A)):
        L_max = max(L_max, A[i - M] - A[i - M - L])
        M_max = max(M_max, A[i - L] - A[i - L - M])
        result = max(result, L_max + A[i] - A[i - M], M_max + A[i] - A[i - L])

    return result


if __name__ == "__main__":
    A = [4,0,1]
    L = 2
    M = 1

    result = maxSumTwoNoOverlap(A,L,M)

    print(result)
