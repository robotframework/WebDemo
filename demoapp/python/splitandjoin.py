def split_and_join(line):
    # write your code here
    l1 = line.split(" ")
    l2 = "-".join(l1)
    return l2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)