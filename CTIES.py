Cities = []
while True:
    add = input("ENTER CITY NAME OR ENTER DONE TO FINISH: \n").lower().strip()
    if add == "done":
        break
    else:
        if add.title() not in Cities:
            Cities.append(add.title())
        else:
            print("CITY HAS ALREADY BEEN ENTERED")

print(Cities[0])
print(Cities[-1])
Cities.sort()
print(Cities)
Cities.pop()
print(Cities)
print(Cities[len(Cities)-1])