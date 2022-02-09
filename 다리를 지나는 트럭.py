def solution(bridge_length, weight, truck_weights):
    
    from collections import deque
    answer = 0
    bridge = [0] * bridge_length
    after_bridge = []
    truck_weights = deque(truck_weights)
  
    while truck_weights :  
        try :  
            while (sum(bridge[1:]) + truck_weights[0]) <= weight : 
                bridge.append(truck_weights.popleft())
                after_bridge.append(bridge[0])
                bridge.pop(0)
                answer += 1
            else :
                bridge.append(0)
                after_bridge.append(bridge[0])
                bridge.pop(0)
                answer += 1

        except : 
            return answer + len(bridge)