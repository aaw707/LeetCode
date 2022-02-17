class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        round_distance = sum(distance)
        average_distance = round_distance / 2
        print("average_distance:", average_distance)
        
        clockwise_distance = 0
        if destination >= start:
            my_start = start
            my_des = destination
        else:
            my_start = destination
            my_des = start

        for stop in range(my_start, my_des):
            print("stop:", stop)
            print("distance[stop]:", distance[stop])
            clockwise_distance += distance[stop]

        print("clockwise_distance:", clockwise_distance)
        if clockwise_distance <= average_distance:
            return clockwise_distance
        else:
            return round_distance - clockwise_distance
