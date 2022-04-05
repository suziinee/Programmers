def solution(bridge_length, weight, truck_weights):
    
    from collections import deque
    sum_truck = 0
    timer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
  
    while bridge :  
        timer += 1
        sum_truck -= bridge.popleft()
        if truck_weights :     
            if (sum_truck + truck_weights[0]) <= weight : 
                pop_truck = truck_weights.popleft()
                bridge.append(pop_truck)
                sum_truck += pop_truck
            else :
                bridge.append(0)

    return timer





    