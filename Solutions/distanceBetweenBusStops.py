class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockWiseDirection = 0
        totalSum = 0

        for idx, val in enumerate(distance):
            if start < destination and (idx >= start and idx < destination ):
                clockWiseDirection += val

            if start > destination and (idx >= start or idx < destination ):
                clockWiseDirection += val

            totalSum += val

        return min(clockWiseDirection, totalSum-clockWiseDirection)