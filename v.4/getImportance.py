class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        ans = 0
        for e in employees:
            if e.id == id:
                ans += e.importance
                temp = e.subordinates
                while temp:
                    p = temp.pop(0)
                    for f in employees:
                        if f.id == p:
                            ans += f.importance
                            temp.extend(f.subordinates)
        return ans


