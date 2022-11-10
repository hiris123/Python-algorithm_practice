

EX_string = input()


## 균형잡힌 괄호 문자열

str =""


def String(string):
    count = 0
    temp = 0 
    for x in range(len(string)):
        if string[x] == "(":
            count += 1
        else:
            count -= 1 
        if count == 0:
            
           temp = x 
           return string[:temp+1], string[temp+1:]


bools= True
while (True):
    
    u, v =String(EX_string)
    ## u와 v로 나눠준다. 
    u,v = String(u)
    
    if u == "":
        str += v 
    if u[0] ==")":
        u[0] = "("
        
    print(str)

## 올바른 괄호 문자열 