def solution(players, callings):
    
    hashmap = dict()
    for rank, name in enumerate(players):
        hashmap[name] = rank
    for call in callings:
        front, back = hashmap[call]-1, hashmap[call]
        hashmap[players[front]], hashmap[players[back]] = back, front
        players[front], players[back] = players[back], players[front]
    
    return players
