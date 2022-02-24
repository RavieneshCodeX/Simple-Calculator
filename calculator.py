from math import sqrt

def input_req():
    firstNum = int(input('Please enter the First Number: '))
    operator = input('Please enter the operator: ')
    secondNum = int(0) 
    
    if operator != "√":
        secondNum = int(input('Please enter the Second Number: '))
        
    start_calc(firstNum, operator, secondNum)

def start_calc(firstNum, operator, secondNum):
    if operator == '+':
        Answer = firstNum + secondNum
        print(Answer)
        

    elif operator == '-':
        Answer = firstNum - secondNum
        print(Answer)
        

    elif operator == '*':
        Answer = firstNum * secondNum
        print(Answer)
        

    elif operator == '/':
        Answer = firstNum / secondNum
        print(Answer)
       

    elif operator == '**':
        Answer = firstNum ** secondNum
        print(int(Answer))
        

    elif operator == '√':
        Answer = sqrt(int(firstNum))
        print(int(Answer))
        
    
    else:
        print('Invalid operator please use +,-,*,/,** or √ ')
        
    loop_ask = input("Do you want to calculate again? (Yes/No) ")
 
    if loop_ask == "Yes":
        input_req()    
 
input_req()