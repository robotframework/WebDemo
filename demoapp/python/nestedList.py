if __name__ == '__main__':
        d1 =dict()
        l2 =list() 
        l4= list()
        for _ in range(int(input())):
            name = input()
            score = float(input())
            d1[name]=score
        for k,v in d1.items():
            l2.append(v)
    l3 =sorted(l2,reverse=True)
    v = l3.pop()
    for val in l3:
        if(val ==v):
            l3.pop()
    for k,v in d1.items():
        if(v == l3[-1]):
            l4.append(k)
    for v in sorted(l4):
        print (v) 
