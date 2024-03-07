def solve_puzzle(array, position=0, visited=None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    end = len(array) - 1
    if visited == None:
        visited = set()

    # 1) Base case: have you found a valid solution?
    if position == end:
        return True
    if position in visited:
        return False
    
    visited.add(position)

    # 2) Find all valid next-steps
    next_cw = (position + array[position]) % len(array)
    next_ccw = (position - array[position]) % len(array)

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    return solve_puzzle(array, next_cw, visited) or solve_puzzle(array, next_ccw, visited)

print(solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0]))   #True
print(solve_puzzle([3, 4, 1, 2, 0]))            #False
