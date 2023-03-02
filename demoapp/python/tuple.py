#map(int, input().strip().split()) 
#map() takes two arguments. 
# The first one is the method to apply, 
# the second one is the data to apply it to. 
# By this understanding, we can see this is doing nothing
#  but typecasting every element of the list to an integer value.
#  Since map returns the data type it was applied to, the list() method applied over map() is redundant.
#  So now we have covered the following:

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().strip().split())
    print(hash(tuple(integer_list)))