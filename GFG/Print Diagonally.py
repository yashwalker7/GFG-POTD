def downwardDigonal(N, A): 
    # code here 
    map = {}
    
    for row in range(N):
        for coloumn in range(N):
            key = row + coloumn
            if key not in map:
                map[key] = []
            map[key].append(A[row][coloumn])
            
    output = []
    key = 0
    while key in map:
        output += map[key]
        key += 1
        
    return output
