class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            temp = start
            start = destination
            destination = temp
        cw = 0
        acw = 0
        for i in range(start, destination):
            cw += distance[i]
        for j in range(destination, len(distance)):
            acw += distance[j]
        if start != 0:
            for i in range(start):
                acw += distance[i]
        return min(cw, acw)
