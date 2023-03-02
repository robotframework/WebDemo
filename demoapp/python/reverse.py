n=int(input("Enter number: "))
print(str(n)[::-1])

while n > 0:
    rem = n % 10                  # extract the last digit
    reverse = reverse * 10 + rem    # append rem to the end of the reversed number
    n //= 10   # drop the last digit

n=(input("Enter string: "))
print(str(n)[::-1])

#Using the string slicing concept, 
# you can get reverse the string. ::-1 corresponds
#  to start:stop:step. When you pass -1 as step, 
# the start point goes to the end and stop at the front.