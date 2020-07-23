"""
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

"""

class Solution:
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)

        return points[:K]

if __name__ == "__main__":

    #points = [[1, 3], [-2, 2]]
    #K = 1

    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    s=Solution().kClosest(points,2)
    print(s)