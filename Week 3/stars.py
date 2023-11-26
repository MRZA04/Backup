def main():
    counter = 0
    for counter in range (1,5,1):
        star()
        counter = counter + 1


def star():
    x=1
    for x in range  (1,10,1): 
        print ("👌"*x)
        x=x+1

main()