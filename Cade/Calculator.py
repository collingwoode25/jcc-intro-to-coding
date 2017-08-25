number1=raw_input("give me a # ")
number1=int(number1)
number2=raw_input("give me another ")
number2=int(number2)
operation=raw_input("what operation do you want ")
if operation=='+':
	answer=number1+number2
elif operation=='-':
	answer=number1-number2
elif operation=='/':
	answer=number1/number2
elif operation=='*':
	answer=number1*number2
	
print(answer)
