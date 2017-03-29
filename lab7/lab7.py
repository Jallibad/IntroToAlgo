import heapq
from collections import defaultdict
import sys
import io

def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))



def main():
    if sys.argv[1] == "text":
        with open("Lab7.txt",encoding='utf8') as file:
            frequency = defaultdict(int)
            for line in file:
                for symbol in line:
                    frequency[symbol] += 1
             
            huff = encode(frequency)
            temp = 0
            print("Symbol".ljust(10) + "Huffman Code")
            for p in huff:
                print(("'"+p[0]+"'").replace('\n','\\n').ljust(10) + p[1])
                temp = temp + len(str(p[1]))*frequency[p[0]]
                 
            print("The total length of the coding is:", temp)
            
        string = ""
        with open("Lab7.txt",encoding='utf8') as file:
            for line in file:
                for symbol in line:
                    for p in huff:
                        if p[0] == symbol:
                            string = string + str(p[1])
        print("The encoded string is:",string)
              
    elif sys.argv[1] == "mississippi":
        data = "mississippi"
        frequency = defaultdict(int)
        for symbol in data:
            frequency[symbol] += 1
        
        huff = encode(frequency)
        temp = 0
        print("Symbol".ljust(10) + "Huffman Code")
        for p in huff:
            print(p[0].ljust(10) + p[1])
            temp = temp + len(str(p[1]))*frequency[p[0]]
            
        print("The total length of the coding is:", temp)
        
        string = ""
        for symbol in data:
            for p in huff:
                if p[0] == symbol:
                    string = string + str(p[1])
        
        print("The encoded string is:",string)    


if __name__ == '__main__':
    main()
