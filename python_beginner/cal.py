num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation=input("Enter the operation(+,-,/,*):")
if operation=='+':
    result=num1+num2
    print("Result:",result)
elif operation =='-':
    result=num1-num2
    print("Result:",result)
elif operation =='*':
    result=num1*num2
    print("Result:",result)
elif operation =='/':
    if num2 !=0:
       result=num1/num2
       print("Result:",result)    
    else:
       print("error: cannot divide by zero")
else:
   print("invalid operation .please enter +,-,/,*" )        
