def add (a, b):
	return a + b
def sub (a, b):
	return a - b
def mul (a, b):
	return a * b
def div (a, b):
	 if b == 0:
	      return "error"
	 return a / b
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = input ("choose 1/2/3/4: ")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
if choice == "1":
	print(add(a, b))
elif choice == "2":
	print(sub(a, b))
elif choice == "3":
	print(mul(a, b))
elif choice == "4":
	print(div(a, b))
else:
	print ("invalid choice")
