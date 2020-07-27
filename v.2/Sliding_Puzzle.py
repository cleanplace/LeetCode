"""
773. Sliding Puzzle

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:
1)
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

2)
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

3)
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.

An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

4)
Input: board = [[3,2,4],[1,5,0]]
Output: 14

Note:
board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

"""

import collections

class Solution:
    def slidingPuzzle(self, board):
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)

        # define possible moves of zero
        moves = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }
        visited = set()
        visited.add(start)
        queue = collections.deque()
        queue.append((start, start.index('0')))
        count = 0

        while queue:
            size = len(queue)

            for i in range(size):
                curr, index = queue.popleft()
                # find target
                if curr == target:
                    return count

                # search
                curr = list(curr)
                for move in moves[index]:
                    new_string = curr.copy()
                    new_string[move], new_string[index] = new_string[index], new_string[move]
                    new_string = ''.join(new_string)

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, move))
            count += 1
        return -1
