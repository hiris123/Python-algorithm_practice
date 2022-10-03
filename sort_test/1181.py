import sys 
n = int(input())

word_list =[ input() for _ in range(n)]

### 버블 정렬 사용해서 풀어보기 ## 


def bubbleSort(word_list):
    
    for x in range(len(word_list)) : 
        small = x 
        temp = 0 
        for j in range(len(word_list) -1 ,x, -1):
            if len(word_list[j-1]) > len(word_list[j]):                                                                                                                                                                                                                                                                      
                temp = word_list[j-1]
                word_list[j-1] = word_list[j]
                word_list[j] = temp 
def rebubbleSort(word_list):
    for x in range(len(word_list)):
        for j in range(x+1, len(word_list)):
            if (len(word_list[j-1]) == len(word_list[j]) )and (word_list[j-1] > word_list[j]): 
                
                temp = word_list[j-1]
                word_list[j-1] = word_list[j]
                word_list[j] = temp 

bubbleSort(word_list)   
rebubbleSort(word_list)
print(word_list)