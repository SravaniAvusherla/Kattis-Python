num = list(map(int, input().split()))
string = input()

def orderNum(num, string):
    answer = []
    num.sort()
    temp = {"A" : num[0], "B" : num[1], "C" : num[2]}
    
    for i in string:
        answer.append(str(temp.get(i))) 
    
    return answer[0] + " " +answer[1] + " " + answer[2]
    
print(orderNum(num, string))
