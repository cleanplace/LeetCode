class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """

        steps = 0
        while target > startValue:
            steps += 1 + target % 2
            target += target % 2
            target //= 2

        return steps + (startValue - target)