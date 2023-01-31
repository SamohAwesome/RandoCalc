import random


done = False
print('if the number does not divide it will go forever, have fun!')
divided = float(input('the number to be divided '))
divisor = float(input('the number that divideds '))
counter1 = int(1)
counter2 = int(0)
prescion = 100000
def getRandomNum():
     x = random.randint(prescion, (divided*prescion))/prescion
     return x

def randCalc(done, divided, divisor, counter1, counter2, prescion):
    while done == False:
        x = getRandomNum()
        b = x
        if round((float(divided) / b), 5) == round(float(divisor),5):
            done = True
            print(str(b))
            print("this is the " + str((counter2*prescion) + int(counter1)) + "th attempt")
            
        else:
            if counter1 == prescion:
                counter2 += 1
                print('its not ' + str(b))
                print("this is the " + str((counter2*prescion)) + "th attempt")
                counter1 = 1
            else:
                counter1 += 1

randCalc(done, divided, divisor, counter1, counter2, prescion)




