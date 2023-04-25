def seq_search(items, desired):
    for item in items:
        if item == desired:
            print("FOUND IT!!!")
            return True
    print ("No dice! :'( ")
    return False

def main():
    items = [55, 12, 13, -3, 9]
    
    print(seq_search(items, 13)) #Expecting True
    print(seq_search(items, 100)) #Expecting False

main()
