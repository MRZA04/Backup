s1 = set()
s2 = set()

def sets():
    counter = 0
    while counter < 4:
        add = input("Add an object from the classroom: ")
        s1.add(add)
        counter = counter + 1
    
    counter = 0
    while counter < 5:
        add = input("Add an object from your bedroom: ")
        s2.add(add)
        counter = counter + 1
    
    print (s1)
    print (s2)
    s3 = s1|s2
    print (s3)
    s3.pop()
    print(s3)
    s4 = s1&s2
    print(s4)
    s5 = s1-s2
    print (s5)



sets()