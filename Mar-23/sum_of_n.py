import time

def sum_of_n(n):
    start = time.time()
    
    #sum
    total = 0
    for i in range(1, n+1):
        total += i
    
    #end time
    end = time.time()
    
    return total, end - start
    
def main():
    print(sum_of_n(100000))
    print(sum_of_n(1000000))
    print(sum_of_n(5000000))
    
main()

# Results from my home computer
# (5000050000, 0.0043621063232421875)
# (500000500000, 0.04368114471435547)
# (12500002500000, 0.2192237377166748)
