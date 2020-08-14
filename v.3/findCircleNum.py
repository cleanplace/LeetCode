"""
547. Friend Circles

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

"""

##Union-Find Method
def find(parent, i):
    if (parent[i] == -1):
        return i
    return find(parent, parent[i])

def union(parent, i, j):
    xset = find(parent, i)
    yset = find(parent, j)
    if (xset != yset):
        parent[xset] = yset

class Solution:

    def findCircleNum(self, M):
        parent = [-1 for i in range(len(M))]

        for i in range(len(M)):
            for j in range(len(M[0])):
                if (M[i][j] == 1) and (i != j):
                    union(parent, i, j)

        count = 0
        for i in range(len(parent)):
            if parent[i] == -1:
                count += 1

        return count

if __name__ == "__main__":

    M = [[1,1,0],[1,1,0],[0,0,1]]
    s = Solution()
    result = s.findCircleNum(M)

    print(result)