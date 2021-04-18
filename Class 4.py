print("\t\t\tCalculator\n")
print("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\nPress 5 to exit the Calculator")
usr=int(input('\nEnter your choice: '))
def add(num1,num2):
    result=num1+num2
    print("Addition Result is: ",result)
def sub(num1,num2):
    result=num1-num2
    print("subtraction Result is: ",result)
def mul(num1,num2):
    result=num1*num2
    print("Multiplication Result is: ",result)
def div(num1,num2):
    if(num2==0):
        print("Cannot Divide by Zero")
    else:
        result=num1/num2
        print("Division Result is: ",result)
if usr==1:
    add(int(input('Enter First Number: ')),int(input('\nEnter Second Number: ')))
elif usr==2:
    sub(int(input('Enter First Number: ')),int(input('Enter Second Number: ')))
elif usr==3:
    mul(int(input('Enter First Number: ')),int(input('Enter Second Number: ')))
elif usr==4:
    div(int(input('Enter First Number: ')),int(input('Enter Second Number: ')))
else:
    print("Invalid Output")
    
