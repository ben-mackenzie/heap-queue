import sys
import time
from heap import HeapQueue


def driver():
    #CODE FOR IN.TXT
    fin = open("in.txt", "r")
    #redirects print statements to output file
    sys.stdout = open("out.txt", "w")
    #converts in.txt to list of ints
    lyst = [int(e) for e in fin.read().strip().split(' ')]
    fin.close()
    #creates empty heap
    h = HeapQueue(lyst)
    print("Heap-based Priority Queue test on random list")
    print("\n")
    #builds heap from list of ints
    for item in lyst:
        h.insert(item)
    print("heap after building:")
    print(h)
    print("\n")
    #tests insert method
    item = 14
    h.insert(item)
    print("heap after inserting 14:")
    print(h)
    print("\n")
    #tests delete method
    h.deleteMin()
    print("heap after deleting min:")
    print(h)
    print("\n")
    sys.stdout.close()
    
    #CODE FOR IN2.TXT
    fin2 = open("in2.txt", "r")
    #redirects print statements to output file
    sys.stdout = open("out2.txt", "w")
    #converts in.txt to list of ints
    lyst2 = [int(e) for e in fin2.read().strip().split(' ')]
    fin2.close()
    #creates empty heap
    h2 = HeapQueue(lyst2)
    print("Heap-based Priority Queue test on ascending list")
    print("\n")
    #builds heap from list of ints
    for item in lyst2:
        h2.insert(item)
    print("heap after building:")
    print(h2)
    print("\n")
    #tests insert method
    item2 = 14
    h2.insert(item2)
    print("heap after inserting 14:")
    print(h2)
    print("\n")
    #tests delete method
    h2.deleteMin()
    print("heap after deleting min:")
    print(h2)
    print("\n")
    sys.stdout.close()
    
    #CODE FOR IN3.TXT
    fin3 = open("in3.txt", "r")
    #redirects print statements to output file
    sys.stdout = open("out3.txt", "w")
    #converts in.txt to list of ints
    lyst3 = [int(e) for e in fin3.read().strip().split(' ')]
    fin3.close()
    #creates empty heap
    h3 = HeapQueue(lyst3)
    #10 insertions of random values w/ CPU timing
    print("Heap-based Priority Queue test on random list w/ CPU timing")
    print("10 timed insertions, 10 timed deletions:")
    print("\n")
    #builds heap from list of ints
    i = 0
    for item in lyst3:
        i += 1
        t1 = time.clock()
        h3.insert(item)
        t2 = time.clock()
        print("heap after insertion number " + str(i))
        print(h3)
        print("time to insert: " + str(t2-t1))
        print("\n")
    #10 deletions of min randoms w/ CPU timing
    i = 0
    for item in lyst3:
        i += 1
        t1 = time.clock()
        h3.deleteMin()
        t2 = time.clock()
        print("heap after deletion number " + str(i))
        print(h3)
        print("time to delete: " + str(t2-t1))
        print("\n")
    sys.stdout.close()
    
    #CODE FOR IN4.TXT
    fin4 = open("in4.txt", "r")
    #redirects print statements to output file
    sys.stdout = open("out4.txt", "w")
    #converts in.txt to list of ints
    lyst4 = [int(e) for e in fin4.read().strip().split(' ')]
    fin4.close()
    #creates empty heap
    h4 = HeapQueue(lyst4)
    print("Heap-based Priority Queue test on descending list")
    print("\n")
    #builds heap from list of ints
    for item in lyst4:
        h4.insert(item)
    print("heap after building:")
    print(h4)
    print("\n")
    #tests insert method
    item4 = 14
    h4.insert(item4)
    print("heap after inserting 14:")
    print(h4)
    print("\n")
    #tests delete method
    h4.deleteMin()
    print("heap after deleting min:")
    print(h4)
    print("\n")
    sys.stdout.close()
    
if __name__ == '__main__':
    driver()
