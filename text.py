d1={"eid":1001,"ename":"Rahul Verma","esal":23000,"design":"DAD"}
def Test_Case1():
    for x,y in d1.items():
        print(x,"---",y)
def Test_Case2():
    for obj1,obj2 in d1.items():
        print(obj1,"----",obj2)
def Test_Case3():
    for m,n in d1.items():
        print(m,"----",n)
if(__name__=="__main__"):
    Test_Case1()
    print()
    Test_Case2()
    print()
    Test_Case3()
    print()
    for o1,o2 in d1.items():
        print(o1,"---",o2)
        