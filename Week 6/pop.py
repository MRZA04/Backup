def revstr(inpstr):
    christ = list(inpstr)
    revedstr = ""

    while christ:
        revedstr += christ.pop()
        
    return revedstr
    
imp = input("Because Do: ")
output = revstr(imp)
print ("revedstr: ", output)