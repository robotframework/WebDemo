n=int(input("Enter number: "))
result=0
length = len(str(n))
for i in range(length):
    temp = str(n)[i:i+1]
    print("digit "+str(pow(int(temp),3)))
    result = result + pow(int(temp),3)

print(result)
if(n == result):
    print("Number is an armstrong number")
else:
    print("Number is not armstrong number")


