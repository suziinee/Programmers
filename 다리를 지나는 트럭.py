def solution(bridge_length, weight, truck_weights):
    
    from collections import deque
    sum_truck = 0
    bridge = deque([0] * bridge_length)
    after_bridge = deque()
    truck_weights = deque(truck_weights)
  
    while bridge :  
        finish_truck = bridge.popleft()
        sum_truck -= finish_truck
        after_trucks.append(finish_truck)
        if truck_weights :     
            if (sum_truck + truck_weights[0]) <= weight : 
                pop_truck = truck_weights.popleft()
                bridge.append(pop_truck)
                sum_truck += pop_truck
            else :
                bridge.append(0)

    return len(after_trucks)

