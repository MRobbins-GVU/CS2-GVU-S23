

def binary_search(values, item):
    # Sort the list
    values.sort()
    
    # Starting indices of these points
    left = 0
    midpoint = len(values) // 2
    right = len(values) - 1
    print(left, midpoint, right)
    
    while left <= right:
        # we find what we're looking for!
        if (item == values[midpoint]):
            print("equal!")
            return True
        
        # we know it's impossible
        
        
        # we need to move left
        elif(item < values[midpoint]):
            print("move left")
            temp = midpoint
            midpoint = (midpoint+left) // 2
            right = temp - 1
            print(left, midpoint, right)
        
        # we need to move right
        elif(item > values[midpoint]):
            print("move right")
            temp = midpoint
            midpoint = (midpoint+right) // 2
            left = temp + 1
            print(left, midpoint, right)
    
    return False
    
def main():
    values = [3, -1, 18, 45, 101]
    print(binary_search(values, 45)) #Expect True
    print(binary_search(values, 500)) #Expect False
    
main()

